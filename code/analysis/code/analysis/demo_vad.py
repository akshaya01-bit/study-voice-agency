# code/analysis/demo_vad.py
import sys
from algorithms.vad import run_endpoint

def main():
    if len(sys.argv) < 2:
        print("Usage: python code/analysis/demo_vad.py path/to/mono16.wav")
        return
    ts = run_endpoint(sys.argv[1], aggressiveness=2, frame_ms=20, silence_window_ms=400)
    # Print a few lines so users see what's happening
    for t, sp in ts[:20]:
        print(f"{t:7.3f}s  {'speech' if sp else '....'}")

if __name__ == "__main__":
    main()
