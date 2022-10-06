from PIL import Image, ImageOps
from os.path import splitext
import sys

def main():

    checking_inputs()
    # Opening images.
    try:
        imagefile = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit('Input does not exist')

    shirtfile = Image.open("shirt.png")

    # Get shirt size.
    size = shirtfile.size

    # Resize muppet image to insert shirt.
    muppet = ImageOps.fit(imagefile, size)

    # Paste shirt on muppet.
    muppet.paste(shirtfile, shirtfile)

    # Save file.
    muppet.save(sys.argv[2])

def check_extension(file):
    if file in ['.jpg', '.jpeg', '.png']:
        return True
    return False

def checking_inputs():
    check1 = splitext(sys.argv[1])
    check2 = splitext(sys.argv[2])

    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')

    if check_extension(check1[1]) == False:
        sys.exit('Invalid input')
    if check_extension(check2[1]) == False:
        sys.exit('Invalid input')
    if check1[1].upper() != check2[1].upper():
        sys.exit('Input and output have different extensions')

if __name__ == '__main__':
    main()