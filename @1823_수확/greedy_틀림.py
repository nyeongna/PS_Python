n = int(input())
rice = list()
for _ in range(n):
    rice.append(int(input()))


'''greedy 하게 접근하면 안됨
2 2 1 2

인 경우 뒤에서 부터 베어야하는데 아래 코드는 앞에서 2 2를 먼저 베므로 최적이 아님..
즉
'''
first, last = 0, n-1
ans, time = 0, 1
while first <= last:
    # 왼쪽을 먼저 베어야 하는 경우
    if rice[first] < rice[last]:
        ans += rice[first]*time
        first += 1
        #print('left')
    # 오른쪽을 먼저 베어야 하는 경우
    elif rice[first] > rice[last]:
        ans += rice[last]*time
        last -= 1
        #print('right')
    # 양옆이 같은 경우 중앙으로 다가가면서 먼저 더 낮은 가치의 벼를 만나는 쪽을 벤다
    else:
        ff, ll = first+1, last-1
        while ff <= ll:
            if rice[ff] < rice[ll]:
                ans += rice[first]*time
                first +=1
                break
            elif rice[ff] > rice[ll]:
                ans += rice[last]*time
                last -=1
                break
            else:
                ff += 1
                ll -= 1
        if ff > ll:
            ans += rice[first]*time
            first += 1
    time += 1
print(ans)
