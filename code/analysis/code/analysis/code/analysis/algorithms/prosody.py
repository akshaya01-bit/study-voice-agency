# code/analysis/algorithms/prosody.py
from dataclasses import dataclass

def _clamp(x: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, x))

@dataclass(frozen=True)
class ProsodyTags:
    open_tag: str
    close_tag: str
    pause_ms: int

def ssml_prosody(assertiveness: float, latency_ms: int, turn_cost: float) -> ProsodyTags:
    """
    Map (a in [0,1], L ms, c in [0,1]) -> SSML prosody tags.
    Softens assertiveness when turn_cost is high to preserve user agency.
    """
    a = _clamp(assertiveness, 0.0, 1.0)
    c = _clamp(turn_cost, 0.0, 1.0)
    L = max(0, int(latency_ms))

    a_eff = _clamp(a - 0.25 * c, 0.0, 1.0)  # soften if turn cost is high

    rate_pct = 100 + int(round(15 * a_eff))     # 100..115%
    pitch_st = +1.0 * a_eff                     # 0..+1 semitone
    pause = 300 if L < 700 else 500             # short pause if tighter latency

    open_tag = f'<prosody rate="{rate_pct}%" pitch="{pitch_st:+.1f}st">'
    close_tag = '</prosody>'
    return ProsodyTags(open_tag=open_tag, close_tag=close_tag, pause_ms=pause)

if __name__ == "__main__":
    # Tiny demo to show the tags:
    tags = ssml_prosody(assertiveness=0.7, latency_ms=600, turn_cost=0.4)
    text = "Thanks for your request. I can help with that."
    ssml = f'{tags.open_tag}{text}{tags.close_tag}<break time="{tags.pause_ms}ms"/>'
    print(ssml)
