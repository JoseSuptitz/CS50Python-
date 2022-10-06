import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    try:
        my_value = re.search(r'.+/embed/(\w+)"', s)
        return f'https://youtu.be/{my_value.group(1)}'
    except AttributeError:
        return None

if __name__ == "__main__":
    main()