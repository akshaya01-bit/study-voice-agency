# Counter-Bias by Design: Voice Choice-Architecture Levers that Preserve Agency

[![OSF Registration](https://img.shields.io/badge/OSF-753gd-brightgreen)](https://osf.io/753gd)
[![DOI](https://zenodo.org/badge/1095176381.svg)](https://doi.org/10.5281/zenodo.17593594)
[![License: MIT](https://img.shields.io/badge/License-MIT-black.svg)](LICENSE)

**What is this?** Research brief + open materials for a voice-first IVR study.
We test Sequencing (system-first vs human-first) × Accountability (“Claim/Modify”)
and track effects on **deference**, **voice**, and **time**.

**90-sec why:** Subtle prosody/timing can inflate deference in voice-only UIs.
We bound SSML (rate/pitch/break) and add a minimal accountability prompt to preserve agency.

---

## Quickstart

```bash
# create a fresh env (Conda/Mamba)
conda env create -f code/analysis/environment.yml
conda activate voice-agency

# run everything (creates outputs in results/)
bash code/analysis/run_all.sh


## Artifact map
- 📝 Brief: `docs/brief.pdf`
- 🧪 Data (synthetic): `data/synthetic/` + `data/synthetic/data_dictionary.md`
- 🧰 Code: `code/analysis/` (stats/plots)
- 🔁 Repro: `RUN.md`
- 🔒 Privacy: `PRIVACY.md`
- 📜 How to cite: `CITATION.cff` (DOI appears after we mint it with Zenodo)

data/
  synthetic/
    study1_demo.csv
    data_dictionary.md
code/
  analysis/
    environment.yml
    make_fig_table.py
    run_all.sh
results/
  (generated on run)
docs/
  brief.pdf


## Licenses
- Code: MIT (see `LICENSE`).  
- Text & figures in this repo (e.g., `docs/brief.pdf`): **CC BY 4.0** (attribution required).

## How to cite
Akshaya Jayasankar (2025). Counter-Bias by Design: Voice Choice-Architecture Levers that Preserve Agency (artifact bundle). Zenodo. https://doi.org/10.5281/zenodo.17593594

## Contact

Questions, feedback, or collaboration ideas?

- **Open an issue**: https://github.com/akshaya01-bit/study-voice-agency/issues
- **Email**: akshaya.jayasankar [at] example [dot] com  <!-- replace with your real email -->
- **OSF prereg link**: https://osf.io/753gd/
- **Artifact DOI (Zenodo)**: https://doi.org/10.5281/zenodo.17593594

