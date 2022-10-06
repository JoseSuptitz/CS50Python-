from random import randint



def main():
    level = get_level()
    counter = 0
    total = 0

    while counter < 10:
        lives = 2
        x, y = generate_integer(level)
        numb_sum = x + y
        while True:
            try:
                guess = int(input(f'{x} + {y} = '))
            except ValueError:
                pass
            if guess == numb_sum:
                total += 1
                break
            elif lives == 0:
                print('EEE')
                print(f'{x} + {y} = {numb_sum}')
                break
            else:
                print('EEE')
                lives -= 1

        counter += 1
        if counter == 10:
            print('Score: ', total)


def get_level():
    try:
        level = int(input('Level: '))
    except ValueError:
        main()
    if level == 1 or level == 2 or level == 3:
        return level
    else:
        main()


def generate_integer(level):
    if level == 1:
        x = randint(0, 9)
        y = randint(0, 9)
        return x, y
    elif level == 2:
        x = randint(10, 99)
        y = randint(10, 99)
        return x, y
    elif level == 3:
        x = randint(100, 999)
        y = randint(100, 999)
        return x, y

if __name__ == "__main__":
    main()