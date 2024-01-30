usrInput = input()

while usrInput != "0":
    userInputInt = int(usrInput)

    for i in range(userInputInt):
        row = [
            *("_" for j in range(userInputInt - i - 1)),
            *("+" for j in range(i + 1)),
        ]

        print("".join(row))

    usrInput = input()