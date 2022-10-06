greeting = input('Greeting: ').upper()

if 'HELLO' in greeting:
    print('$0')
elif 'H' in greeting[0]:
    print('$20')
else:
    print('$100')