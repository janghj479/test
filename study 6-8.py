#전역 변수 선언 부분
i,k=0,0

#메인 코드 부분
i=0
for i in range(1,10):
    if i < 5:
        k=0
        for k in range(0,5-i):
            print(' ',end='')
            k+=1
        k=0
        for k in range(0,i*2-1):
            print('\u2665',end='')
            k+=1
            
    else:
        k=0
        for k in range(0,i-5):
            print(' ',end='')
            k+=1
        k=0
        for k in range(0,(9-i)*2+1):
            print('\u2665',end='')
            k+=1
    print()
    i+=1
            