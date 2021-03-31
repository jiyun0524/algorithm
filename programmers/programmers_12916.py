# 문자열 내 p와 y의 개수

s = 'PYY'
numP = 0
numY = 0

# for i in range(len(s)) :
#     if 'p' in s :
#         numP += 1
#     elif 'y' in s :
#         numY += 1


for i in s :
    if i == 'p' :
        numP += 1
    elif i == 'y' :
        numY += 1

print(numP, numY)

if numP == numY :
    print('앙')
else :
    print('홍')