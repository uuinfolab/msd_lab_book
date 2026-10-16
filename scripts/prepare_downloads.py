from pathlib import Path
import shutil

root = Path(__file__).resolve().parents[1]

for source in (root / "labs").rglob("*.ipynb"):
    if ".ipynb_checkpoints" in source.parts:
        continue

    target = root / "downloads" / source.relative_to(root / "labs")
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)
