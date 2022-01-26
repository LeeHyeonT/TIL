s1, s2, s3, s4, s5, s6, s7, s8, s9  = int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input())
s_lst = [s1,s2,s3,s4,s5,s6,s7,s8,s9]
#s_lst = [20,7,23,19,10,15,25,8,13]

for nope1 in range(0, 8):
    for nope2 in range(nope1+1, 9):
        s_lst_sorted = sorted(s_lst)
    #    total = 0
    #    yeap_lst = []
        #for i in s_lst_sorted:
    #    print(s_lst_sorted[nope1], s_lst_sorted[nope2])
        s_lst_sorted.pop(nope1)
        s_lst_sorted.pop(nope2-1)
    #    print(s_lst_sorted)

        if sum(s_lst_sorted) == 100:
            for i in s_lst_sorted:
                print(i)
            break