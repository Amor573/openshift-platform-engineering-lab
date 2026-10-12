# Lab 04 — OADP/Velero backup and restore

**Preconditions:** OADP Operator deployed, Velero available, BackupStorageLocation configured, and appropriate CSI snapshot or data-mover capabilities. **Do not run on production data.**

## Confirm readiness

```bash
oc get csv -A | grep -i oadp
oc get dataprotectionapplications -A
oc get backupstoragelocations -A
oc get volumesnapshotclasses
oc -n openshift-adp get pods
```

## Back up a disposable namespace

```bash
velero backup create platform-storage-demo \
  --include-namespaces platform-storage-lab \
  --snapshot-volumes \
  --wait
velero backup describe platform-storage-demo --details
velero backup logs platform-storage-demo
```

A completed Velero backup object **does not prove** recoverable application data. Inspect warnings, snapshots, storage location and backups.

## Restore to a different test namespace

```bash
velero restore create platform-storage-demo-restore \
  --from-backup platform-storage-demo \
  --namespace-mappings platform-storage-lab:platform-storage-restore \
  --wait
velero restore describe platform-storage-demo-restore --details
oc -n platform-storage-restore get deployment,pods,pvc
```

Compare the restored `/data/events.log` with the backed-up content. Namespace mapping and snapshot restoration must be supported by the installed Velero plugin and storage configuration.

## Retention

```bash
velero backup create short-retention-demo \
  --include-namespaces platform-storage-lab --ttl 72h --snapshot-volumes
```

Velero backup TTL is not a guarantee of underlying provider snapshot retention. Avoid publishing bucket secrets, OADP cloud credentials or real endpoint information.
