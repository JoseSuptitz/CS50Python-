from pyfiglet import Figlet
from random import choice
import sys

figlet = Figlet()
fonts_figlet = figlet.getFonts()

def main():
    if(len(sys.argv) == 3):
        chosen_font()
    elif(len(sys.argv) == 1):
        random_font()
    else:
        sys.exit('Invalid usage')

def chosen_font():
    if(sys.argv[1] == '-f' or sys.argv[1] == '--font'):
        if fonts_figlet.count(sys.argv[2]) > 0:
            desired_text = input('Your text: ')
            figlet.setFont(font=sys.argv[2])
            print(figlet.renderText(desired_text))
        else:
            sys.exit('Invalid usage')
    else:
        sys.exit('Invalid usage')

def random_font():
    desired_text = input('Your text: ')
    random_font = choice(fonts_figlet)
    figlet.setFont(font=random_font)
    print(figlet.renderText(desired_text))

main()