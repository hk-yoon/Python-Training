import csv

with open("samples.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["sample", "value"])
    writer.writerow(["S01", 3.5])

with open("samples.csv", encoding="utf-8") as f:
    for row in csv.reader(f):
        print(row)

with open("samples.csv", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        print(row["sample"])
