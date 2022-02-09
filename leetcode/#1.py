# -*- coding: utf-8 -*-
# @problem 1. Two Sum
# @date    2022-02-09
# @comment 입력 받은 배열의 요소들로 target에 해당하는 수를 만들려면 몇 번째 인덱스를 이용해야하는지 출력하는 문제
def twoSum(nums, target):
        for i in range(len(nums)):
            # 자기자신 외의 것을 더해야하기 때문에 i+1부터 시작하는 범위를 적용
            for j in range(i+1, (len(nums))):
                if(nums[i] + nums[j] == target):
                    return [i,j]

print(twoSum([2, 7, 11, 15], 9));