# Attempt 3 Recovery Run Report

## Runtime
- Startup and early training were stable.
- Later terminated by memory pressure.

## Metrics at evaluation snapshot
- train_last20 avg completion: 11.35
- eval_last20 avg completion: 22.13
- best_eval_completion: 23
- off-track rate: 100%

## Decision
- NO-GO

## Reason
- Some evaluation improvement was observed, but best completion remained below practical target and run reliability was broken by OOM (ExitCode 137).
