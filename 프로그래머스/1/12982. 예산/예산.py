def solution(d, budget):
    answer, count = 0,0
    d.sort()
    for i in d :
        answer += i
        count += 1
        if answer > budget :
            answer -= i 
            count -= 1
    return count