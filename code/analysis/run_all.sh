#!/usr/bin/env bash
# Repro runner for the research brief
set -euo pipefail

ENV_NAME=voice-agency

# If Conda is available, create/update the env from environment.yml and activate it
if command -v conda >/dev/null 2>&1; then
  # update if exists, otherwise create (both are safe to run)
  conda env update -n "$ENV_NAME" -f code/analysis/environment.yml --prune || \
  conda env create -n "$ENV_NAME" -f code/analysis/environment.yml

  # load conda and activate
  # (conda activation within a non-interactive shell requires this)
  source "$(conda info --base)/etc/profile.d/conda.sh"
  conda activate "$ENV_NAME"
else
  echo "Conda not found. Please install Anaconda/Miniconda or create a Python env manually."
  echo "See README -> Quickstart for alternatives."
fi

# Run the demo analysis – writes a table/plot into results/
python code/analysis/make_fig_table.py

echo "Done. See results/ for outputs."
