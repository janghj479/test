#변수 선언 부분
money, c500, c100, c50, c10 = 0, 0, 0, 0, 0

#메인 코드 부분
money=int(input("교환할 돈은 얼마?"))

c500 = money // 50000
money %= 50000

c100 = money // 1000
money %= 10000

c50 = money // 5000
money %= 5000

c10 = money // 1000
money %= 1000

print("\n 50000원짜리 ==> %d장" %c500)
print(" 10000원짜리 ==> %d장" %c100)
print(" 5000원짜리 ==> %d장" %c50)
print(" 1000원짜리 ==> %d장" %c10)
print(" 바꾸지 못한 777777돈 ==> %d원 \n" %money)