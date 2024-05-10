nmbr = str(int(input()))
nmbr_digits = len(nmbr)
mysum = 0
for x in range(nmbr_digits):
    mysum += int(nmbr[x])
print(mysum)