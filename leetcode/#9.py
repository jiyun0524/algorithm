# -*- coding: utf-8 -*-
# @problem 9. Palindrome Number
# @date    2022-02-09
# @comment 121과 같이 앞/뒤에서 읽어도 같은 숫자인지 판별하기
def isPalindrome(x):
        if(x<0): # 음수 일 경우 항상 실패 값을 반환
            return False
        else:
            return x == int(str(x)[::-1])

# (+)
# @date    2022-02-09
# @comment 기존의 풀이를 아래와 같이 줄여서 작성 가능
def isPalindrome(x):
    return False if x < 0 else x == int(str(x)[::-1])

print(isPalindrome(121));
print(isPalindrome(-121));
print(isPalindrome(10));
print(isPalindrome(1234567654321));