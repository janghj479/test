a=0
result = 0
i=0

a = int(input("시프트할 숫자는? "))

#if (sel==2) or (sel==8) or(sel==10) or(sel==16):

num=input("출력할 횟수는? ")

for i in range(1,int(num)+1):
    result=a<<i
    print("%d << %d = %d" %(a,i,result))
    
for i in range(1,int(num)+1):
    result=a>>i
    print("%d >> %d = %d" %(a,i,result))