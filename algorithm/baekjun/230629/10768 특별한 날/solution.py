month = int(input())
day = int(input())
if month == 1:
    print('Before')
else:
    if month >= 3:
        print('After')
    else:
        if day < 18:
            print('Before')
        elif day == 18:
            print('Special')
        else:
            print('After')