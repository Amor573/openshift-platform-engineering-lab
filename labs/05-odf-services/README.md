# Lab 05 — ODF services, object storage and capacity

This is a **planning and verification guide**, not a claim that the OpenShift image registry has been changed.

## Preflight

```bash
oc get sc
oc get storagecluster -A
oc -n openshift-storage get pods
oc get objectbucketclaims -A
oc -n openshift-image-registry get configs.imageregistry.operator.openshift.io cluster -o yaml
```

## ObjectBucketClaim workflow

1. Identify the NooBaa ObjectBucketClaim StorageClass actually installed on your cluster (often `openshift-storage.noobaa.io`).
2. Apply an authorized OBC using the correct provisioner, bucket naming policy and approved project.
3. Verify the OBC becomes `Bound` and that generated ConfigMap/Secret objects exist without printing their secret values.
4. Record registry operator configuration **before** any changes, confirm OCP/ODF version-specific support, and prepare a rollback plan.
5. During an approved maintenance window, validate registry operator health and image push/pull after changes.

## Capacity and service health

Ceph RBD and CephFS capacity depend on Ceph health, replication, backing devices and available pool storage; PVC requests alone don't measure remaining usable space.

```bash
oc -n openshift-storage get cephcluster
oc -n openshift-storage get storagecluster
oc -n openshift-storage get pods
```

Changing the image registry can interrupt platform services. Do **not** make these edits as an unreviewed lab exercise on a shared cluster.
