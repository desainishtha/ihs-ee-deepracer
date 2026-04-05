# Attempt 4 Headless-Fix Run Report

## Runtime
- Display/render crash signatures were resolved.
- Containers remained up during evaluation window.
- No immediate OOM signature in that run window.

## Metrics at evaluation snapshot
- train_last20 avg completion: 8.15
- eval_last20 avg completion: 3.80
- best_eval_completion: 5
- off-track rate: 100%

## Decision
- FAIL_METRICS

## Reason
- Runtime stability improved, but lane-following quality regressed significantly.
