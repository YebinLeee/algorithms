'''
문제 조건
- 바로 앞번호 학생, 바로 뒷번호 학생에게만 체육복 빌려줄 수 있음
- 체육복을 적절히 빌려, 최대한 많은 학생이 체육 수업을 들어야 함

- n: 전체 학생수 (2<=n<=30)
- lost 배열: 도난단한 학생들 번호 (1<=len(lost)<=n)
- reserve: 여벌 체육복 있는 학생들 번호 (1<=len(reserve)<=n)

* 여벌 체육복 가져온 학생이 체육복을 도난 당할 수도 있다
   -> lost, reserve의 번호 중복 가능

solution 함수 작성
- 체육 수업 들을 수 있는 학생 최댓값 return



문제 해결 아이디어
1) 정렬
2) lost와 reserve 중복되는 것 먼저 제거
3) lost에 남은 학생 번호 -> reserve에서 빌려줄 수 있다면 제거


- flag 리스트: reserve 리스트의 학생이 빌려줄 수 있는 상태인지 체크

- 전체 학생 리스트를 훑어 가면서 잃어버린 학생 리스트 lost에 포함되어 있는지 먼저 확인
- 여분 리스트 reserve에서 빌려줄 수 있는지 상태 확인

'''

def solution():
  # 학생 번호 배열
  list = [i for i in range(N)]
  
  # reserve 값에 대한 0, 1값 (이미 빌려준 경우라면 1로 변경)
  flag = [0 for _ in range(N)]
  
  cnt = 0
  
  for n in list:
    # lost 배열에 포함되어 있는 경우라면
    if n+1 in lost:
      # reserve 배열에서 빌려줄 옆 학생이 있는지 확인
      # 앞번호 학생에게 받기
      if n in list and n in reserve and n not in lost:
        if flag[n]==0:
          flag[n] = 1
          cnt +=1
      # 다음 번호 학생에게 받기
      elif n+2 in list and n+2 in reserve and n+2 not in lost:
        if flag[n+2]==0:
          flag[n+2] = 1
          cnt+=1
    # lost와 reserve에 모두 포함된 학생 고려
    else:
      cnt+=1
  return cnt


N = int(input())
lost = list(map(int, input().split()))
reserve = list(map(int, input().split()))
print(solution())