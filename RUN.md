# RUN.md — one-command repro

## 0) Prereqs
- Conda (Anaconda or Miniconda)

## 1) Create/Update the environment
```bash
conda env create -f code/analysis/environment.yml || conda env update -f code/analysis/environment.yml
conda activate voice-agency

2) Run everything
bash code/analysis/run_all.sh
3) Algorithms quick test
Prosody → SSML
python code/analysis/demo_ssml.py

VAD endpointing (needs a small mono 16 kHz PCM WAV)
# convert any audio (requires ffmpeg installed locally)
ffmpeg -i in.mp3 -ac 1 -ar 16000 -acodec pcm_s16le sample.wav

python code/analysis/demo_vad.py sample.wav
4) Outputs

results/figure1_voice.png

results/table1_summary.csv
