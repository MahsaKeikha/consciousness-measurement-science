# Cross-Site Replication Inference and Stability

## Research III V46-V50

V41-V45 established search-wide error control, exact finite randomization under a declared symmetry null, the failure of naive same-data post-selection intervals, and the value of independent confirmation.

V46-V50 address the next question:

> Once a candidate electromagnetic result has been defined and confirmed, what does it mean for that result to be stable across sites rather than being carried by one unusually precise or influential dataset?

The present layer is deliberately limited. The "sites" below are analytic or synthetic study units with declared estimates and standard errors. They are not real laboratories, cohorts, EEG systems, MEG systems, participants, or clinical centers. These results validate replication-inference machinery. They do not provide external empirical replication of a consciousness marker.

---

## V46. Inverse-variance common-effect pooling

Suppose site (i) reports estimate

[
widehat	heta_i
]

with known standard error

[
s_i>0.
]

Under the declared common-effect model,

[
widehat	heta_i
=
	heta+epsilon_i,
qquad
epsilon_isimmathcal N(0,s_i^2),
]

with independent site errors.

Define inverse-variance weights

[
w_i=rac{1}{s_i^2},
qquad
W=sum_{i=1}^{K}w_i.
]

The minimum-variance linear unbiased common-effect estimate is

[
oxed{
widehat	heta_{mathrm{FE}}
=
rac{sum_i w_iwidehat	heta_i}{W}
}
]

with known-variance standard error

[
oxed{
operatorname{SE}(widehat	heta_{mathrm{FE}})
=
rac{1}{sqrt{W}}.
}
]

### Canonical V46 construction

The declared synthetic site estimates are

[
(0.42, 0.55, 0.37, 0.48)
]

with standard errors

[
(0.12, 0.18, 0.10, 0.15).
]

They give

[
widehat	heta_{mathrm{FE}}
=
0.4268600252
]

and

[
operatorname{SE}
=
0.0639198742.
]

This is a known-variance common-effect calculation. It does not assert that a common effect is scientifically appropriate for real multisite data.

---

## V47. Known-variance heterogeneity statistic

The common-effect residual statistic is

[
oxed{
Q
=
sum_{i=1}^{K}
w_i
(widehat	heta_i-widehat	heta_{mathrm{FE}})^2.
}
]

Under the declared independent Gaussian common-effect model with known variances,

[
Qsimchi^2_{K-1}.
]

Therefore

[
mathbb E[Q]=K-1
]

and

[
operatorname{Var}(Q)=2(K-1).
]

### Canonical V47 check

For the four-site V46 construction,

[
Q_{mathrm{obs}}
=
0.9200868712,
qquad
K-1=3.
]

A fixed-seed simulation with 50,000 common-effect datasets gives

[
overline Q_{mathrm{sim}}
=
3.0115441662
]

against theoretical mean

[
3,
]

and simulated variance

[
6.0378717168
]

against theoretical variance

[
6.
]

The simulation verifies the implementation against the known moment law. It is not a power study for realistic cross-site heterogeneity.

---

## V48. Exact leave-one-site-out influence identity

A pooled result can look stable while being carried by one site. V48 makes the delete-one effect explicit.

Let

[
widehat	heta_{mathrm{FE}}
=
rac{sum_j w_jwidehat	heta_j}{W}.
]

After deleting site (i),

[
widehat	heta_{(-i)}
=
rac{
Wwidehat	heta_{mathrm{FE}}
-
w_iwidehat	heta_i
}{
W-w_i
}.
]

Subtracting the full pooled estimate gives the exact identity

[
oxed{
widehat	heta_{(-i)}
-
widehat	heta_{mathrm{FE}}
=
rac{
w_i
(widehat	heta_{mathrm{FE}}-widehat	heta_i)
}{
W-w_i
}.
}
]

This separates two sources of influence: how far a site's estimate lies from the pooled estimate and how much inverse-variance weight that site carries.

### Canonical V48 shifts

Deleting the four declared sites changes the pooled estimate by approximately

[
(+0.00272, -0.01777, +0.03928, -0.01179).
]

The implementation computes the leave-one-out estimate directly and through the closed-form identity. They agree to floating-point precision.

A small delete-one shift is evidence of stability only for the declared pooling model. It does not exclude shared bias across all sites.

---

## V49. Partial-conjunction replicability inference

A pooled p-value can be driven by evidence from only one site. Replicability requires a stronger question:

> Is there evidence that at least (r) sites carry a non-null effect?

Let

[
p_{(1)}
le
p_{(2)}
le
cdots
le
p_{(K)}
]

be ordered valid site-level p-values.

For the partial-conjunction null that fewer than (r) sites are non-null, a Bonferroni construction is

[
oxed{
p_{mathrm{PC}}^{(r)}
=
min
left[
1,
(K-r+1)p_{(r)}
ight].
}
]

