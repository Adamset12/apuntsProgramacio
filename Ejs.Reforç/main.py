strin = input()
i = 0
length = len(strin)
result = ""
while i < length:
    if ord(strin[i]) >= ord("a") and ord(strin[i]) <= ord("z"):
        result += chr(ord(strin[i]) - 32)
    else:
        result += strin[i]
    i += 1
print(result)
