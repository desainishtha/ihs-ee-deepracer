# DeepRacer-for-Cloud Training Report - 30 Minute Run

Date: 2026-04-04
Environment: macOS (Apple Silicon), Docker Desktop, DRfC local mode
Goal: First stable physical-car readiness (safety over speed)

## Run Commands Used

- source /Users/nishthadesai/deepracer-for-cloud/bin/activate.sh
- dr-update
- dr-upload-custom-files
- dr-start-training -w -q
- docker logs -f deepracer-0-rl_coach-1

## Captured Metrics Snapshot

Source file: reports/training/metrics/TrainingMetrics_30min.json

Summary captured at end of run:
- total training rows: 57
- total evaluation rows: 20
- last 40 training: avg completion 10.47, median 8.5, max 39.0, off-track rate 100%
- last 20 evaluation: avg completion 11.55, median 7.0, max 31.0, off-track rate 100%
- best evaluation completion observed: 31.0

## Container and Log Evidence

Raw container log exported to:
- reports/training/logs/30min_algo_container.log

Notable log patterns:
- checkpoints were produced and uploaded
- episodes progressed, but completion remained low
- off-track remained dominant in evaluation episodes

## Practical Go/No-Go Decision (Physical Car)

Decision: NO-GO

Reason:
- Evaluation completion is too low for safe first autonomous physical movement.
- Off-track rate remains 100% in evaluation samples.

## Recommendation After This Run

- Continue training and re-evaluate only after sustained eval completion increases.
- Keep safety-first action space and reward settings; prioritize stability before any speed tuning.
