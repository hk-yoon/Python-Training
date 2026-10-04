from collections import defaultdict
genes = defaultdict(list)
genes["pathway1"].append("TP53")
genes["pathway1"].append("BRCA1")
print(genes)
