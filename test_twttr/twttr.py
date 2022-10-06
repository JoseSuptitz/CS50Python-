def main():
    letter = input('Input: ')
    print(shorten(letter))

def shorten(word):
    #check for vogals.
    check = word.upper()
    full_word = ''
    for i in range(len(check)):
        if check[i] in ('A','E','I','O','U'):
            continue
    #if no vogals, print the letter and then continue.
        else:
            full_word = full_word + word[i]
    return full_word

if __name__ == "__main__":
    main()