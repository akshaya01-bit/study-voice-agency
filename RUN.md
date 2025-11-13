# Run everything (one command)

```bash
# create/update env, activate, and run analysis
conda env update -f code/analysis/environment.yml
conda activate voice-agency
bash code/analysis/run_all.sh

## Algorithms quick test

# Prosody → SSML
python code/analysis/demo_ssml.py
# prints an SSML snippet using <prosody rate="…" pitch="…">…</prosody>

# VAD endpointing (needs a small mono 16-bit PCM WAV)
# You can convert an mp3 with: ffmpeg -i in.mp3 -ac 1 -ar 16000 -acodec pcm_s16le sample.wav
python code/analysis/demo_vad.py sample.wav
