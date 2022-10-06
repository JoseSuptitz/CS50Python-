def main():
    greeting = input('Greeting: ')
    print(value(greeting))


def value(greeting):
    greeting = greeting.upper()
    if 'HELLO' in greeting:
        return 0
    elif 'H' in greeting[0]:
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()