# 체육복 문제 재 도전 (테스트케이스 20/20 통과)

def main():
    print(solution(5,[2,3,4],[3,4,5])==4)
    print(solution(5, [2,4], [1,3,5])==5)
    print(solution(5, [2,4],[3])==4)
    print(solution(3,[3],[1])==2)
    
def solution(n, lost, reserve):
    answer = 0
    lent_numbers=[] # 빌린 학생의 번호
    
    # 오름차순 정렬
    lost.sort()
    reserve.sort()
    
    # lost, reserve 중복으로 포함된 학생 제거
    for number in lost:
        if number in reserve:
            lent_numbers.append(number)
            reserve.remove(number)
    
    # 빌릴 수 있는 학생 제거
    for number in lost:
        # 앞번호에게 빌리기
        if number-1 in reserve:
            if number not in lent_numbers:
                lent_numbers.append(number)
                lent_numbers.remove(number-1)               
        # 뒷번호에게 빌리기
        elif number+1 in reserve:
            if number not in lent_numbers:
                lent_numbers.append(number)
                reserve.remove(number+1) 
    
    answer = n-(len(lost)-len(lent_numbers))
    return answer

main()
