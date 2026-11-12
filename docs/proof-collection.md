# OpenShift proof collection checklist

**Important:** A passing GitHub Actions YAML check only means that sample documents parse and contain common Kubernetes identity fields. It does not prove admission on OCP 4.18 or any other cluster, network connectivity, data persistence, backup recovery, or access control.

For each lab you validate in an authorized cluster, record:
- Git commit SHA, test date, OCP version, and an anonymized environment name
- The expected behavior and a reproducible sequence of `oc` commands
- Actual observed results, including failures and how they were resolved
- An independently checkable success condition

Suggested proof captures:
1. `oc -n platform-lab auth can-i get pods --as system:serviceaccount:platform-lab:...` with expected allow/deny.
2. PVC state, mount point and checksum of test-file content after restarting a workload.
3. A deliberately Pending PVC and the event identifying its root cause.
4. Velero/OADP backup and restore `Completed` states plus recovered application data, not status alone.
5. OBC/ODF resources and sanitized object-read proof, without endpoints, credentials, bucket keys or account details.

Before publishing screenshots, redact bearer tokens, kubeconfig, private addresses, internal names, user names, URLs containing credentials and customer data. Name sanitized files by lab and date, for example `02-pvc-resize-verified-YYYY-MM-DD.png`. Do not commit raw terminal recordings with secrets.

Only change `EVIDENCE.md` entries to **Validated** after the real command output has been reviewed.