The construction is valid by Bonferroni reasoning under arbitrary dependence among the site-level p-values, provided the individual p-values are valid for their declared site-level nulls.

### Canonical V49 sequence

For

[
(0.001, 0.012, 0.04, 0.21, 0.45),
]

the partial-conjunction p-values are

[
(0.005, 0.048, 0.12, 0.42, 0.45)
]

for required non-null counts

[
r=1,ldots,5.
]

At alpha (0.05), the canonical construction supports the statement "at least two non-null sites" under the declared p-value assumptions, but not "at least three."

That conclusion concerns replicability of a statistical effect. It does not identify what the effect means experientially.

---

## V50. Site-weight concentration and effective replication count

Four nominal sites do not necessarily provide four independent units of evidential weight.

Normalize the inverse-variance weights:

[
a_i=rac{w_i}{W},
qquad
sum_i a_i=1.
]

Define the Kish-style effective site count

[
oxed{
K_{mathrm{eff}}
=
rac{1}{
sum_i a_i^2
}.
}
]

This equals (K) under equal weights and approaches one as one site dominates.

The common-effect variance is

[
operatorname{Var}(widehat	heta_{mathrm{FE}})
=
rac{1}{W}.
]

After deleting site (i),

[
operatorname{Var}(widehat	heta_{(-i)})
=
rac{1}{W-w_i}.
]

The exact variance-inflation factor is therefore

[
oxed{
rac{
operatorname{Var}(widehat	heta_{(-i)})
}{
operatorname{Var}(widehat	heta_{mathrm{FE}})
}
=
rac{1}{1-a_i}.
}
]

### Canonical V50 comparison

For four equal standard errors,

[
K_{mathrm{eff}}=4
]

and the largest delete-one variance inflation is

[
rac{4}{3}.
]

For standard errors

[
(0.05, 0.20, 0.20, 0.20),
]

the most precise site carries normalized weight

[
rac{16}{19}
approx
0.8421,
]

so

[
K_{mathrm{eff}}
approx
1.3938
]

and deleting that site inflates variance by

[
rac{19}{3}
approx
6.3333.
]

A multisite result can therefore have a nominal site count much larger than its effective evidential count.

---

## Combined replication-inference chain

V46-V50 form a compact stability audit:

[
	ext{pool declared site estimates}
ightarrow
	ext{check common-effect residual heterogeneity}
ightarrow
	ext{delete each site}
ightarrow
	ext{test effect replicability across sites}
ightarrow
	ext{measure weight concentration}.
]

The chain keeps several distinctions explicit:

[
	ext{pooled significance}

eq
	ext{cross-site replicability},
]

[
	ext{nominal site count}

eq
	ext{effective site count},
]

[
	ext{leave-one-site-out stability}

eq
	ext{absence of shared bias},
]

and

[
	ext{replicated physical association}

eq
	ext{measurement of consciousness}.
]

---

## What V46-V50 establish

Within the declared analytic and fixed-seed synthetic model:

1. inverse-variance common-effect pooling reproduces the exact known-variance estimator and standard error;
2. the known-variance (Q) statistic has the declared chi-square moment law under an independent Gaussian common effect;
3. the leave-one-site-out shift satisfies an exact closed-form identity;
4. Bonferroni partial-conjunction p-values quantify how many site-level non-null effects are supported under the declared validity assumptions;
5. normalized inverse-variance weights determine an effective site count and exact delete-one variance-inflation factor.

## What V46-V50 do not establish

They do not establish:

- external replication in real participants, cohorts, laboratories, scanners, EEG systems, or MEG systems;
- that a common-effect model is correct for real electromagnetic studies;
- that between-site heterogeneity is absent because one synthetic (Q) value is small;
- that site-level p-values in a future study will satisfy the assumptions used here;
- that a replicated electromagnetic association is specific to consciousness;
- that any electromagnetic field observable is identical to experience or qualia;
- clinical validity, diagnostic utility, or a universal consciousness threshold.

Real replication requires independent datasets, independently implemented acquisition and preprocessing where feasible, transparent site-level estimates, protocol harmonization without hiding heterogeneity, and target-specific human validation.

---

## Reproduce

Run

```bash
python scripts/run_electromagnetic_replication_validation.py
```

The runner writes:

- `results/v46_common_effect_pooling.csv`
- `results/v47_common_effect_heterogeneity.csv`
- `results/v48_leave_one_site_out.csv`
- `results/v49_partial_conjunction_replicability.csv`
- `results/v50_site_weight_concentration.csv`
- `results/electromagnetic_replication_validation_summary.json`
- `docs/figures/v46_v50_electromagnetic_replication_validation.svg`

V46, V48, V49, and V50 are analytic or deterministic. V47 uses seed `20260918` with 50,000 Gaussian common-effect simulations.

The machine-readable CSV and JSON records are the numerical source of truth. The SVG is a generated visual summary.
