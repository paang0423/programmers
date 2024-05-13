def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    num = len(score) // m
    for i in range(num):
        group_min = min(score[i*m:(i+1)*m])
        answer += group_min * m
    return answer
