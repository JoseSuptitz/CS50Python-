import sys

line_count = 0

if not sys.argv[1].endswith('.py'):
    sys.exit('Not a Python file')
elif len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')
elif len(sys.argv) < 2:
    sys.exit('Too few command-line arguments')

try:
    with open(sys.argv[1]) as file:
        for line in file:
            if line.strip().startswith('#') or line.isspace():
                pass
            else:
                line_count += 1
    print(line_count)
except FileNotFoundError:
    sys.exit('File does not exist')

