# Schemas

This directory contains machine-readable contracts for the research program.

## `cep.schema.json`

Defines the structure of a Consciousness Evidence Profile. A CEP is a target-specific evidence record, not a clinical diagnosis.

## `claim.schema.json`

Defines the structure of an M0-M7 scientific claim record. It requires explicit assumptions, identifiability status, falsification condition, nonclaims, and result status.

## Schema rules

A schema change that alters scientific meaning must update:

- the corresponding example;
- the relevant documentation;
- tests;
- software data structures when applicable.

Examples are validated in the test suite with JSON Schema Draft 2020-12.
