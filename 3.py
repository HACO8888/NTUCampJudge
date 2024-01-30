nums = input()
peoples = input().split()
big = 0

for people in peoples:
  if int(people) > big:
    big = int(people)

print(big)