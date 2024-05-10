floors = int(input())
columns = 1
for x in range(floors):
    for y in range(columns):
        print("# ", end = "")
    columns += 1
    print("\n", end = "")