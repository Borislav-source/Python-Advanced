def palindrome(word, index):
    if len(word) // 2 == index:
        return True
    if not word[index] == word[-1 - index]:
        return f"{word} is not a palindrome"
    if palindrome(word, index+1):
        return f"{word} is a palindrome"




print(palindrome("abcba", 0))
print(palindrome("petep", 0))

import unittest

class Tests(unittest.TestCase):
   def test(self):
      func = palindrome
      res = func("abcba", 0)
      self.assertEqual(res, 'abcba is a palindrome')

if __name__ == "__main__":
   unittest.main()