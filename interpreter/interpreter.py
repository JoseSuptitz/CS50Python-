x, y, z = input('Expression: ').split()

match y:
    case '+':
        print(float(x) + float(z))
    case '-':
        print(float(x) - float(z))
    case '*':
        print(float(x) * float(z))
    case '/':
        print(float(x) / float(z))
