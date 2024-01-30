def is_palindrome(word):
    length = len(word)
    for i in range(length // 2):
        if word[i] != word[length - i - 1]:
            return False
    return True

word = input("")
if is_palindrome(word):
    print("yes")
else:
    print("no")