import random
import string


def password_generting (length,numbers = True,special_chars = True):
    letters = string.ascii_letters
    digits = string.digits
    chars = string.punctuation
    word = letters
    if numbers:
        word += digits
    if special_chars:
        word += chars
    print(word)
    password = ""
    meets_rules = False
    has_number = False
    has_special_chars = False
    
    while not meets_rules or len(password) < length:
        new_chars = random.choice(word)
        print(new_chars)
        password += new_chars
        if new_chars in digits:
            has_number = True
            
        if new_chars in chars:
            has_special_chars = True
        
        meets_rules = True
        
    return password

has_number = input("numbers: ") == "y"
has_chars = input("chars : ") == "y"
print(password_generting(10,has_number,has_chars))