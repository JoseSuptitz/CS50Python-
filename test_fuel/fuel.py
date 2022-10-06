def main():
    fuel = input('Fraction: ')
    fuel_convert = convert(fuel)
    print(gauge(fuel_convert))

def convert(fraction):
        fraction = fraction.split('/')
        fuelPerc = int(fraction[0]) / int(fraction[1]) * 100
        if int(fraction[0]) > int(fraction[1]):
            raise ValueError()
        return fuelPerc

def gauge(percentage):
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return f'{round(fuelPerc)}%'


if __name__ == "__main__":
    main()