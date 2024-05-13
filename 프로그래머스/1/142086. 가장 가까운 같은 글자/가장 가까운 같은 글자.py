def solution(s):
    answer = [-1] * len(s)
    for i in range(len(s)):
        if s[i] in s[:i]:
            answer[i] = i - s[:i].rfind(s[i])
    return answer