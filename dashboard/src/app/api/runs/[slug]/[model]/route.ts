import { NextResponse } from "next/server";

import {
  getModelNameBySlug,
  getQuantityBySlug,
  getSummaryData,
  loadRunPayloadForSite,
  slugForModel,
  slugForQuantity,
} from "@/lib/site-data";

/** Per-cell raw runs as prerendered JSON — the archived parsed responses
 *  behind each strip-plot row, served by the site itself (the runs.jsonl
 *  files are too large for GitHub's inline blob view). The shared prompt
 *  is hoisted to one top-level field instead of repeating per run. */
export const dynamic = "force-static";

export function generateStaticParams() {
  return getSummaryData().quantities.flatMap((quantity) =>
    quantity.modelSummaries.map((summary) => ({
      slug: slugForQuantity(quantity.quantityId),
      model: slugForModel(summary.modelName),
    })),
  );
}

export async function GET(
  _request: Request,
  { params }: { params: Promise<{ slug: string; model: string }> },
) {
  const { slug, model } = await params;
  const quantity = getQuantityBySlug(slug);
  const modelName = getModelNameBySlug(model);
  if (!quantity || !modelName) {
    return NextResponse.json(
      { error: "unknown quantity or model" },
      { status: 404 },
    );
  }
  const payload = loadRunPayloadForSite(quantity.quantityId, modelName);
  if (!payload) {
    return NextResponse.json({ error: "no archived runs" }, { status: 404 });
  }
  const prompt = payload.runs.find((run) => run.prompt)?.prompt ?? null;
  return NextResponse.json({
    ...payload,
    prompt,
    // Drop the per-run prompt copies; JSON serialization omits undefined.
    runs: payload.runs.map((run) => ({ ...run, prompt: undefined })),
  });
}
