from datetime import date
import inflect, sys

p = inflect.engine()

def main():
    date = input('Date of Birth: ')
    print(age(date))

def age(birthdate):
    today = date.today()
    try:
        year, month, day = birthdate.split('-')
    except ValueError:
        sys.exit('Invalid date')
    born = date(int(year), int(month), int(day))
    total_days = today - born
    total_days, rest = str(total_days).split(',')
    total_days, rest = total_days.split(' ')
    total_days = int(total_days) * 24 * 60
    return f'{p.number_to_words(total_days, andword="").capitalize()} minutes'

if __name__ == "__main__":
    main()