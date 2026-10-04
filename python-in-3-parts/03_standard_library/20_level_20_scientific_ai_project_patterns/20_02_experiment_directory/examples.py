from pathlib import Path
from datetime import datetime
run_id = datetime.now().strftime("%Y%m%d_%H%M%S")
run_dir = Path("runs") / run_id
run_dir.mkdir(parents=True, exist_ok=True)
print(run_dir)
