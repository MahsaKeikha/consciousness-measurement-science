# Claim Registry

This registry is the repository's guard against overclaiming. Every future empirical conclusion should be entered with a target, evidence tier, assumptions, and explicit non-claims.

| ID | Candidate claim | Target | Minimum ladder level | Required evidence | Explicitly not implied |
|---|---|---|---|---|---|
| C1 | a feature predicts reportable content | content | M1 | held-out prediction + calibration | direct access to qualia |
| C2 | a feature generalizes across sites | declared target | M2 | locked external-site validation | mechanism or necessity |
| C3 | a marker transports across sleep/anesthesia/wake | global state/presence proxy | M3 | multiple manipulations + controls | universal consciousness scalar |
| C4 | perturbing mechanism changes experiential target as predicted | mechanism | M4 | causal manipulation + controls | complete explanation of experience |
| C5 | multimodal model bounds latent target | presence/state | M5 | identified/partially identified latent model + sensitivity analysis | ontology of consciousness |
| C6 | physical geometry predicts phenomenal geometry | structure | M6 | reliable reports + held-out structural prediction + confound controls | physical geometry *is* phenomenology |
| C7 | one theory's unique prediction survives adversarial test | theory comparison | M7 | preregistered divergence + confirmatory data | final theory of consciousness |

## Claim record template

```yaml
claim_id: Cx
target: presence|state|content|structure|capacity
statement: "..."
claim_level: M0-M7
population: "..."
contexts: ["..."]
evidence:
  datasets: ["..."]
  analyses: ["..."]
assumptions: ["..."]
identifiability: point|interval|partial|not_identified
external_validation: yes|no
falsification_condition: "..."
nonclaims: ["..."]
status: proposed|preregistered|supported|failed|inconclusive
```

Machine-readable claim records should eventually live under `claims/` and be validated in CI.
