# Data Policy

No participant-level research data are stored in this public repository.

## Principles

Data handling must preserve:

- informed consent and governance;
- privacy and deidentification;
- licensing;
- source provenance;
- reproducibility;
- version stability;
- explicit access restrictions.

## Public datasets

When a public dataset is used, prefer a retrieval script or documented procedure that records:

- authoritative source;
- dataset name;
- version or release date;
- citation;
- license;
- expected file list;
- checksums where practical;
- any preprocessing performed before analysis.

A public URL is not enough if the underlying dataset can change silently.

## Controlled-access datasets

Controlled or clinical datasets should remain in approved storage. The public repository should contain only:

- a data-access statement;
- schema or data dictionary when permitted;
- synthetic or toy examples;
- analysis code that can run after authorized data are placed in the expected location;
- provenance metadata that do not identify participants.

## Sensitive neural and physiological data

Neural and physiological data can be identifying or reveal health and mental-state information. Deidentification must consider more than removal of names.

Do not publish raw participant data merely to satisfy an open-science norm when consent or privacy does not support it.

## Directory convention for future analyses

Recommended local-only layout:

```text
data/
  raw/              # never committed unless explicitly permitted
  external/         # retrieved authoritative datasets
  interim/          # preprocessing outputs
  derived/          # analysis-ready derivatives
  manifests/        # hashes, versions, provenance
```

The `.gitignore` should exclude participant data and local credentials.

## Dataset manifest

Each empirical project should maintain a machine-readable manifest containing at least:

```text
dataset_id
source
version
license
citation
retrieved_at
checksums
participants_expected
sites_expected
access_class
preprocessing_entrypoint
```

## Split integrity

Participant and site identifiers used to define discovery, internal-confirmation, and external-confirmation splits should be stored in versioned manifests without exposing protected identifiers publicly.

The same person must not silently appear in training and confirmatory data.

## Data-quality accounting

For every dataset report:

- number of participants available;
- number included;
- number excluded and reasons;
- failed acquisition rate;
- failed preprocessing rate;
- channel-specific missingness;
- usable trial or duration distribution;
- site-specific quality differences.

Quality failure is an observation about the measurement process, not evidence of absent consciousness.
