# Claims

This directory is reserved for stable machine-readable research claim records.

A future empirical claim file should:

- validate against `../schemas/claim.schema.json`;
- use a stable `claim_id`;
- name the measurement target;
- state the M0-M7 level;
- link to datasets and analyses through repository-specific identifiers;
- list assumption IDs from `../docs/assumption-registry.md`;
- state identifiability and external-validation status;
- state a falsification condition;
- list explicit nonclaims;
- remain in the repository if it fails or becomes inconclusive.

Do not add machine-generated claims that have not been reviewed against the Claim Registry.
