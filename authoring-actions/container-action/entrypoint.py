#!/usr/bin/env python3

import os, datetime as dt

# Github injects this env
name = os.getenv("INPUT_WHO_TO_GREET", "World")

# Or can be read as argv using sys

greeting = f"Hello, {name}"
time = f"{dt.datetime.now(dt.timezone.utc) UTC}"

# https://docs.github.com/en/actions/writing-workflows
# Emitting a GHA NOTICE annotation
print(f"::notice file=entrypoint.py,line=12::{greeting}")

# Expose an output for downstream jobs/steps
with open(os.environ["GITHUB_OUTPUT"], "a") as fh:
    fh.write(f"greeting={greeting}\n")
    fh.write(f"time={time}\n")
