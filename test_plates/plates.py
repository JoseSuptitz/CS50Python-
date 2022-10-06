#  Asks for plate name to the user and calls function.
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):

    #  Verifies if the minimum and maximum length of string is met.
    if len(s) >= 2 and len(s) <= 6:
        max_and_min = True
    else:
        return False


    #  Verifies if the plate name starts with two letters.
    if s[0].isalpha() and s[1].isalpha():
        two_letters = True
    else:
        return False

    #  Verifies the presence of a 0 starting at the middle of the plate name.
    for i in range(int(len(s) / 2 + 1)):
        if s[i] == '0':
            return False
        else:
            not_middle = True

    #  Verifies for special characters.
    specials = ['!', '"', '#', '$', '%', '&', "'",
     '()', '*', '+', ',', '-', '.', '/', ':', ';',
      '<', '=', '>', '?', '@', '[', ' ', ']', '^',
       '_', '`', '{', '|', '}', '~']

    for i in range(len(s)):
        for j in range(len(specials)):
            if s[i] == specials[j]:
                return False
    special_chars = True

    #  Verifies if theres no number at the middle of the plate.
    if not s[-1].isdigit() and s[-2].isdigit():
        return False
    else:
        middle_digits = True


    if max_and_min and two_letters and not_middle and special_chars and middle_digits:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
