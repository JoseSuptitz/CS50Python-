from random import randint
import sys

def main():
    while True:
        try:
            level = int(input('Level: '))
        except ValueError:
            main()
        if level >= 1:
            random_num = randint(1, level)
            guessing(random_num, level)


def guessing(random_num, level):
    try:
        guess = int(input('Guess: '))
    except ValueError:
        guessing(random_num, level)
    if guess >= 1:
        if guess == random_num:
            print('Just right!')
            sys.exit()
        elif guess > random_num:
            print('Too large!')
            guessing(random_num, level)
        elif guess < random_num:
            print('Too small!')
            guessing(random_num, level)
            return
    else:
        guessing(random_num, level)

main()