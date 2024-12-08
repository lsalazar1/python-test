def isPalindrome(word):

    modified_word=word.lower()
    return modified_word == modified_word[::-1]
      
def isReccuring(s):
    found = ""
    for char in s:
        if char in seen:
            return char
        found += char
    return None

word="pot"
print(isPalindrome(word))

print(isReccuring("affa"))