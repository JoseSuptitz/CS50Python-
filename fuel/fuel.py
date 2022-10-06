def main():
    fuel = input('Fraction: ').split('/')
    try:
        fuelPerc = int(fuel[0]) / int(fuel[1]) * 100
    except ZeroDivisionError:
        main()
    except ValueError:
        main()

    if int(fuel[0]) > int(fuel[1]):
        main()
    elif fuelPerc <= 1:
        print('E')
    elif fuelPerc >= 99:
        print('F')
    else:
        print(f'{round(fuelPerc)}%')

main()