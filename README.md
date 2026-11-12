# OpenShift Platform Engineering Lab

A non-production lab portfolio for **OpenShift operations, RBAC, persistent storage, ODF, CSI troubleshooting, and OADP/Velero backup and recovery**.

The labs are deliberately documented as **exercises awaiting environment-specific validation**, not proof of a production deployment. As you run them, capture sanitized command outputs in [EVIDENCE.md](EVIDENCE.md).

## Labs

| Lab | What you will practice |
| --- | --- |
| [01 — Namespace RBAC](labs/01-rbac/README.md) | Role, RoleBinding, ServiceAccount and least-privilege verification |
| [02 — Persistent storage](labs/02-persistent-storage/README.md) | PVC, filesystem-mode RBD, mount paths, data persistence and resize |
| [03 — Storage troubleshooting](labs/03-troubleshooting/README.md) | Pending claims, CrashLoopBackOff, mount errors, RWO multi-attach |
| [04 — OADP and Velero](labs/04-oadp/README.md) | CSI snapshot-backed backup, restore mapping and TTL |
| [05 — ODF platform services](labs/05-odf-services/README.md) | OBC, NooBaa, registry integration planning and ODF capacity |

## Lab safety

- **Only apply to a cluster you own or have permission to administer.** Prefer a disposable OpenShift project.
- Verify identity and target first: `oc whoami`, `oc project`, `oc get sc`.
- Never commit credentials, kubeconfig, snapshot secrets, bucket endpoints, internal IP addresses or real enterprise data.
- A PVC mounted at `/data` stores writes made to `/data` **inside the container**. It does not copy files from an arbitrary path on a worker node.
- OADP restore success must be verified by examining the recovered application and data.

## Begin with RBAC

```bash
oc whoami
oc get sc
oc apply -f labs/01-rbac/namespace.yaml
oc apply -f labs/01-rbac/sa.yaml -f labs/01-rbac/role.yaml -f labs/01-rbac/rolebinding.yaml
oc -n platform-lab get roles,rolebindings,serviceaccounts
```

Then proceed to [Lab 02](labs/02-persistent-storage/README.md). Use [EVIDENCE.md](EVIDENCE.md) to document what actually worked and what required correction.

## Goals

Build repeatable OpenShift operating procedures for storage, backups, authorization and troubleshooting. Add real-world evidence only after lab validation. See [portfolio notes](docs/portfolio-notes.md).

**Skills:** Red Hat OpenShift · Kubernetes · ODF/Ceph RBD · OADP/Velero · RBAC · Linux · CSI · Troubleshooting.

## Automated checks and evidence

[![Validate lab YAML structure](https://github.com/Amor573/openshift-platform-engineering-lab/actions/workflows/yaml-check.yml/badge.svg)](https://github.com/Amor573/openshift-platform-engineering-lab/actions/workflows/yaml-check.yml)

A lightweight CI job now parses every lab YAML resource and checks that common identity fields exist. **This is not an OpenShift deployment test.** Follow the [proof-collection checklist](docs/proof-collection.md) and record only validated cluster outcomes in [EVIDENCE.md](EVIDENCE.md).
