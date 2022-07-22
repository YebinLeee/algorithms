def solution(N, number):
    dp = [{N}]  # dp 리스트 (먼저 N을 삽입)
    if N==number: 
      return 1
      
    for i in range(1,9):
        # i : number 사용 횟수
        arr = [int(str(N)*(i+1))] # 5, 55, 555, (N을 이어붙인 수)
        
        # dp[j]과 dp[i-j]에 대한 연산
        for j in range(0, i//2+1):
            for k in dp[j]:
                for m in dp[i-j-1]:
                    arr.append(k+m)
                    arr.append(k-m)
                    arr.append(m-k)
                    arr.append(k*m)
                    if m!=0:
                        arr.append(k//m)
                    if k!=0:
                        arr.append(m//k)
        dp.append(set(arr))

        if number in set(arr):
            return i+1
        
    return -1