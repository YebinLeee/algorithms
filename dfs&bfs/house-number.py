

def main():
    result = get_house_number([
        [0,1,1,0,1,0,0],
        [0,1,1,0,1,0,1],
        [1,1,1,0,1,0,1],
        [0,0,0,0,1,1,1],
        [0,1,0,0,0,0,0],
        [0,1,1,1,1,1,0],
        [0,1,1,1,0,0,0]
    ])

    print(len(result))
    for r in result:
        print(r)

def get_house_number(numbers):
    result = []
    idx = 0
    for y in range(len(numbers)):
        for x in range(len(numbers)):
            if numbers[y][x] != 0:
                result.append(0)
                dfs(numbers,x,y, result, idx)
                idx = idx + 1
                
    return result

def dfs(map, x, y, result, idx):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    if isSafe(map, x, y,len(map),len(map)):
        return
    
    map[y][x] = 0
    result[idx] = result[idx] + 1
    for i in range(4):
        dfs(map, x + dx[i], y + dy[i], result, idx)

def isSafe(map, x, y, x_len, y_len):
    return x<0 or x>=x_len or y>=y_len or y<0 or map[y][x] == 0

main()
