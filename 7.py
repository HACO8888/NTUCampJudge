def check_win(a1, b1, c1):
    a = int(a1)
    b = int(b1)
    c = int(c1)

    if (a > b and a > c):
        if a > (b + c):
            return "A"
        else:
            if b > c:
                return "B"
            else:
                return "C"
    elif (b > a and b > c):
        if b > (a + c):
            return "B"
        else:
            if a > c:
                return "A"
            else:
                return "C"
    elif (c > a and c > b):
        if c > (a + b):
            return "C"
        else:
            if a > b:
                return "A"
            else:
                return "B"


all = []

try:
    while True:
        ts = input().split()
        all.append(check_win(ts[0], ts[1], ts[2]))
except EOFError:
    pass


for a in all:
    print(a)
