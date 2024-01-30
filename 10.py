def move(n, s, t, a):
    if n > 0:
        move(n-1, s, a, t)
        print(f"Move ring {n} from {s} to {t}")
        move(n-1, a, t, s)


while True:
    try:
        n = int(input(""))
        move(n, 'A', 'C', 'B')
    except EOFError:
        break
