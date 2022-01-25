lst1 = list (map (int, input().split(" ")))
lst2 = list (map (int, input().split(" ")))
lst3 = list (map (int, input().split(" ")))
lst4 = list (map (int, input().split(" ")))

lst=[lst1, lst2, lst3, lst4]


lx, ly, rx, ry = [], [], [], []
for i in lst:
    lx.append(i[0])
    ly.append(i[1])
    rx.append(i[2])
    ry.append(i[3])


area = 0
#x축 기준으로 너비 구해 나갈 것 lx의 최솟값 ~ rx의 최댓값 사이 구간
for widX in range(min(lx), max(rx)):
    ly_lst = [0]
    ry_lst = [0]

    for i in range(0, 4):

        if lst[i][0] <= widX < lst[i][2]:
            ly_lst.append(lst[i][1])
            ry_lst.append(lst[i][3])
        #print(ry_lst, ly_lst)

# list 항목이 1이하인 경우 max 에러나서 장황해짐
    if len(ly_lst) == 1: # ly_lst = [0]
        area = area + max(ry_lst)
    elif len(ly_lst) == 2:
        area = area + max(ry_lst) - ly_lst[1]
    else:
        ly_lst.pop(0) #ly_lst = [2, 7]
        area = area + max(ry_lst) - min(ly_lst) 
print(area)