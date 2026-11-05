#!/usr/bin/env python3
"""List or delete remote branches with a given suffix older than N days."""

from __future__ import annotations

import argparse
import subprocess
import sys
from datetime import datetime, timedelta, timezone


PROTECTED = frozenset({"main", "master", "develop", "development", "production", "staging"})


def run(cmd: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, check=False, capture_output=True, text=True)


def list_remote_tips(remote: str) -> list[tuple[int, str]]:
    ref = f"refs/remotes/{remote}"
    proc = run(
        [
            "git",
            "for-each-ref",
            "--format=%(committerdate:unix)|%(refname:short)",
            ref,
        ]
    )
    if proc.returncode != 0:
        sys.stderr.write(proc.stderr)
        raise SystemExit(proc.returncode)

    rows: list[tuple[int, str]] = []
    prefix = f"{remote}/"
    for line in proc.stdout.splitlines():
        if "|" not in line:
            continue
        unix_s, short = line.split("|", 1)
        if not short.startswith(prefix):
            continue
        name = short[len(prefix) :]
        rows.append((int(unix_s), name))
    return rows


def candidates(
    rows: list[tuple[int, str]],
    *,
    suffix: str,
    cutoff_unix: int,
) -> list[tuple[int, str]]:
    out: list[tuple[int, str]] = []
    for unix, name in rows:
        if name in PROTECTED:
            continue
        if not name.endswith(suffix):
            continue
        if unix >= cutoff_unix:
            continue
        out.append((unix, name))
    out.sort(key=lambda item: item[0])
    return out


def delete_batches(remote: str, names: list[str], batch_size: int = 15) -> int:
    failed = 0
    for i in range(0, len(names), batch_size):
        batch = names[i : i + batch_size]
        proc = run(["git", "push", remote, "--delete", *batch])
        sys.stdout.write(proc.stdout)
        sys.stderr.write(proc.stderr)
        if proc.returncode != 0:
            failed += 1
    return failed


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--remote", default="origin")
    parser.add_argument("--suffix", default="-review")
    parser.add_argument("--days", type=int, default=60)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--dry-run", action="store_true")
    mode.add_argument("--delete", action="store_true")
    args = parser.parse_args()

    cutoff_dt = datetime.now(timezone.utc) - timedelta(days=args.days)
    cutoff_unix = int(cutoff_dt.timestamp())
    rows = list_remote_tips(args.remote)
    matched = candidates(rows, suffix=args.suffix, cutoff_unix=cutoff_unix)

    print(f"remote={args.remote} suffix={args.suffix} days={args.days}")
    print(f"cutoff_utc={cutoff_dt.strftime('%Y-%m-%d')} count={len(matched)}")
    for unix, name in matched:
        day = datetime.fromtimestamp(unix, tz=timezone.utc).strftime("%Y-%m-%d")
        print(f"{day}\t{name}")

    if args.dry_run or not matched:
        return

    failed_batches = delete_batches(args.remote, [name for _, name in matched])
    if failed_batches:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
