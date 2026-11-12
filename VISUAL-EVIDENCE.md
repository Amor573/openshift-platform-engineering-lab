# Selected historical evidence

These sanitized captures document related hands-on work, not execution of this repository revision. Exact crops and solid redactions preserve the technical output. No production SLA, high availability or successful data recovery is implied.

## Logging: scheduling failure

Scheduler events show unbound storage, insufficient CPU/memory and control-plane taints. Diagnostic evidence, not a resolved state.

[View sanitized capture](https://github.com/Amor573/Amor573.github.io/blob/main/portfolio-v2/evidence/openshift/logging-scheduling-failure.png)

## Logging: pods running

A later capture shows the listed logging pods Ready and Running after an ingester pod deletion. It does not prove log ingestion, retention or alert delivery.

[View sanitized capture](https://github.com/Amor573/Amor573.github.io/blob/main/portfolio-v2/evidence/openshift/logging-pods-running.png)

## Velero restore result

manual-restore reports Completed, 0 errors and 1 warning. Application data integrity and the warning cause are not established by this capture.

[View sanitized capture](https://github.com/Amor573/Amor573.github.io/blob/main/portfolio-v2/evidence/openshift/velero-restore-completed.png)

