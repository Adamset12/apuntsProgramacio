quantitat = int(input())
lletres = input().split()
i = 0
while i < quantitat:
    if lletres[i] in ["a", "e", "i", "o", "u"]: print(lletres[i], end = " ")
    i += 1
