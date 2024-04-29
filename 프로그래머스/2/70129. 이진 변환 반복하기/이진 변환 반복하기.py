def solution(s):
    cnt, count = 0, 0
    while s != '1' :
        count += s.count('0')
        s = s.replace('0', '')
        s = bin(len(s))[2:]
        cnt += 1
    return [cnt, count]