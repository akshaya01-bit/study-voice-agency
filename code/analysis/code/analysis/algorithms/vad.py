# code/analysis/algorithms/vad.py
import collections
import math
import wave
import webrtcvad  # classic low-latency VAD (10/20/30ms frames)

class Frame:
    def __init__(self, bytes_, timestamp, duration):
        self.bytes = bytes_
        self.timestamp = timestamp
        self.duration = duration

def read_wave(path):
    with wave.open(path, 'rb') as wf:
        assert wf.getnchannels() == 1, "Use mono PCM16 WAV"
        assert wf.getsampwidth() == 2, "Expect 16-bit WAV"
        sample_rate = wf.getframerate()
        pcm = wf.readframes(wf.getnframes())
    return pcm, sample_rate

def frame_generator(frame_ms, audio, sample_rate):
    n = int(sample_rate * (frame_ms / 1000.0) * 2)  # bytes per frame (16-bit mono)
    offset = 0
    timestamp = 0.0
    duration = (float(n) / (2 * sample_rate))
    while offset + n <= len(audio):
        yield Frame(audio[offset:offset+n], timestamp, duration)
        timestamp += duration
        offset += n

def vad_collector(sample_rate, frame_ms, vad, frames, silence_window_ms=400):
    """
    Minimal endpointing: speak until we observe continuous non-voice >= silence_window_ms.
    """
    num_silent = 0
    silent_needed = math.ceil(silence_window_ms / frame_ms)

    for f in frames:
        is_speech = vad.is_speech(f.bytes, sample_rate)
        yield f, is_speech
        if is_speech:
            num_silent = 0
        else:
            num_silent += 1
            if num_silent >= silent_needed:
                # endpoint reached
                return

def run_endpoint(wav_path, aggressiveness=2, frame_ms=20, silence_window_ms=400):
    audio, sr = read_wave(wav_path)
    vad = webrtcvad.Vad(aggressiveness)  # 0=least, 3=most aggressive
    frames = frame_generator(frame_ms, audio, sr)

    out = []
    for f, is_speech in vad_collector(sr, frame_ms, vad, frames, silence_window_ms):
        out.append((f.timestamp, is_speech))
    return out  # list of (timestamp, bool)
