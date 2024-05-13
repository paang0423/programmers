def solution(food):
    answer = ''
    pair = ''
    num = []
    for i in range(1, len(food)) :
        num.append(food[i] // 2) 
    print(num)
    for i in range(0,len(num)) :
        pair += str(i+1)*num[i]
    return pair+'0'+pair[::-1]