import Link from "next/link";

import { PageBand, ProvenanceFooter } from "@/components/site-chrome";
import { providerColor } from "@/components/strip-plot";
import { getModelLabel } from "@/lib/model-meta";
import {
  buildModelProfile,
  orderedModelNames,
  slugForModel,
  totalRunCount,
} from "@/lib/site-data";

export function generateMetadata() {
  const modelCount = orderedModelNames().length;
  return {
    title: "Models · AI beliefs · PolicyEngine",
    description: `All ${modelCount} frontier models in the gated panel: organization, elicitation wave, predictive tightness, and cost, with per-model belief profiles.`,
  };
}

export default function ModelsIndex() {
  const modelNames = orderedModelNames();
  const modelCount = modelNames.length;

  return (
    <div>
      <PageBand
        title="Models"
        lede={`Each organization appears at its frontier tier as of its elicitation date, and superseded models stay in the panel — so generation-to-generation shifts are directly observable. Tightness is the model's average 90 percent interval-width rank across the 13 canonical quantities (1 = narrowest of ${modelCount}).`}
      />
      <div className="mx-auto max-w-[1100px] px-5 py-8">
        <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
          {modelNames.map((modelName) => {
            const profile = buildModelProfile(modelName);
            return (
              <Link
                key={modelName}
                href={`/models/${slugForModel(modelName)}`}
                className="rounded-lg border p-4 transition hover:border-[color:var(--ring)]"
                style={{
                  borderColor: "var(--border)",
                  background: "var(--card)",
                }}
              >
                <div className="flex items-center gap-2">
                  <span
                    className="inline-block h-2.5 w-2.5 rounded-full"
                    style={{ background: providerColor(modelName) }}
                  />
                  <span
                    className="text-sm font-semibold"
                    style={{ color: "var(--foreground)" }}
                  >
                    {getModelLabel(modelName)}
                  </span>
                </div>
                <dl
                  className="mt-2.5 grid grid-cols-3 gap-2 text-xs"
                  style={{ color: "var(--muted-foreground)" }}
                >
                  <div>
                    <dt>Organization</dt>
                    <dd style={{ color: "var(--foreground)" }}>
                      {profile.organizationLabel}
                    </dd>
                  </div>
                  <div>
                    <dt>Wave</dt>
                    <dd style={{ color: "var(--foreground)" }}>
                      {profile.waveLabel}
                    </dd>
                  </div>
                  <div>
                    <dt>Tightness</dt>
                    <dd style={{ color: "var(--foreground)" }}>
                      {profile.avgWidthRank !== null
                        ? `#${profile.avgWidthRank.toFixed(1)}`
                        : "—"}
                    </dd>
                  </div>
                </dl>
              </Link>
            );
          })}
        </div>
        <ProvenanceFooter runCount={totalRunCount()} />
      </div>
    </div>
  );
}
