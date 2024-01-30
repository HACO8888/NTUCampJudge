words = []
ans = []

try:
    while True:
        a = input("")
        if (a in words):
            ans.append("YES")
        else:
            words.append(a)
            ans.append("NO")
except EOFError:
    pass

for an in ans:
    print(an)