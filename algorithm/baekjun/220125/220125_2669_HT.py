square1_coordinate = list(map(int, input().split()))
square2_coordinate = list(map(int, input().split()))
square3_coordinate = list(map(int, input().split()))
square4_coordinate = list(map(int, input().split()))    

x_list = [square1_coordinate[0], square1_coordinate[2], 
square2_coordinate[0], square2_coordinate[2],
square3_coordinate[0], square3_coordinate[2],
square4_coordinate[0], square4_coordinate[2]
]

y_list = [square1_coordinate[1], square1_coordinate[3],
square2_coordinate[1], square2_coordinate[3],
square3_coordinate[1], square3_coordinate[3],
square4_coordinate[1], square4_coordinate[3]]

x_list.sort()
y_list.sort()
# surface_cnt = 0
# for i in range(x_list[0], x_list[7]):
#     if square1_coordinate[0] <= i < square1_coordinate[2]:
#         if square2_coordinate[0] <= i < square2_coordinate[2]:

#         surface_cnt += square1_coordinate[3] - square1_coordinate[1]
#     elif square2_coordinate[0] <= i < square2_coordinate[2]:
#         surface_cnt += square2_coordinate[3] - square2_coordinate[1]
#     elif square3_coordinate[0] <= i < square3_coordinate[2]:
#         surface_cnt += square3_coordinate[3] - square3_coordinate[1]
#     elif square4_coordinate[0] <= i < square4_coordinate[2]:
#         surface_cnt += square4_coordinate[3] - square4_coordinate[1]

print(x_list)
print(y_list)
# print(surface_cnt)

