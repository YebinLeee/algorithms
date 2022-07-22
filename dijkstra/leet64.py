def solution(m,n,grid):
# 오른쪽과 아래로만 이동 가능하므로 0번 row, col은 각각 더해줌
  # 첫번째 col 채우기
  for i in range(1, m):
    grid[i][0] += grid[i-1][0]
  # 첫번째 row 채우기
  for i in range(1, n):
    grid[0][i] += grid[0][i-1]

  print(grid)

  # [0,0]부터 [m-1,n-1]까지 left, up중에서 오는 것중 작은 것을 선택하여 더한 결과값을 저장
  for i in range(1,m):
    for j in range(1,n):
      grid[i][j] += min(grid[i-1][j], grid[i][j-1])
      # print(i,j,grid[i][j])

  # print(grid)
  return grid[m-1][n-1]


# m x n grid
print(solution(2,3,[[1,2,3],[4,5,6]]))
print(solution(3,3,[[1,3,1],[1,5,1],[4,2,1]]))