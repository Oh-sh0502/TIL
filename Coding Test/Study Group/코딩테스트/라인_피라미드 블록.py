def cycle(d):
    for i in range(1,n):
        for j in range(i):
            sumlist=[d[i-1][j],d[i][j],d[i][j+1]]
            print(sumlist)
            if sumlist.count(0) >= 2:
                continue
            if sumlist[0] != sumlist[1] + sumlist[2]:
                if sumlist.index(0) == 1:
                    sumlist[1] = sumlist[0] - sumlist[2]
                    d[i][j] = sumlist[1]
                elif sumlist.index(0) == 2:
                    sumlist[2] = sumlist[0] - sumlist[1]
                    d[i][j+1] = sumlist[2]
            print(sumlist)
            print(d)
    return d
n = len(list)
def Solution(list):
    result = []
    layer = []
    order = []
    for i in list:
        layer.append(i[0])
        order.append(i[1])
    print(n)
    d = []
    for i in range(1,n+1):
        d.append([0]*i)
    print(d)
    for i in range(len(list)):
        d[i][list[i][0]] = list[i][1]
    print(d)
    cycle(d)

    return result

ans1 = [[0,50], [0,22], [2,10], [1,4], [4,-13]]
ans2 = [[0,92],[1,20],[2,11],[1,-81],[3,98]]
print(Solution(ans1))
print(Solution(ans2))