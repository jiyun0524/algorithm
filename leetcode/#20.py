# -*- coding: utf-8 -*-
# @problem 20. Valid Parentheses
# @start   2022-02-09
# @submit  
# @comment 주어진 문자열에서 다음 괄호 ( ) { } [ ] 가 제대로 열리고 닫혔는지 boolean으로 표현

def isValid(s):
    if s[0] == '(':
        if(s[1] == ')'):
            return 'true'
        else:
            return 'false'
    elif s[0] == '{':
        if(s[1] == '}'):
            return 'true'
        else:
            return 'false'
    else:
        if(s[1] == ']'):
            return 'true'
        else:
            return 'false'

print(isValid('(]'));