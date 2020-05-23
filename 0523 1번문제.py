def solution(p):
    num = p
    while(True):
        num += 1
        num1 = num // 1000
        num2 = (num - num1*1000) // 100
        num3 = (num - num1*1000 - num2*100) // 10
        num4 =  num - num1*1000 - num2*100 - num3*10
        #print(num)
        #print(num1,num2,num3,num4)
        if(num1 != num2 and num1 != num3 and num1 != num4):
            if(num2 != num3 and num2 != num4):
                if(num3 != num4):
                    break

    return num