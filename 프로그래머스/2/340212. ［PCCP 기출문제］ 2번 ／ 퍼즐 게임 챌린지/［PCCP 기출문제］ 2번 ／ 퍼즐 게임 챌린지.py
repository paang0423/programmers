def solution(diffs, times, limit):
    left, right = 1, max(diffs)
    
    while left <= right:
        mid = (left + right) // 2
        time = 0
        time_prev = 0
        
        for i in range(len(diffs)):
            if diffs[i] > mid:
                time_cur = times[i]
                wrong = diffs[i] - mid
                time += wrong * (time_cur + time_prev) + time_cur
            else:
                time_cur = times[i]
                time += time_cur
            time_prev = times[i]
        
        if time > limit:
            left = mid + 1
        else:
            right = mid - 1
    
    return left
