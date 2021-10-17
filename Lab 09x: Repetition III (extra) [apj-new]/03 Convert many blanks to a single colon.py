def to_colon(s):
    res = ''
    i = 0
    while i<len(s):
        if s[i] == ' ':
            while i<len(s) and s[i] == ' ':
                i += 1
            res += ':'
        else:
            res += s[i]
            i += 1
    return res

while True:
    inp = input('Enter something (or <ENTER> to quit): ')
    if inp == '':
        break
    print(to_colon(inp))
print('Bye!')
