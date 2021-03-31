def spin(gear_num, direction):
    if direction == -1:
        if gear_num == 0:

        else:
            gear[gear_num] = gear[gear_num][1:]+gear[gear_num][:1]
            logic(gear_num, direction)
    elif direction == 1:
        gear[gear_num] = gear[gear_num][7:]+gear[gear_num][:7]
        logic(gear_num, direction)

def logic(gear_num, direction):
    # 1번 톱니바퀴
    if gear_num == 0:
        # 2번 톱니바퀴의 오른쪽과 극이 같다면 노 회전
        if gear[0][2] == gear[1][6]:
            return
        # 2번 톱니바퀴의 오른쪽과 극이 다르다면 반대 방향으로 회전
        else:
            direction *= -1
            spin(1, direction)
    # 4번 톱니바퀴
    elif gear_num == 3:
        # 3번 톱니바퀴의 왼쪽과 극이 같다면 노 회전
        if gear[gear_num][6] == gear[2][2]:
            return
        # 3번 톱니바퀴의 왼쪽과 극이 다르다면 반대 방향으로 회전
        else:
            direction *= -1
            spin(2, direction)
    # 2, 3번 톱니바퀴
    elif gear_num == 1 or gear_num == 2:
        # 양쪽 모두 고려한다.
        # 오른쪽 톱니바퀴의 왼쪽과 극이 같다면 노회전
        if gear[gear_num][2] == gear[gear_num + 1][6] and gear[gear_num][6] == gear[gear_num-1][2]:
            return
        # 오른쪽 톱니바퀴의 왼쪽과 극이 다르다면 반대방향으로 회전
        else:
            direction *= -1
            if gear[gear_num][2] != gear[gear_num + 1][6] and gear[gear_num][6] == gear[gear_num-1][2]:
                spin(gear_num + 1, direction)
            elif gear[gear_num][2] == gear[gear_num + 1][6] and gear[gear_num][6] != gear[gear_num-1][2]:
                spin(gear_num-1, direction)
            elif gear[gear_num][2] == gear[gear_num + 1][6] and gear[gear_num][6] == gear[gear_num-1][2]:
                spin(gear_num + 1, direction)
                spin(gear_num - 1, direction)
gear =[]
for _ in range(4):
    gear.append(list(map(int, input())))

k = int(input())
for _ in range(k):
    gear_num, direction = map(int, input().split())
    spin(gear_num-1, direction)

point = 0
for i in range(4):
    if gear[i][0] == 0:
        continue
    elif gear[i][0] == 1:
        point += 2**i
        print(i, point)
print(point)