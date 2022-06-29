def solution(lottos, win_nums):
    # 0의 갯수 세고, win_nums와 겹치는 수의 갯수 세기
    # 최대 : 0 만큼 순위 올리기, 최소 : 겹치는 수만 가지고 계산
    hits = len(list(set(lottos) & set(win_nums)))
    zeros = lottos.count(0)
    print(hits, zeros)
    answer = [7-(hits+zeros), 7-hits]
    if answer[0]>5:
        answer[0] = 6
    if answer[1]>5:
        answer[1] = 6
    return answer