
x_dir = [-1,0,1,0]
y_dir = [0,1,0,-1]
d = 0
x, y = 500, 500
up, right, down, left = 500, 500, 500, 500
graph = [ [0]*1010 for _ in range(1010) ]
for _ in range(int(input())):
    d = 0
    x, y = 500, 500
    # 가장 [위, 오른, 밑, 왼]에 해당하는 위치들을 찾아야한다
    up, right, down, left = 500, 500, 500, 500
    order_list = list(map(str, input()))
    for order in order_list:
        if order == 'F':
            x = x + x_dir[d]
            y = y + y_dir[d]
            up, right, down, left = min(up, x), max(right, y), max(down, x), min(left, y)
        elif order== 'B':
            x = x - x_dir[d]
            y = y - y_dir[d]
            up, right, down, left = min(up, x), max(right, y), max(down, x), min(left, y)
        elif order == 'L':
            d = (d - 1) % 4
        elif order == 'R':
            d = (d + 1) % 4
    # 아래에서 위 빼면 높이
    # 오른쪽에서 왼쪽 빼면 밑변길이
    size = (down - up) * (right - left)
    print(size)

        