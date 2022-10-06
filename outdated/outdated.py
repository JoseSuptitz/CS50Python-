month = {
    "January" : "01",
    "February" : "02",
    "March" : "03",
    "April" : "04",
    "May" : "05",
    "June" : "06",
    "July" : "07",
    "August" : "08",
    "September" : "09",
    "October" : "10",
    "November" : "11",
    "December" : "12",
}

def main():
    date = input('Please input the date: ').strip()

    #  Check if the date has spaces between characters, and create the ordered date.
    if (date[-5].isspace() == True):

        newDate = date.split()
        if ',' not in newDate[1]:
            main()
        try:
            newDate[1] = newDate[1].replace(',', '').zfill(2)
            newDate[0] = month[newDate[0]].zfill(2)
        except KeyError:
            main()

        #  Checks if the dates are correct.
        check(newDate)

    #  Create the ordered date that has slashes dividing it.
    else:
        newDate = date.split('/')
        newDate[0] = newDate[0].zfill(2)
        newDate[1] = newDate[1].zfill(2)

        #  Checks if the dates are correct, and if there are any ValueErrors.
        try:
            check(newDate)
        except ValueError:
            main()

    print(f"{newDate[2]}-{newDate[0]}-{newDate[1]}")

def check(newDate):
    check = list(map(int, newDate))
    if check[0] > 12 or check[1] > 31:
        main()

main()