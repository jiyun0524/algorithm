# -*- coding: utf-8 -*-
# @problem 14. Longest Common Prefix
# @start   2022-02-09
# @submit  
# @comment 주어진 배열 내에서 공통되게 사용하는 문자를 출력(왼쪽부터)

def longestCommonPrefix(strs):
    answer = ''
    # 주어진 배열에 들어있는 요소의 갯수만큼 돌고
    for i in range (len(strs)):
        # 각 원소 중 가장 긴 것의 길이만큼
        for j in range (len(max(strs, key=len))):
            if(strs[i+1][j].startswith(strs[i][j])):
                answer = strs[i][j]
                return True
            else:
                return False
                        
print(longestCommonPrefix(["flower","flow","flight"]));