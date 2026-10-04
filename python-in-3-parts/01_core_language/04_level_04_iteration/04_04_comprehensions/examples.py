squares = [x * x for x in range(5)]
print(squares)

values = [1, 2, 2, 3]
unique_squares = {x * x for x in values}
print(unique_squares)

genes = ["TP53", "EGFR"]
lengths = {gene: len(gene) for gene in genes}
print(lengths)
