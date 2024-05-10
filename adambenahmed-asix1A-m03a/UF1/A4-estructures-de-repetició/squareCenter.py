dimensions = input().split()
dim1 = int(dimensions[0])
dim2 = int(dimensions[1])
valid = False
if dim1 % 2 != 0 and dim2 % 2 != 0 or dim1 % 2 == 0 and dim2 % 2 == 0 and dim1 > dim2: valid = True
if valid:
    start_square2 = (dim1 - dim2)/2
    end_square2 = dim1 - start_square2
    for x in range(dim1):
        for y in range(dim1):
            if x >= start_square2 and y >= start_square2 and x < end_square2 and y < end_square2:
                print(end = "🔥 ")
            else: print(end = "🌳 ")
        print(end = "\n")
