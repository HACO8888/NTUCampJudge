def is_prime(n):
    if n <= 1:
        return "N"
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return "N"
    return "Y"

input()
all = []

while True:
    try:
        s = input()
        all.append(is_prime(int(s)))
    except EOFError:
        break
    
for a in all:
    print(a)
