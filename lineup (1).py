def lineUp2(commands):
    res = 0
    same = True
    for command in commands:
        if command in 'LR':
            same = not same
        if same:
            res += 1
    return res


print(lineUp2("LLARL"))
