import Link from "next/link";

import { PageBand, ProvenanceFooter } from "@/components/site-chrome";
import { providerColor } from "@/components/strip-plot";
import {
  getModelLabel,
  getProviderForModel,
  PROVIDER_LABELS,
} from "@/lib/model-meta";
import {
  buildModelProfile,
  orderedModelNames,
  slugForModel,
  totalRunCount,
} from "@/lib/site-data";

export const metadata = {
  title: "Models · AI beliefs · PolicyEngine",
  description:
    "All 17 frontier models in the panel: provider, elicitation wave, predictive tightness, and cost, with per-model belief profiles.",
};

export default function ModelsIndex() {
  const modelNames = orderedModelNames();

  return (
    <div>
      <PageBand
        title="Models"
        lede="Each provider appears at its frontier tier as of its elicitation date, and superseded models stay in the panel — so generation-to-generation shifts are directly observable. Tightness is the model's average 90 percent interval-width rank across the 13 canonical quantities (1 = narrowest of 17)."
      />
      <div className="mx-auto max-w-[1100px] px-5 py-8">
        <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
          {modelNames.map((modelName) => {
            const profile = buildModelProfile(modelName);
            const provider = getProviderForModel(modelName);
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
                    <dt>Provider</dt>
                    <dd style={{ color: "var(--foreground)" }}>
                      {provider ? PROVIDER_LABELS[provider] : "—"}
                    </dd>
                  </div>
                  <div>
                    <dt>Wave</dt>
                    <dd style={{ color: "var(--foreground)" }}>
                      {profile.julyWave ? "July 2026" : "April 2026"}
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
