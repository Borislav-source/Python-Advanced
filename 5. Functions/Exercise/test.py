def palindrome(word, i):
    if len(word) < 2 or word[0] == word[-1] and palindrome(word[1:-1], i):
        return f"{word} is a palindrome"
    else:
        return f"{word} is not a palindrome"

print(palindrome("abcba", 0))
print(palindrome("petvp", 0))