# 완주하지 못한 선수
# 미완 / 해쉬 사용해야함 !
def solution(participant, completion):
    for i in participant :
        if i not in completion :
            print(i)
    answer = ''
    return answer

participant = list(map(str, input().split( )))
completion = list(map(str, input().split( )))
solution(participant, completion)
