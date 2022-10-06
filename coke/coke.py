amount = 50
while amount > 0:

    insert = int(input('insert coin: '))

    if (insert == 25) or (insert == 10) or (insert == 5):
        amount -= insert


    print(abs(amount))

