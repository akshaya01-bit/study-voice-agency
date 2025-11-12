from dataclasses import dataclass

@dataclass
class ProsodyInput:
    assertiveness: float  # 0..1
    latency_ms: int       # allowed budget in ms
    turn_cost: float      # 0..1

@dataclass
class ProsodyOutput:
    rate: float        # e.g., 1.00 means 100%
    pitch_st: float    # semitones
    pause_ms: int
    ssml_open: str
    ssml_close: str

def prosody(a: float, L: int, c: float) -> ProsodyOutput:
    # Bound inputs
    a = max(0.0, min(1.0, a))
    c = max(0.0, min(1.0, c))
    L = max(0, L)

    a_eff = max(0.0, a - 0.25 * c)  # soften if turn-cost high
    rate = 1.00 + 0.15 * a_eff
    pitch_st = 0.0 + 1.0 * a_eff
    pause = 300 if L < 700 else 500

    ssml_open = f'<prosody rate="{rate:.2f}" pitch="{pitch_st:+.1f}st">'
    ssml_close = f'</prosody><break time="{pause}ms"/>'
    return ProsodyOutput(rate, pitch_st, pause, ssml_open, ssml_close)
