def f91(n):
    if (n <= 100):
        num = f91(f91(n+11))
    elif (n >= 101):
        num = n-10

    return num

while True:
    try:
        s = int(input())
        if s == 0:
            break
        a = f"f91({s}) = {f91(s)}"
        print(a)
    except EOFError:
        break