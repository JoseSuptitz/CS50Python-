import inflect

names = []
p = inflect.engine()


while True:
    try:
        name = input('Name: ').strip()
        names.append(name)
    except EOFError:
        print()
        break

result = p.join(names)

print('Adieu, adieu, to', result)