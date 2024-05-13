def solution(k, score):
    answer = [score[0]]
    honor = [score[0]]
    for i in range(1,len(score)) :
        if len(honor) < k :
            honor.append(score[i])
            answer.append(min(honor))
        else :
            honor.sort(reverse=True)
            honor[-1] = max(honor[-1], score[i])
            answer.append(min(honor))
    return answer