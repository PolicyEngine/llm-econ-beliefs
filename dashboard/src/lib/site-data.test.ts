import { describe, expect, test } from "bun:test";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";

import {
  loadDashboardSummaryData,
  loadRunPayload,
  sumCompleteOrNull,
} from "./dashboard-data";
import {
  loadGatedComparisonModelIds,
  loadModelRegistry,
  tieAveragedRanks,
} from "./site-data";

describe("tieAveragedRanks", () => {
  test("assigns the mean occupied rank to exact ties", () => {
    const ranks = tieAveragedRanks(
      new Map([
        ["wide", 4],
        ["tie-b", 2],
        ["narrow", 1],
        ["tie-a", 2],
      ]),
    );

    expect(Object.fromEntries(ranks)).toEqual({
      narrow: 1,
      "tie-a": 2.5,
      "tie-b": 2.5,
      wide: 4,
    });
  });

  test("supports descending ranks through the same implementation", () => {
    const ranks = tieAveragedRanks(
      new Map([
        ["low", 1],
        ["high-a", 3],
        ["high-b", 3],
      ]),
      true,
    );

    expect(ranks.get("high-a")).toBe(1.5);
    expect(ranks.get("high-b")).toBe(1.5);
    expect(ranks.get("low")).toBe(3);
  });
});

describe("sumCompleteOrNull", () => {
  test("keeps an aggregate untracked when any component is untracked", () => {
    expect(sumCompleteOrNull([1.25, null, 0.75])).toBeNull();
  });

  test("preserves a legitimately tracked zero", () => {
    expect(sumCompleteOrNull([0, 0])).toBe(0);
  });
});

const REGISTRY_HEADER =
  "model_id,display_label,organization,serving_provider_path,model_family,wave\n";

function registryRow(modelId: string, organization = "openai"): string {
  return `${modelId},${modelId} label,${organization},openai_chat_completions,test-family,april_2026\n`;
}

describe("registry and comparison gating", () => {
  test("loads organization/wave metadata and requires matching gated artifacts", () => {
    const resultsDir = fs.mkdtempSync(path.join(os.tmpdir(), "belief-dashboard-"));
    try {
      fs.writeFileSync(
        path.join(resultsDir, "model-registry.csv"),
        REGISTRY_HEADER + registryRow("model-a") + registryRow("model-b", "google"),
      );
      fs.writeFileSync(
        path.join(resultsDir, "elasticity-all-model-comparison.csv"),
        "model_name,quantity_id\nmodel-a,quantity-a\nmodel-a,quantity-b\n",
      );
      fs.writeFileSync(
        path.join(resultsDir, "elasticity-model-rollup.csv"),
        "model_name\nmodel-a\n",
      );

      const registry = loadModelRegistry(resultsDir);
      const gated = loadGatedComparisonModelIds(resultsDir, registry);

      expect(registry.get("model-b")?.organization).toBe("google");
      expect(registry.get("model-b")?.wave).toBe("april_2026");
      expect([...gated]).toEqual(["model-a"]);
    } finally {
      fs.rmSync(resultsDir, { recursive: true, force: true });
    }
  });

  test("rejects duplicate registry IDs and unregistered comparison models", () => {
    const resultsDir = fs.mkdtempSync(path.join(os.tmpdir(), "belief-dashboard-"));
    try {
      fs.writeFileSync(
        path.join(resultsDir, "model-registry.csv"),
        REGISTRY_HEADER + registryRow("model-a") + registryRow("model-a"),
      );
      expect(() => loadModelRegistry(resultsDir)).toThrow("duplicate model_id");

      fs.writeFileSync(
        path.join(resultsDir, "model-registry.csv"),
        REGISTRY_HEADER + registryRow("model-a"),
      );
      fs.writeFileSync(
        path.join(resultsDir, "elasticity-all-model-comparison.csv"),
        "model_name\nmodel-unknown\n",
      );
      fs.writeFileSync(
        path.join(resultsDir, "elasticity-model-rollup.csv"),
        "model_name\nmodel-unknown\n",
      );
      expect(() => loadGatedComparisonModelIds(resultsDir)).toThrow(
        "unregistered model",
      );
    } finally {
      fs.rmSync(resultsDir, { recursive: true, force: true });
    }
  });

  test("filters summaries and run payloads to the gated model set", () => {
    const resultsDir = fs.mkdtempSync(path.join(os.tmpdir(), "belief-dashboard-"));
    const summaryHeader = [
      "model_name",
      "quantity_id",
      "quantity_name",
      "n_successful_runs",
      "pooled_point_estimate",
      "pooled_lower_bound",
      "pooled_upper_bound",
    ].join(",");
    try {
      for (const modelId of ["model-a", "model-b"]) {
        const experimentDir = path.join(
          resultsDir,
          `${modelId}-elasticities-batch15`,
        );
        fs.mkdirSync(experimentDir);
        fs.writeFileSync(
          path.join(experimentDir, "summary.csv"),
          `${summaryHeader}\n${modelId},quantity-a,Quantity A,15,0.5,0.2,0.8\n`,
        );
      }

      const gated = new Set(["model-a"]);
      const summary = loadDashboardSummaryData(resultsDir, gated);

      expect(summary.modelNames).toEqual(["model-a"]);
      expect(summary.stats.modelCount).toBe(1);
      expect(summary.quantities[0].availableModels).toEqual(["model-a"]);
      expect(loadRunPayload("quantity-a", "model-b", resultsDir, gated)).toBeNull();
    } finally {
      fs.rmSync(resultsDir, { recursive: true, force: true });
    }
  });
});
