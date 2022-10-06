grocery_list = {}
while True:
    try:
        grocery = input().upper()
        if grocery not in grocery_list:
            grocery_list[grocery] = 1
        elif grocery in grocery_list:
            grocery_list[grocery] += 1
    except EOFError:
        for k, v in sorted(grocery_list.items()):
            print(v, k)
        break
