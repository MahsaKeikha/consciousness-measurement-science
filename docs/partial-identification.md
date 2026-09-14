# Dependence-Robust Partial Identification

This document formalizes a conservative multimodal evidence calculation for the case in which each binary evidence channel has calibrated marginal sensitivity and specificity but the conditional dependence among channels is unknown.

The goal is not to produce a better-looking score. The goal is to answer a narrower identification question:

> Given only the calibrated marginal behavior of the observed channels, what range of joint evidence is compatible with all dependence structures that have not been ruled out?

If that range is wide, the scientifically correct conclusion is wide. If it spans the full probability interval, the available marginal calibration does not identify a posterior probability without additional assumptions or data about dependence.

## 1. Setup

Let \(E\) denote a declared binary latent target for a specific validation domain. It need not mean "consciousness" in general. It may represent a narrower target that has an operationally defensible calibration model.

For channel \(i\), let

\[
s_i=P(X_i=1\mid E)
\]

be sensitivity and

\[
c_i=P(X_i=0\mid \neg E)
\]

be specificity.

Suppose the observed value is \(x_i\in\{0,1\}\). Define the marginal probability of that observed sign under the target as

\[
p_i^{(E)}=
\begin{cases}
s_i,&x_i=1,\\1-s_i,&x_i=0,
\end{cases}
\]

and under the non-target condition as

\[
p_i^{(\neg E)}=
\begin{cases}1-c_i,&x_i=1,\\c_i,&x_i=0.
\end{cases}
\]

The ordinary independence calculation assumes

\[
P(X_1=x_1,\ldots,X_K=x_K\mid E)=\prod_i p_i^{(E)}
\]

and the analogous factorization under \(
eg E\). That factorization is not implied by knowing the marginal sensitivities and specificities.

## 2. Sharp Frechet-Hoeffding bounds

For events \(A_1,\ldots,A_K\) with known marginal probabilities \(p_1,\ldots,p_K\) and otherwise unrestricted dependence, the intersection probability satisfies

\[
\max\left(0,\sum_{i=1}^{K}p_i-(K-1)\right)
\le P\left(\bigcap_i A_i\right)
\le \min_i p_i.
\]

These are sharp marginal-only bounds. Therefore the observed multimodal pattern has two conditional intervals:

\[
P(X=x\mid E)\in[L_E,U_E]
\]

and

\[
P(X=x\mid \neg E)\in[L_0,U_0].
\]

No conditional-independence assumption is needed to obtain these intervals.

## 3. Likelihood-ratio identification region

When \(U_0>0\), the compatible likelihood ratios satisfy

\[
LR(x)=\frac{P(X=x\mid E)}{P(X=x\mid \neg E)}
\in
\left[
\frac{L_E}{U_0},
\frac{U_E}{L_0}
\right].
\]

If \(L_0=0\) and \(U_E>0\), the upper likelihood-ratio bound is unbounded:

\[
LR_{\max}=+\infty.
\]

This is not a numerical instability. It says that the marginal information does not rule out a dependence structure under which the observed pattern is arbitrarily more diagnostic than another admissible dependence structure would make it.

If the pattern has zero probability under every admissible non-target distribution, the ordinary likelihood ratio is not identified by this helper and the software raises an error rather than returning an invented finite value.

## 4. Posterior identification region

For a declared prior \(\pi=P(E)\), prior odds are

\[
O_0=\frac{\pi}{1-\pi}.
\]

Because the posterior is monotone in the likelihood ratio, the LR interval maps directly to

\[
P(E\mid X=x)
\in
\left[
\frac{O_0LR_{\min}}{1+O_0LR_{\min}},
\frac{O_0LR_{\max}}{1+O_0LR_{\max}}
\right],
\]

with the limiting value 1 when \(LR_{\max}=+\infty\).

A posterior interval of \([0,1]\) is a valid result. It means the marginal calibration alone does not identify the posterior under unrestricted conditional dependence.

## 5. Worked example

Consider two positive channels:

- channel 1: sensitivity 0.80, specificity 0.90;
- channel 2: sensitivity 0.75, specificity 0.80.

Under \(E\), the observed positive-sign marginals are 0.80 and 0.75, so

\[
P(++\mid E)\in[0.55,0.75].
\]

Under \(
eg E\), the positive-sign marginals are 0.10 and 0.20, so

\[
P(++\mid\neg E)\in[0,0.10].
\]

Therefore

\[
LR(++)\in[5.5,+\infty).
\]

With prior probability 0.25, the posterior lower bound is about 0.647 and the upper bound is 1.

The ordinary conditional-independence calculation produces one value inside this interval. It is not wrong when independence is justified. It is simply more assumption-dependent than the marginal-only identification region.

## 6. Why three or more channels can become completely nonidentifying

Suppose three channels each have sensitivity 0.50 and specificity 0.50 and all three are observed positive. Under either latent condition, each observed-sign marginal is 0.50.

For three events with marginal probability 0.50,

\[
P(+++)\in[0,0.50].
\]

The resulting likelihood-ratio interval is

\[
[0,+\infty),
\]

and every posterior probability in \([0,1]\) is compatible with some admissible dependence structure.

This example is intentionally simple. It makes the identification point explicit: adding channels does not automatically add independent information.

## 7. What this calculation establishes

The current implementation establishes exact marginal-only bounds for the observed binary evidence pattern under unrestricted conditional dependence. It can be used to:

- show whether an independence-based posterior is robust or assumption-sensitive;
- expose when channel marginals alone provide only weak joint evidence;
- identify cases where the posterior is not point identified;
- provide a principled abstention trigger when the identification region is too wide for the intended claim;
- motivate collection of joint calibration data rather than treating more modalities as automatically independent evidence.

## 8. What it does not establish

This calculation does not:

- validate the latent target itself;
- prove that sensitivity or specificity transport to a new state, site, population, or device;
- model uncertainty in estimated sensitivities or specificities;
- use known pairwise correlations, copulas, latent-factor models, or repeated-measures structure;
- solve missing-data or reference-standard error;
- turn a posterior interval into a direct probability of consciousness;
- establish a necessary or sufficient mechanism for experience.

Those are separate layers of the measurement problem.

## 9. Next tightening steps

The marginal-only interval is deliberately the least assumption-intensive baseline. It can be tightened only by adding information that is itself justified and declared. Candidate extensions include:

1. confidence regions for sensitivity and specificity rather than treating calibration values as fixed;
2. empirically estimated pairwise or higher-order dependence constraints;
3. state-specific and site-specific dependence models;
4. latent-variable or copula sensitivity families;
5. missingness bounds;
6. reference-standard uncertainty;
7. transport uncertainty;
8. preregistered decision rules that map interval width to abstention.

Each extension must state which new assumption or new empirical estimate narrows the identification region.

## 10. Software

The implementation is in `src/consciousness_measurement/partial_identification.py`.

Primary functions are:

- `frechet_intersection_bounds(...)`;
- `conditional_pattern_probability_bounds(...)`;
- `likelihood_ratio_bounds(...)`;
- `posterior_interval_from_lr_bounds(...)`;
- `fuse_unknown_dependence(...)`.

The unit tests are in `tests/test_partial_identification.py`.

The software is a research scaffold. It is not a clinical classifier and it is not a consciousness meter.
