def solution(price, money, count):
    price2 = 0
    i = 1
    for i in range(count+1) :
        price2 += price*i
    if money >= price2 :
        return 0
    else : 
        return abs(price2-money)