import random, art

class Points:
    def __init__(self):
        self.lives = random.randint(5, 10)

    @property
    def lives(self):
        return self._lives

    @lives.setter
    def lives(self, lives):
        self._lives = lives

# Initialize Points class.
points = Points()
all_lives = points.lives

# Get random number.
random_num = random.randint(1, 1000)
condition = True

# Get the guess and loop for checking.
def main(condition):
    while condition == True:
        guess = get_guess()
        try:
            condition = check(guess, random_num)
        except TypeError:
            pass

# Guess from 1 to 1000 and error checking.
def get_guess():
    try:
        guess = int(input('Guess between 1 & 1000: '))
        return guess
    except ValueError:
        art.tprint('Try inserting a number', font="small")

# Checks if higuer then guess, lower, or if its equal to.
def check(guess, random_num):
    if guess > random_num:
        art.tprint(f'{points.lives - 1} lives left, guess too high', font="small")
        return new_lives(random_num)
    elif guess < random_num:
        art.tprint(f'{points.lives - 1} lives left, guess too low', font="small")
        return new_lives(random_num)
    else:
        art.tprint(f'You did it! it was {random_num}, you had {all_lives} lives', font="small")
        return False

# Reduces the player lives from the Points class.
def new_lives(random_num):
    points.lives -= 1
    if points.lives == 0:
        art.tprint(f'Game Over, the number was: {random_num}', font="small")
        return False
    return True

if __name__ == "__main__":
    main(condition)