# Lab 01 — Namespace-scoped RBAC

## Goal

Create a ServiceAccount that can **read selected namespaced workloads** but cannot modify RoleBindings, pods, or another user's privileges.

```bash
oc apply -f labs/01-rbac/namespace.yaml
oc apply -f labs/01-rbac/sa.yaml -f labs/01-rbac/role.yaml -f labs/01-rbac/rolebinding.yaml
oc -n platform-lab describe rolebinding lab-reader-binding
```

## Validation (requires impersonation permission)

```bash
oc auth can-i list pods -n platform-lab --as=system:serviceaccount:platform-lab:lab-reader
oc auth can-i get deployments -n platform-lab --as=system:serviceaccount:platform-lab:lab-reader
oc auth can-i create pods -n platform-lab --as=system:serviceaccount:platform-lab:lab-reader
oc auth can-i update rolebindings -n platform-lab --as=system:serviceaccount:platform-lab:lab-reader
oc auth can-i get secrets -n platform-lab --as=system:serviceaccount:platform-lab:lab-reader
```

Expected: `yes`, `yes`, `no`, `no`, `no`. An impersonation error may indicate the *caller* is not allowed to impersonate; it does not by itself establish the ServiceAccount's access.

Kubernetes RBAC is additive. Not granting RoleBinding write privileges here is **not** a global deny rule. To prevent privilege elevation for other identities, inspect their effective RBAC and Kubernetes built-in anti-escalation checks.

Cleanup destroys everything in the disposable namespace: `oc delete namespace platform-lab`. Do not run against a shared project.
