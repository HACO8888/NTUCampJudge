def check_yee(s):
    final = 0
    j = 1

    for i in range(len(s)):
        if s[i] == "y":
            final += abs((i+1) - j)
            j += 3

    return final


try:
    while True:
        s = input()
        print(check_yee(s))
except EOFError:
    pass
