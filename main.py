def isPalindrome(word):

    modified_string="".join(char.lower() for char in word if char.isalnum())
    if modified_string == modified_string[::-1]:
        return True
    return False


word="Madam"
print(isPalindrome(word))