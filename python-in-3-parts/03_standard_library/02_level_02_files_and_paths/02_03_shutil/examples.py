from pathlib import Path
import shutil

Path("source.txt").write_text("data", encoding="utf-8")
shutil.copy("source.txt", "backup.txt")
print(Path("backup.txt").read_text(encoding="utf-8"))

print("Directory example: shutil.copytree('experiment1', 'experiment1_backup')")
