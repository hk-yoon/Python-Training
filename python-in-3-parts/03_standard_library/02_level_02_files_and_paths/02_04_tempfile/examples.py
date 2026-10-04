import tempfile
from pathlib import Path

with tempfile.TemporaryDirectory() as tmp:
    p = Path(tmp) / "result.txt"
    p.write_text("temporary result", encoding="utf-8")
    print(p.read_text(encoding="utf-8"))
