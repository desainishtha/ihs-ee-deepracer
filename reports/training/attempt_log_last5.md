# DeepRacer Attempt Log (Last 5 Attempts)

## Attempt 1 - Baseline 30-minute run
- Runtime: stable enough to complete run
- Metrics summary: training avg completion ~10.47, eval avg completion ~11.55, best eval completion 31, off-track 100%
- Decision: NO-GO
- Main reason: evaluation consistency was too low and off-track remained dominant.

## Attempt 2 - Extended 60-minute run
- Runtime: unstable due to memory pressure
- Metrics summary: training avg completion ~9.62, eval avg completion ~12.37, best eval completion 23, off-track 100%
- Critical event: OOM (ExitCode 137)
- Decision: NO-GO

## Attempt 3 - Recovery configuration run
- Runtime: startup healthy; training progressed; later failed by OOM
- Metrics summary at evaluation point: train_last20 11.35, eval_last20 22.13, best_eval_completion 23, off-track 100%
- Critical event: OOM (ExitCode 137)
- Decision: NO-GO
- Note: eval average improved, but best completion and reliability remained low.

## Attempt 4 - Headless rendering fix run
- Runtime: render/display issue resolved, containers remained up, no immediate OOM
- Metrics summary: train_last20 8.15, eval_last20 3.80, best_eval_completion 5, off-track 100%
- Decision: FAIL_METRICS
- Note: infrastructure was stable but driving quality regressed.

## Attempt 5 - Conservative action/reward retry
- Runtime: started healthy, evaluation episodes accumulated, later OOM terminated trainer
- Metrics summary at recheck: training episodes 40, evaluation episodes 8, train_last20 9.45, eval_last20 7.00, best_eval_completion 7, off-track 100%
- Critical event: OOM (ExitCode 137, SIGKILL)
- Decision: NO-GO

## Overall pattern across last 5 attempts
- Main blockers were:
  - Off-track rate stuck at 100%
  - Evaluation completion too low and inconsistent
  - Intermittent OOM crashes in longer runs
- Improvement observed in one recovery run (eval_last20 > 20), but not sustained or reliable enough for physical deployment.
