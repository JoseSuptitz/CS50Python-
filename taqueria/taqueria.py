p_ = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

tot = 0

while True:
    try:
        item = input('Please input: ').title()
        if item in p_:
            tot += p_[item]
            formatted = '{:.2f}'.format(tot)
            print(f'${formatted}')
    except EOFError:
        break
    except TypeError:
        pass