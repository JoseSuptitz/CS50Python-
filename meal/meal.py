def main():
    time = input('Please input the time: ')
    converted = convert(time)
    if converted >= 7.0 and converted <= 8.0:
        print('breakfast time')
    elif converted >= 12.0 and converted <= 13.0:
        print('lunch time')
    elif converted >= 18.0 and converted <= 19.0:
        print('dinner time')

def convert(time):
    hours, minutes = time.split(":")
    realTime = ((int(hours) * 60) + int(minutes)) / 60
    return realTime

if __name__ == "__main__":
    main()