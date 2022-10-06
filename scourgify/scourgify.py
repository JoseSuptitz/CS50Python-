import sys, csv

names = []

if len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')
elif len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')

try:
    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        next(reader)
        for name, house in reader:
            last, first = name.split(',')
            first = first.strip()
            new_name = [first, last, house]
            names.append(new_name)
except FileNotFoundError:
    sys.exit('File does not exist')

with open(sys.argv[2], 'w') as second_file:
    writer = csv.writer(second_file)
    writer.writerow(['first','last','house'])
    for name in range(len(names)):
        writer.writerow(names[name])