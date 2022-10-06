import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    s = s.lower()
    counting = re.findall(r'\bum\b', s)
    return len(counting)


if __name__ == "__main__":
    main()