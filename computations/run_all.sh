#!/bin/sh
# Reproduce all computations. Requires python3 only.
set -e
cd "$(dirname "$0")"
echo "== exact prime-range checks (Theorems A and B), ~40 s"; python3 pmin.py
