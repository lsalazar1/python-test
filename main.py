def isPalindrome(word):

    modified_word=word.lower()
    return modified_word == modified_word[::-1]
      


word="pot"
print(isPalindrome(word))