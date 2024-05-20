def solution(k, tangerine):
    answer = 0
    count = [0] * (max(tangerine) + 1)
    for size in tangerine:
        count[size] += 1
    sorted_count = sorted(count, reverse=True)
    for freq in sorted_count:
        k -= freq
        answer += 1
        if k <= 0:
            break
    return answer
