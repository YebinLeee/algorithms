'''
현재의 노드가 4이고, 다음 수가 1이라고 치면, +1, -1 총 2가지의 경우가 있다. (인접 노드가 2개)

4 -> + 1 = 3
4 -> -1 = 2

따라서 n개의 노드가 존재할 때 뻗어나갈 수 있는 가지의 수는 2^n개 이다.
numbers = [4,1,2,1] 일때,
각 수에 +, -를 붙여 총 2^4 = 16가지의 경우의 수를 만들 수 있다.

1) [4, +1, +2, +1] -> 
2) [4, +1, +2, -1] -> 
3) [4, +1, -2, +1] ->
....
15)
16) [-4, -1, -2, -1] ->

'''

numbers = [4,1,2,1]
target = 3

def solution(numbers,target):
  answer = 0
  data = [] # 2^len(numbers)개의 결과 값들을 담은 리스트
  for i in numbers:
    sum = 0 # 각 수를 더한 값들
    for j in numbers:
      

  # 2^len(numbers)개의 결과 값들 중 target과 같으면 1 더함
  for d in data:
    if d==target:
      answer += 1
        
  return answer

def main():
    print(solution([4,1,2,1], 3)==2)
    print(solution([1,1,1,1,1],4)==2)
    
main()