a,b = map(int, input().split( ))

b -= 45

if(b < 0) :
    a -= 1
    b += 60

    if(a<0) :
        a += 24
    print(a,b)

else :
    print(a,b)

# 반대로 45분을 더하는 코드
# b += 45

# if (b >= 60) :
#     a += 1
#     b -= 60
    
#     if (a>=24) :
#         a -= 24
#     print (a,b)

# else :
#     print(a,b)