A = int(input())
B = int(input())
C = int(input())

totalList = list(str(A*B*C))
for i in range(10) :
    # count를 사용하여 리스트에 문자가 몇 개씩 있는지 print
    print(totalList.count(str(i))) 
