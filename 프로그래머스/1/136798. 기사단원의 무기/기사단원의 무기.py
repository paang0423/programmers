def get_divisor_counts(limit):
    yaksu = [0] * (limit + 1)
    for i in range(1, limit + 1):
        for j in range(i, limit + 1, i):
            yaksu[j] += 1
    return yaksu

def solution(number, limit, power):
    answer = 0
    yaksu = get_divisor_counts(number)
    for i in range(1, number + 1) :
        if yaksu[i] > limit :
            yaksu[i] = power  
    return sum(yaksu)