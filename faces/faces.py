def convert(phrase):
    newValue = phrase.replace(":)", "🙂").replace(":(", "🙁")

    return newValue

def main():
    phrase = input()
    newPhrase = convert(phrase)
    return print(newPhrase)

main()