from pathlib import Path

FIG_DIR = Path(__file__).resolve().parents[1] / "figures"
FIG_DIR.mkdir(exist_ok=True)

def savefig(plt, name: str):
    """Enregistre une figure matplotlib dans figures/<name>.png"""
    out = FIG_DIR / f"{name}.png"
    plt.savefig(out, bbox_inches="tight", dpi=160)
    print(f"Figure enregistrée: {out}")
