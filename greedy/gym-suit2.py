# 체육복 문제 재 도전 (테스트케이스 9/10 통과)

def solution(n, lost, reserve):
    answer = 0
    list=[] # 빌린 학생의 번호
    
    # lost, reserve 중복 제거
    for i in lost:
        if i in reserve:
            list.append(i)
            del reserve[reserve.index(i)]
    
    # 빌려줄 수 있는 학생
    for i in lost:
        # 앞번호에게 빌리기
        if i-1 in reserve:
            if i not in list:
                list.append(i)
                del reserve[reserve.index(i-1)]
        # 뒷번호에게 빌리기
        elif i+1 in reserve:
            if i not in list:
                list.append(i)
                del reserve[reserve.index(i+1)] 
    
    answer = n-(len(lost)-len(list))
    return answer