n = int(input())

for i in range(n):
    string = input()
    length = len(string)
    if length <= 2:
        print(-1)
    elif length == 3:
        if string == 'OOO' or string == 'MOM':
            print(1)
        elif string == 'MOO':
            print(0)
        elif string == 'OOM':
            print(2)
        else:
            print(-1)
    else:
        if 'MOO' in string:
            print(length-3)
        elif 'MOM' in string or 'OOO' in string:
            print(length-2)
        elif 'OOM' in string:
            print(length-1)
        else:
            print(-1)
