#  Asks for plate name to the user and calls function.
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

#  Verifies if the plate name starts with two letters.
def two_letters(s):
    if s[0].isalpha() and s[1].isalpha():
        return True
    else:
        return False

#  Verifies if the minimum and maximum length of string is met.
def max_and_min(s):
    if len(s) >= 2 and len(s) <= 6:
        return True
    else:
        return False

def not_middle(s):
    #  Verifies the presence of a 0 starting at the middle of the plate name.
    for i in range(int(len(s) / 2 + 1)):
        if s[i] == '0':
            return False

    #  Verifies if theres no number at the middle of the plate.
    if not s[-1].isdigit() and s[-2].isdigit():
        return False
    else:
        return True

#  Verifies for special characters.
def special_chars(s):
    specials = ['!', '"', '#', '$', '%', '&', "'",
     '()', '*', '+', ',', '-', '.', '/', ':', ';',
      '<', '=', '>', '?', '@', '[', ' ', ']', '^',
       '_', '`', '{', '|', '}', '~']

    for i in range(len(s)):
        for j in range(len(specials)):
            if s[i] == specials[j]:
                return False
    return True

#  Evaluates to true if all the others functions are true.
def is_valid(s):
    if max_and_min(s) and two_letters(s) and not_middle(s) and special_chars(s):
        return True
    else:
        return False

main()