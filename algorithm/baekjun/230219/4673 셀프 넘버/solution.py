
def Function(n):
    global not_using
    new_n = n
    for i in range(len(str(n))):
        new_n += int(str(n)[i])
    not_using.append(new_n)

one_to_man = [num for num in range(1, 10001)]
not_using = []
for j in range(1, 10000):
    Function(j)

for ans in one_to_man:
    if ans not in not_using:
        print(ans)

'''
2만번 정도 반복하는 것은 문제가 되지 않는다!
쫄지 말고 해보도록.....
'''