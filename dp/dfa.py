def solution(N, number):
  dp = [[] for _ in range(9)] # N 사용 횟수에 대한 DP테이블
  dp[1].append(N) # 1번 사용
  
  # 2번~8번 사용
  for i in range(2, 9):
    # i : number 사용 횟수
    dp[i].append(int(str(N)*i)) # 5, 55, 555, (N을 이어붙인 수)

    # dp[i-1]과 dp[i]에 대한 연산
    for j in dp[i-1]:
      # 덧셈
      dp[i].append(j+N)
      # 곱셈
      dp[i].append(j*N)
      # 나눗셈
      dp[i].append(j//N)
      if j>0:
        dp[i].append(N//j)
      # 뺄셈
      dp[i].append(j-N)
      dp[i].append(N-j)

    if number in dp[i]:
      # print(dp[i])
      answer = i
      return answer

  answer = -1
  return answer


print(solution(5,12)) # 5로 12 만들기 ((55+5)/5)
print(solution(2,11)) # 2로 11 만들기 ( 22/2 )
print(solution(2, 111))