# code/analysis/demo_ssml.py
from algorithms.prosody import ssml_prosody

def main():
    tags = ssml_prosody(assertiveness=0.7, latency_ms=600, turn_cost=0.4)
    text = "Thanks for your request. I can help with that."
    ssml = f'{tags.open_tag}{text}{tags.close_tag}<break time="{tags.pause_ms}ms"/>'
    print(ssml)

if __name__ == "__main__":
    main()
