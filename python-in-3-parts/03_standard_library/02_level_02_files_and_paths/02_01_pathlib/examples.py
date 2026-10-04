from pathlib import Path

data_dir = Path("data")
print(data_dir)
print(data_dir / "samples.csv")
print(data_dir.exists(), data_dir.is_dir())

output_dir = Path("results")
output_dir.mkdir(exist_ok=True)
print(output_dir.exists())

for file in Path(".").glob("*.csv"):
    print(file)
