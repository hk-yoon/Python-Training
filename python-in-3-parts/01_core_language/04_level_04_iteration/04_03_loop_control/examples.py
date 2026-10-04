for x in [1, 3, 7, 10]:
    if x > 5:
        print(x)
        break

for x in range(5):
    if x == 2:
        continue
    print(x)

target = 7
for x in [1, 3, 5]:
    if x == target:
        break
else:
    print("not found")

def future_function():
    pass
