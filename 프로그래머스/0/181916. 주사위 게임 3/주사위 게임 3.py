def solution(a, b, c, d):
    score = [a,b,c,d]
    score2 = set(score)
    score2 = list(score2)
    score3 = []
    
    for i in range(len(score2)) :
        score3.append(score.count(score2[i]))
    
    if max(score3) == 4 :
        answer = 1111 * a
    elif max(score3) == 3 :
        p = score3.index(3)
        p = score2[p]
        q = score3.index(1)
        q = score2[q]
        answer = ((10*p)+q)**2
    elif score3 == [2,2] :
        p,q = score2[0], score2[1]
        answer = abs(p+q) * abs(p-q)    
    elif max(score3) == 2 :
        score2.remove(score2[score3.index(2)])
        answer = 1
        for i in score2 :
            answer *= i
        print(score2)
    else :
        answer = min(score)
        
    return answer