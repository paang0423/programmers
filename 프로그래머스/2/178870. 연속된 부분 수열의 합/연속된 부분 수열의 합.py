def solution(sequence, k):
    left = 0
    right = 0
    current_sum = sequence[0]
    answer = []
    min_length = float('inf')

    while right < len(sequence):
        if current_sum == k:
            if (right - left) < min_length:
                min_length = right - left
                answer = [left, right]
            current_sum -= sequence[left]
            left += 1
        elif current_sum < k:
            right += 1
            if right < len(sequence):
                current_sum += sequence[right]
        else:
            current_sum -= sequence[left]
            left += 1

    return answer
