import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if value := re.search(r'([0-9]+):?([0-9]*)? (AM|PM) to ([0-9]+):?([0-9]*)? (AM|PM)', s):
        all_values = value.groups()
        if int(all_values[0]) > 12 or int(all_values[3]) > 12:
            raise ValueError
        elif all_values[1] == '' and all_values[4] == '':
            pass
        elif int(all_values[1]) >= 60 or int(all_values[4]) >= 60:
            raise ValueError
        return convert_time(all_values[0], all_values[3], all_values[2], all_values[5], all_values[1], all_values[4])
    else:
        raise ValueError

def convert_time(time_1, time_2, pm_am1, pm_am2, colon_1, colon_2):
    if 'AM' in pm_am1:
        first_time = convert_AM(time_1)
    elif 'PM' in pm_am1:
        first_time = convert_PM(time_1)
    else:
        raise ValueError
    if 'AM' in pm_am2:
        second_time = convert_AM(time_2)
    elif 'PM' in pm_am2:
        second_time = convert_PM(time_2)
    else:
        raise ValueError
    if colon_1 != '' or colon_2 != '':
        return f'{first_time}:{colon_1} to {second_time}:{colon_2}'
    else:
        return f'{first_time}:00 to {second_time}:00'

def convert_AM(time):
    if time == '12':
        return '00'
    elif int(time) >= 10:
        return time
    else:
        return '0' + time

def convert_PM(time):
    if time == '12':
        return time
    else:
        return str(int(time) + 12)
if __name__ == "__main__":
    main()