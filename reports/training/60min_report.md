# DeepRacer-for-Cloud Training Report - 60 Minute Attempt

Date: 2026-04-04
Environment: macOS (Apple Silicon), Docker Desktop, DRfC local mode
Goal: Extended run to assess first physical-car readiness

## Run Commands Used

- source /Users/nishthadesai/deepracer-for-cloud/bin/activate.sh
- dr-update
- dr-stop-training || true
- dr-upload-custom-files
- dr-start-training -w -q
- docker logs -f deepracer-0-rl_coach-1

## Captured Metrics Snapshot

Source file: reports/training/metrics/TrainingMetrics_60min_attempt.json

Summary captured from this attempt:
- training rows: 60
- evaluation rows: 19
- training (all): avg completion 9.62, median 8.0, max 30.0, off-track rate 100%
- evaluation (all): avg completion 12.37, median 8.0, max 23.0, off-track rate 100%
- best evaluation completion observed: 23.0

## Runtime Incident

Run terminated by out-of-memory condition:
- ExitCode 137
- ExtraInfo: OutOfMemory: Process killed by SIGKILL (signal 9)

Raw container log exported to:
- reports/training/logs/60min_algo_container.log

## Practical Go/No-Go Decision (Physical Car)

Decision: NO-GO

Reason:
- Evaluation stability remained too low.
- Off-track rate remained 100%.
- Run ended due to memory pressure, reducing reliability of longer-run convergence.

## Recommendation After This Attempt

- Use lower-memory hyperparameters before next long run (for example lower batch_size).
- Re-run and require materially higher evaluation completion before physical testing.
