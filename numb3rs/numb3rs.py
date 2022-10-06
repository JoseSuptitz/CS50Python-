import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):

    if validating := re.search('^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$', ip):
        numbers = ip.split('.')
        if validate_first(numbers) and validate_second(numbers) and validate_third(numbers) and validate_fourth(numbers):
            return True
        else:
            return False
    else:
        return False

def validate_first(numbers):
    if int(numbers[0]) <= 255 and int(numbers[0]) >= 0:
        return True
    else:
        return False
def validate_second(numbers):
    if int(numbers[1]) <= 255 and int(numbers[1]) >= 0:
        return True
    else:
        return False
def validate_third(numbers):
    if int(numbers[2]) <= 255 and int(numbers[2]) >= 0:
        return True
    else:
        return False
def validate_fourth(numbers):
    if int(numbers[3]) <= 255 and int(numbers[3]) >= 0:
        return True
    else:
        return False

if __name__ == "__main__":
    main()