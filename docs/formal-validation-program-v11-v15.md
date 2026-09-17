# Research III Formal Validation V11-V15

## Identification limits and release-safe measurement design

V11-V15 extend the Research III validation program from robustness diagnosis to explicit experimental-design laws. The central question is no longer only whether a latent quantity can be inverted from an imperfect proxy. It is whether a planned measurement design has enough information to support the desired resolution, whether site pooling preserves the target quantity, and whether a release decision can be made without invalidating the inferential guarantee.

These are analytic and synthetic measurement-science results. They do not establish that any biological, behavioral, neural, physiological, perturbational, or artificial-system proxy is calibrated for consciousness.

---

## Notation

Let the declared binary latent target be \(Z\in\{0,1\}\), with prevalence

\[
\pi=P(Z=1).
\]

Let the observed binary proxy be \(Y\in\{0,1\}\), with sensitivity \(\alpha\), specificity \(\beta\), positive proxy rate \(q\), and Youden information margin

\[
J=\alpha+\beta-1.
\]

Whenever \(J>0\),

\[
q=(1-\beta)+J\pi,
\qquad
\pi=\frac{q+\beta-1}{J}.
\]

For a multisite design, site \(i\) has weight \(w_i>0\), \(\sum_i w_i=1\), site prevalence \(\pi_i\), calibration \((\alpha_i,\beta_i)\), and information margin \(J_i=\alpha_i+\beta_i-1\).

---

# V11. Exact missingness-resolution law under known calibration

Suppose \(N\) measurements were intended, \(n_o\) outcomes are observed, and \(s_o\) of those observed outcomes are positive. With no assumption on the missing outcomes, the sharp observable-rate set is

\[
q\in
\left[
\frac{s_o}{N},
\frac{s_o+N-n_o}{N}
\right].
\]

This is sharp because the lower endpoint is attained by assigning every missing outcome zero and the upper endpoint by assigning every missing outcome one.

If calibration is point-known and \(J>0\), the inverse \(q\mapsto\pi\) is strictly increasing. Therefore the sharp latent identified set is obtained by intersecting the proxy interval with the physically compatible proxy range \([1-\beta,\alpha]\), then applying the inverse to both endpoints.

### Proposition V11

Let \(m=N-n_o\) denote the number of missing outcomes. If both sharp proxy endpoints correspond to interior latent prevalences, then the exact latent identified-set width is

\[
\boxed{
W_{\mathrm{miss}}=\frac{m/N}{J}
}
\]

where \(J=\alpha+\beta-1\).

### Proof

The sharp proxy interval has width

\[
\frac{s_o+m}{N}-\frac{s_o}{N}=\frac{m}{N}.
\]

For fixed calibration,

\[
\pi(q)=\frac{q+\beta-1}{J}
\]

is affine with slope \(1/J\). Therefore, before clipping at the parameter-space boundaries,

\[
W_{\mathrm{miss}}
=\frac{1}{J}\frac{m}{N}.
\]

Sharpness follows because both proxy endpoints are attainable under unrestricted missing outcomes and the inverse is one-to-one when \(J>0\). If an endpoint maps outside \([0,1]\), clipping can only reduce the width. \(\square\)

### Engineering interpretation

Missingness and channel weakness multiply rather than add. Ten percent arbitrary missingness produces latent uncertainty width \(0.10/J\) in the interior. A channel with \(J=0.8\) converts that to width 0.125; a channel with \(J=0.4\) converts it to width 0.25.

---

# V12. Necessary and sufficient condition for pooled multisite identification

For \(K\) sites, the pooled positive proxy rate is

\[
\bar q
=
\sum_{i=1}^K w_i(1-\beta_i)
+
\sum_{i=1}^K w_iJ_i\pi_i.
\]

The population-weighted latent target is

\[
\bar\pi=\sum_{i=1}^K w_i\pi_i.
\]

The pooled observable identifies a weighted sum with coefficients \(w_iJ_i\), whereas the scientific target uses coefficients \(w_i\).

### Theorem V12

Assume all \(w_i>0\) and all \(J_i>0\). One pooled proxy rate \(\bar q\), together with known site calibrations and weights, identifies \(\bar\pi\) for every feasible site-prevalence vector if and only if

\[
\boxed{J_1=J_2=\cdots=J_K.}
\]

### Proof: sufficiency

If every \(J_i=J\), then

\[
\bar q
=
\sum_i w_i(1-\beta_i)+J\sum_i w_i\pi_i,
\]

so

\[
\boxed{
\bar\pi
=
\frac{\bar q-\sum_iw_i(1-\beta_i)}{J}.
}
\]

Hence the target average is point-identified.

### Proof: necessity

Suppose there exist sites \(i\neq j\) with \(J_i\neq J_j\). Choose an interior feasible prevalence vector. For sufficiently small \(t\), perturb only those two sites by

\[
\Delta\pi_i=t,
\qquad
\Delta\pi_j=-\frac{w_iJ_i}{w_jJ_j}t.
\]

The pooled observable is unchanged because

\[
w_iJ_i\Delta\pi_i+w_jJ_j\Delta\pi_j=0.
\]

But the target average changes by

\[
\Delta\bar\pi
=w_it+w_j\Delta\pi_j
=w_it\left(1-\frac{J_i}{J_j}\right),
\]

which is nonzero when \(J_i\neq J_j\). Thus the same pooled observable corresponds to different values of \(\bar\pi\), so the target is not point-identified. \(\square\)

### Engineering interpretation

Equal sensitivity and specificity are not required across sites. What pooled identification requires is equality of the net information slope \(J_i\). Site-specific false-positive intercepts may differ if they are known and accounted for.

