import Link from "next/link";

import { PageBand, ProvenanceFooter } from "@/components/site-chrome";
import {
  SUBPANEL_LABELS,
  getSummaryData,
  slugForQuantity,
  subpanelForQuantity,
  totalRunCount,
  type Subpanel,
} from "@/lib/site-data";
import type { QuantitySummary } from "@/lib/dashboard-types";

export const metadata = {
  title: "Quantities · AI beliefs · PolicyEngine",
  description:
    "All 26 elicited economic quantities, grouped by subpanel, with per-model interval charts and run-level detail.",
};

const SUBPANEL_ORDER: Subpanel[] = [
  "labor-tax",
  "macro-trade",
  "calibration",
  "simulation",
];

export default function QuantitiesIndex() {
  const data = getSummaryData();
  const groups = new Map<Subpanel, QuantitySummary[]>();
  for (const quantity of data.quantities) {
    const subpanel = subpanelForQuantity(quantity.quantityId);
    const group = groups.get(subpanel) ?? [];
    group.push(quantity);
    groups.set(subpanel, group);
  }

  return (
    <div>
      <PageBand
        title="Quantities"
        lede="Every elicited quantity, grouped the way the paper analyzes them. Labor-and-tax and macro-and-trade form the headline subpanels; calibration parameters enter the stability checks; simulation-facing coefficients feed PolicyEngine-style microsimulation."
      />
      <div className="mx-auto max-w-[1100px] px-5 py-8">
        {SUBPANEL_ORDER.map((subpanel) => {
          const quantities = groups.get(subpanel);
          if (!quantities || quantities.length === 0) return null;
          return (
            <section key={subpanel} className="mb-8">
              <h2
                className="text-xs font-semibold uppercase tracking-wide"
                style={{ color: "var(--muted-foreground)" }}
              >
                {SUBPANEL_LABELS[subpanel]} · {quantities.length}
              </h2>
              <ul
                className="mt-2 divide-y rounded-lg border"
                style={{
                  borderColor: "var(--border)",
                  background: "var(--card)",
                }}
              >
                {quantities.map((quantity) => (
                  <li key={quantity.quantityId}>
                    <Link
                      href={`/quantities/${slugForQuantity(quantity.quantityId)}`}
                      className="flex items-center justify-between gap-4 px-4 py-3 text-sm transition hover:bg-[color:var(--muted)]"
                      style={{ borderColor: "var(--border)" }}
                    >
                      <span style={{ color: "var(--foreground)" }}>
                        {quantity.quantityName}
                      </span>
                      <span
                        className="shrink-0 font-mono text-xs"
                        style={{ color: "var(--muted-foreground)" }}
                      >
                        {quantity.modelSummaries.length} models
                      </span>
                    </Link>
                  </li>
                ))}
              </ul>
            </section>
          );
        })}
        <ProvenanceFooter runCount={totalRunCount()} />
      </div>
    </div>
  );
}
