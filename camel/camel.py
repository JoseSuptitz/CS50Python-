camel = input('camelCase: ')

for i in range(len(camel)):
    if camel[i].isupper():
        camel = camel.replace(camel[i], f'_{camel[i].lower()}')
print(camel)