---

# V13. Sharp K-site partial identification

When the V12 condition fails, the pooled observation still defines a sharp identified set.

Let

\[
r
=
\bar q-
\sum_iw_i(1-\beta_i).
\]

Then feasible prevalences satisfy

\[
\sum_iw_iJ_i\pi_i=r,
\qquad
0\leq\pi_i\leq1.
\]

We seek extrema of

\[
\bar\pi=\sum_iw_i\pi_i.
\]

### Theorem V13

The sharp lower endpoint of \(\bar\pi\) is obtained by assigning prevalence first to sites with the **largest** \(J_i\). The sharp upper endpoint is obtained by assigning prevalence first to sites with the **smallest** \(J_i\), using at most one fractional site after the preceding sites reach \(\pi_i=1\).

### Proof

Define \(x_i=w_iJ_i\pi_i\). Then

\[
0\leq x_i\leq w_iJ_i,
\qquad
\sum_i x_i=r,
\]

while

\[
\bar\pi
=
\sum_i\frac{x_i}{J_i}.
\]

This is the continuous fractional-knapsack problem with value per unit constraint mass equal to \(1/J_i\). To maximize the target, allocate constraint mass to the largest value ratios, equivalently the smallest \(J_i\). To minimize it, allocate to the smallest value ratios, equivalently the largest \(J_i\). The greedy solution is optimal for a one-constraint linear program and is feasible at an extreme point with at most one fractional coordinate. Because every such allocation corresponds to a valid \(\pi_i=x_i/(w_iJ_i)\), both endpoints are attainable. \(\square\)

### Consequence

The two-site result already used in V9 is the \(K=2\) special case. V13 generalizes the same identification geometry to arbitrary known multisite mixtures without numerical optimization.

---

# V14. Finite-sample resolution design law

Assume point-known positive calibration and \(n\) independent deployment observations. A two-sided Hoeffding interval for \(q\) has half-width

\[
\epsilon_n(\delta)
=
\sqrt{\frac{\log(2/\delta)}{2n}}.
\]

The proxy interval therefore has width at most \(2\epsilon_n(\delta)\). Because the inverse slope is exactly \(1/J\), the corresponding latent interval has width at most

\[
W_n
\leq
\frac{2\epsilon_n(\delta)}{J}.
\]

### Proposition V14

To guarantee latent interval width no larger than a predeclared \(\omega>0\) with Hoeffding coverage at least \(1-\delta\), it is sufficient that

\[
\boxed{
 n
\geq
\frac{2\log(2/\delta)}{J^2\omega^2}.
}
\]

The smallest integer satisfying this inequality is used by the executable design function.

### Proof

Require

\[
\frac{2}{J}
\sqrt{\frac{\log(2/\delta)}{2n}}
\leq\omega.
\]

Squaring and rearranging gives the stated result. Clipping the interval at \([0,1]\) can only reduce its width. \(\square\)

### Engineering interpretation

The sample-size penalty is quadratic in inverse channel strength and inverse target resolution:

\[
n=O(J^{-2}\omega^{-2}).
\]

Halving \(J\) multiplies the sufficient sample size by four. Halving the desired interval width also multiplies it by four.

---

# V15. Selection-safe release through independent pilot gating

V10 established that a data-dependent resolution gate does not automatically preserve nominal conditional coverage among released intervals. V15 provides a simple design that does.

Split the experiment into two independent information sets:

1. **pilot data** used only to decide whether the planned confirmatory design is expected to meet a predeclared release criterion;
2. **confirmatory data** used only to construct the final interval.

Let \(G\) be the release event determined from pilot data. Let \(C\) be the event that the confirmatory interval covers the true parameter. Suppose

\[
P(C)\geq1-\delta
\]

and the pilot and confirmatory data are independent.

### Theorem V15

If \(P(G)>0\), then

\[
\boxed{
P(C\mid G)=P(C)\geq1-\delta.
}
\]

### Proof

The event \(G\) is measurable with respect to pilot data, while \(C\) is measurable with respect to independent confirmatory data. Hence \(C\) and \(G\) are independent:

\[
P(C\cap G)=P(C)P(G).
\]

Dividing by \(P(G)>0\) yields

\[
P(C\mid G)=P(C).
\]

Thus the confirmatory coverage guarantee is preserved among released cases. \(\square\)

### Important limitation

This theorem does **not** apply when the final confirmatory interval itself determines whether it is released, or when pilot observations leak into the confirmatory interval construction. Those designs require separate selective-inference arguments or direct conditional-coverage analysis.

---

# Reproducibility map

| Stage | Result | Executable source | Test target |
|---|---|---|---|
| V11 | exact missingness-resolution law | `identification_design.py` | sharp endpoints and width identity |
| V12 | pooled identification iff equal Youden margins | `identification_design.py` | equal-margin recovery and unequal-margin failure |
| V13 | sharp K-site identified interval | `identification_design.py` | agreement with V9 and three-site exact solution |
| V14 | finite-sample resolution/sample-size law | `identification_design.py` | minimal sufficient integer and quadratic scaling |
| V15 | independent pilot gate preserves confirmatory conditional coverage | `identification_design.py` | theorem contract plus fixed-seed pilot/confirmatory experiment |

The companion deterministic experiments are implemented in `identification_design_simulations.py` and use canonical seed `20260919` for stochastic checks.

---

# Scientific boundary

V11-V15 establish properties of an abstract imperfect-proxy measurement problem. They show how missingness, calibration strength, site heterogeneity, finite sample size, and release design constrain what can be inferred. They do not supply the empirical calibration that would be required to claim that a particular proxy measures consciousness, and they do not establish any ontology of consciousness.
