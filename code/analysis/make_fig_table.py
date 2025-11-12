import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

DATA = Path("data/synthetic/study1_demo.csv")
OUT  = Path("results")
OUT.mkdir(exist_ok=True, parents=True)

df = pd.read_csv(DATA)

# Grouped summary (this becomes Table 1)
grp = df.groupby(["condition_seq","condition_acc"]).agg(
    deference_mean=("deference_score","mean"),
    voice_mean=("voice_score","mean"),
    time_mean=("time_seconds","mean"),
    n=("participant_id","count")
).reset_index()

# Save a CSV table
table_path = OUT / "table1_summary.csv"
grp.to_csv(table_path, index=False)

# Quick bar plot: voice_score by Sequencing × Accountability
ax = grp.pivot(index="condition_seq", columns="condition_acc", values="voice_mean").plot(kind="bar")
plt.title("Voice score by Sequencing × Accountability (synthetic)")
plt.ylabel("Mean voice_score (0–1)")
plt.tight_layout()
fig_path = OUT / "figure1_voice.png"
plt.savefig(fig_path)

print(f"Wrote {table_path} and {fig_path}")
