# id_list = ["muzi", "frodo", "apeach", "neo"]
# report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
# k = 2

def solution(id_list, report, k):
    matrix = []
    m = len(id_list)
    for i in range(m):
        matrix.append([])
        for j in range(m):
            matrix[i].append(0)
    #show_matrix(matrix)
    # id_list 순서 dict로 저장하기
    num = 0
    name_dic = {}
    for q in id_list:
        name_dic[q] = num
        num += 1
    # report의 각 케이스를 matrix에 기록하기
    for j in report:
        caller, callee = j.split(" ")
        a = name_dic[callee]
        b = name_dic[caller]
        matrix[a][b] = 1
    #show_matrix(matrix)
    # k번 이상 신고당한 멤버 색출
    lst = []
    for o in range(len(matrix)):
        if sum(matrix[o]) >= k:
            lst.append(o)
    #print(lst)
    # 신고 접수 메일을 받은 횟수 계산
    answer = []
    for y in range(len(id_list)):
        answer.append(0)
    for z in lst:
        for w in range(len(matrix[z])):
            answer[w] = answer[w]+matrix[z][w]
    #print(answer)
    return answer

def show_matrix(matrix):
    print(len(matrix))
    for i in range(len(matrix)):
        print(matrix[i])
    return None

def main():
    solution(id_list, report, k)
    return None