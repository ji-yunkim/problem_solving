
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
def solution(numbers, hand):
    # distance measurement
    keys = {1:[1,1], 2:[1,2], 3:[1,3], 4:[2,1], 5:[2,2], 6:[2,3], 7:[3,1], 8:[3,2], 9:[3,3], "*":[4,1], 0:[4,2], "#":[4,3]}
    l = "*"
    r = "#"
    txt = ""
    sentence = ""
    for i in numbers:
        if i in [1,4,7]:
            txt = "L"
            l = i
        elif i in [3,6,9]:
            txt = "R"
            r = i
        else:
            txt = "0"
            # 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용
            l_d = abs(keys[l][0]-keys[i][0])+abs(keys[l][1]-keys[i][1])
            r_d = abs(keys[r][0]-keys[i][0])+abs(keys[r][1]-keys[i][1])
            if l_d > r_d :
                txt = "R"
                r = i
            elif r_d > l_d:
                txt = "L"
                l = i
            else:
                # 거리가 같다면 오른손잡이는 오른손, 왼손잡이는 왼손
                if hand == "right":
                    txt = "R"
                    r = i
                else:
                    txt = "L"
                    l = i
        sentence += txt
    return sentence