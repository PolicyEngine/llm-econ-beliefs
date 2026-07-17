/** Standard-notation formulas for each elicited quantity.
 *
 *  Editorial shorthand for display only: the models received the prose
 *  definition from the elicitation prompt (shown beside the formula),
 *  never the formula itself. Strings are trusted local constants
 *  rendered with dangerouslySetInnerHTML; keep them to em/sub/sup
 *  markup only. */

const POLICY_RESPONSE_FORMULA =
  "Δ ln <em>h</em> = <em>ε</em> · Δ ln <em>w</em><sub>net</sub><sup>marginal</sup> (bounded relative change)";

export const QUANTITY_FORMULAS: Record<string, string> = {
  "labor_supply.income_elasticity.prime_age":
    "<em>ε</em> = ∂ ln <em>h</em> / ∂ ln <em>y</em><sub>non-labor</sub>, holding <em>w</em><sub>net</sub> fixed",
  "labor_supply.frisch_elasticity.prime_age":
    "<em>ε</em><sup>F</sup> = ∂ ln <em>h</em> / ∂ ln <em>w</em><sub>net</sub>, holding marginal utility of wealth <em>λ</em> constant",
  "labor_supply.marshallian_wage_elasticity.prime_age":
    "<em>ε</em><sup>M</sup> = ∂ ln <em>h</em> / ∂ ln <em>w</em><sub>net</sub> (uncompensated: substitution + income effects)",
  "labor_supply.extensive_margin.single_mothers":
    "<em>ε</em> = ∂ ln Pr(employed) / ∂ ln <em>w</em><sub>net</sub>",
  "household.relative_risk_aversion.crra":
    "<em>γ</em> = −<em>c</em> · <em>u</em>″(<em>c</em>) / <em>u</em>′(<em>c</em>)",
  "household.intertemporal_elasticity_of_substitution":
    "<em>σ</em> = ∂ ln(<em>c</em><sub>t+1</sub>/<em>c</em><sub>t</sub>) / ∂ ln(1+<em>r</em>)",
  "household.annual_discount_factor":
    "<em>β</em> in <em>U</em> = Σ<sub>t</sub> <em>β</em><sup>t</sup> <em>u</em>(<em>c</em><sub>t</sub>)",
  "production.capital_labor_substitution":
    "<em>σ</em><sub>KL</sub> = ∂ ln(<em>K</em>/<em>L</em>) / ∂ ln MRTS<sub>KL</sub> (CES)",
  "production.capital_share":
    "<em>α</em> = ∂ ln <em>Y</em> / ∂ ln <em>K</em>",
  "trade.armington_elasticity.import_domestic":
    "<em>σ</em><sub>A</sub> = ∂ ln(<em>M</em>/<em>D</em>) / ∂ ln(<em>p</em><sub>D</sub>/<em>p</em><sub>M</sub>)",
  "tax.elasticity_of_taxable_income.top_earners":
    "<em>e</em> = ∂ ln <em>z</em> / ∂ ln(1−<em>τ</em>)",
  "tax.capital_gains_realizations.elasticity":
    "<em>ε</em><sub>τ</sub> = ∂ ln <em>R</em> / ∂ ln <em>τ</em>",
  "tax.capital_gains_realizations.elasticity.net_of_tax_rate":
    "<em>ε</em><sub>1−τ</sub> = ∂ ln <em>R</em> / ∂ ln(1−<em>τ</em>)",
  "macro.tfp_persistence.ar1":
    "<em>ρ</em> in ln <em>A</em><sub>t</sub> = <em>ρ</em> ln <em>A</em><sub>t−1</sub> + <em>ε</em><sub>t</sub>",
  "labor_supply.policy_response.substitution_elasticity.all": POLICY_RESPONSE_FORMULA,
  "labor_supply.policy_response.substitution_elasticity.secondary": POLICY_RESPONSE_FORMULA,
  ...Object.fromEntries(
    Array.from({ length: 10 }, (_, index) => [
      `labor_supply.policy_response.substitution_elasticity.primary.decile_${index + 1}`,
      POLICY_RESPONSE_FORMULA,
    ]),
  ),
};
