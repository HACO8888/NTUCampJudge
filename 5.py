from sys import stdin

history = []

for line in stdin:
    inputString = line

    if inputString in history:
        print("YES")
    else:
        print("NO")

    history.append(inputString)