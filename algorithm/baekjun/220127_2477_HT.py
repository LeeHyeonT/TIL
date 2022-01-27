
# num_per_area = int(input())
x = 0
y = 0
# x_point = []
# y_point = []
x_point_abs = []
y_point_abs = []
width_minus = 0
height_minus = 0
for _ in range (6):
    way, length = list(map(int,input().split()))
    if way == 1:
        x = x + length
    elif way == 2:
        x = x - length
    elif way == 3:
        y = y - length
    elif way == 4:
        y = y + length
    # x_point.append(x)
    # y_point.append(y)
    x_point_abs.append(abs(x))
    y_point_abs.append(abs(y))

for i in range(1,len(x_point_abs)):
    if x_point_abs[i] != x_point_abs[i+1]:
        width_minus = abs(x_point_abs[i] - x_point_abs[i+1])
        continue
    if y_point_abs[i] != y_point_abs[i+1]:
        height_minus = abs(y_point_abs[i] - y_point_abs[i+1])
        break
area_big = max(x_point_abs) * max(y_point_abs)
area_minus = width_minus * height_minus
print(x_point_abs)
print(y_point_abs)
print(area_big - area_minus)

[0 30 30 50 50 0]
[0 0 30 30 50 50]
[30 30 50 50 0 0]