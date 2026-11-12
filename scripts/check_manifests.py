#!/usr/bin/env python3
"""Static structure check for the portfolio's Kubernetes manifest examples.

This does NOT claim the manifests were applied to a live OpenShift cluster.
"""
from pathlib import Path
import sys
import yaml

files = sorted(Path("labs").rglob("*.yaml"))
if not files:
    sys.exit("No YAML manifests found under labs/")

errors = []
checked = 0
for path in files:
    try:
        documents = list(yaml.safe_load_all(path.read_text(encoding="utf-8")))
    except (OSError, yaml.YAMLError) as exc:
        errors.append(f"{path}: cannot parse YAML: {exc}")
        continue
    for number, document in enumerate(documents, start=1):
        if not isinstance(document, dict):
            errors.append(f"{path} document {number}: expected an object")
            continue
        for field in ("apiVersion", "kind", "metadata"):
            if not document.get(field):
                errors.append(f"{path} document {number}: missing {field}")
        metadata = document.get("metadata")
        if not isinstance(metadata, dict) or not metadata.get("name"):
            errors.append(f"{path} document {number}: missing metadata.name")
        checked += 1

if errors:
    print("\n".join(errors), file=sys.stderr)
    sys.exit(1)
print(f"PASS: parsed {checked} resource documents from {len(files)} files.")
print("Static validation only; API schema, permissions, storage, and runtime checks remain open.")
