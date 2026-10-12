# Presenting this OpenShift lab professionally

Describe what you **implemented and verified**, not simply what is listed in a README.

For each lab:
1. Write the infrastructure preconditions (OCP/ODF/OADP versions, CSI capabilities).
2. Run the sample on an authorized disposable cluster.
3. Record relevant redacted output (e.g., pods Running, PVC Bound, access checks, successful restore).
4. Document root cause and how you fixed the first failure.
5. Note rollback and cleanup; only then update EVIDENCE.md.

A completed backup does not establish recovery capability: validate restored application data. Avoid screenshots that expose secrets or cluster details. Never imply client systems have been reproduced here.
