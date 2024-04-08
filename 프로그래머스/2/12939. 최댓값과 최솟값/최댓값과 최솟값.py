def solution(s):
    s2 = list(map(int,s.split()))
    s_min = min(s2)
    s_max = max(s2)
    return str(s_min)+' '+str(s_max)