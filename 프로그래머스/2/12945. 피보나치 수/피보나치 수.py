def solution(n):
    answer = [0,1]
    for i in range(2,100001) :
        answer.append(answer[i-1]+answer[i-2])
    return answer[n]%1234567