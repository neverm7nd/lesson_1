def is_palindrome(string):
    reversed_string = string[::-1] 
    if string == reversed_string:
        return True
    else:
        return False
