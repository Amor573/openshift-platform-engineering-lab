# Lab 02 — PVC, mounted data path and resize

**Goal:** The application's data is written to `/data/events.log` *inside the container*. The PVC is mounted at `/data` so the data survives a Pod recreation.

```bash
oc get storageclasses
oc apply -f labs/02-persistent-storage/namespace.yaml
oc apply -f labs/02-persistent-storage/pvc.yaml
oc -n platform-storage-lab get pvc -w
oc apply -f labs/02-persistent-storage/deployment.yaml
oc -n platform-storage-lab rollout status deployment/data-writer --timeout=120s
oc -n platform-storage-lab exec deploy/data-writer -- tail -n 3 /data/events.log
oc -n platform-storage-lab rollout restart deployment/data-writer
oc -n platform-storage-lab rollout status deployment/data-writer
oc -n platform-storage-lab exec deploy/data-writer -- tail -n 3 /data/events.log
```

A filesystem-mode PVC backed by **Ceph RBD** presents a mounted directory, even though the CSI storage behind it is block-based. For raw block devices use `volumeMode: Block` and `volumeDevices` instead of `volumeMounts`; the application must know how to use the device.

The PVC uses the default StorageClass unless you explicitly set `storageClassName`. Check actual cluster classes; `ocs-storagecluster-ceph-rbd` is common on ODF but not guaranteed.

### Diagnose

```bash
oc -n platform-storage-lab describe pvc app-data
oc -n platform-storage-lab describe pod -l app=data-writer
oc -n platform-storage-lab logs deployment/data-writer
oc -n platform-storage-lab get events --sort-by=.lastTimestamp
```

To request expansion, first check `oc get storageclass -o yaml` for `allowVolumeExpansion: true`, plus quota/capacity. Resize the PVC request to `4Gi` and inspect status. Shrinking is generally unsupported.

A PVC **does not automatically copy historical data from another server path**. Migrate historical data explicitly using appropriate tooling.
