letter = input('Input: ')
checking = letter.upper()

#check for vogals.
for i in range(len(letter)):
    if checking[i] == 'A' or checking[i] == 'E' or checking[i] == 'I' or checking[i] == 'O' or checking[i] == 'U':
        continue
    #if no vogals, print the letter and then continue.
    else:
        print(letter[i], end='')