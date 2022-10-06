from tabulate import tabulate
import sys, csv

menu = []

if not sys.argv[1].endswith('.csv'):
    sys.exit('Not a CSV file')
elif len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')
elif len(sys.argv) < 2:
    sys.exit('Too few command-line arguments')

try:
    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        for Pizza, Small, Large in reader:
            menu.append([Pizza, Small, Large])
except FileNotFoundError:
    sys.exit('File does not exist')

table = menu
print(tabulate(table, headers="firstrow", tablefmt="grid"))

