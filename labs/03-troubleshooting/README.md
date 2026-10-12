# Lab 03 — Storage-related workload troubleshooting

`CrashLoopBackOff` describes repeated crashes; it is not itself a root cause. Inspect logs and Pod events, then repair the underlying issue.

```bash
oc -n platform-storage-lab get pods,pvc
oc -n platform-storage-lab describe pods -l app=data-writer
oc -n platform-storage-lab logs deployment/data-writer --previous
oc -n platform-storage-lab describe pvc app-data
oc -n platform-storage-lab get events --sort-by=.metadata.creationTimestamp
```

| Symptom | Check | Likely action |
| --- | --- | --- |
| Pod Pending; PVC Pending | StorageClass, CSI provisioner, capacity, quota | Fix provisioning or choose installed class |
| CrashLoopBackOff due to missing path | App logs, command, volumeMounts | Mount PVC at app's actual expected write location |
| Volume full | `df -h` inside pod; PVC status | Expand if provisioner supports resizing |
| Multi-Attach error | RWO access mode, Pod nodes, VolumeAttachment | Single writer / same-node scheduling or select RWX-capable file volume |
| Permission denied | Pod UID, SCC, ownership, driver | Correct directory access with policy-compliant security settings |
| Filesystem path rather than block device | `volumeMode`, `volumeMounts` | Expected on filesystem RBD; use `Block` and `volumeDevices` for raw device |

**Controlled failure:** In a disposable lab, temporarily change the write target to `/missing/events.log`. Observe logs and Pod status, then restore `/data/events.log`.

Check `allowVolumeExpansion`, LimitRange, ResourceQuota and ODF pool health before resizing.
