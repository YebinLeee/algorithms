

def main():
    print(tie_number([1,2,3,4,0]) == 15)
    print(tie_number([-1,2,1,3]) == 6)
    print(tie_number([0,1,2,4,3,5]) == 27)
    print(tie_number([-1])==-1)
    print(tie_number([-1,0,1])==1)



def tie_number(numbers):
    result = 0
    plus = [ i for i in numbers if i>1] # 1 초과된 갯수만 리스트로 가져옴
    minus = [ i for i in numbers if i<=0] # 0 이하의 갯수만 리스트로 가져옴
    plus.sort(reverse=True) # plus 역순으로 정렬
    minus.sort() # minus는 그냥 정렬

    for i in range(0,len(plus), 2): # 2칸씩 넘기면서 수 묶기
        if i < len(plus)-1:
            result += plus[i] * plus[i+1]
            continue
        result += plus[i]

    for i in range(0,len(minus), 2): # 2칸씩 넘기면서 수 묶기
        if i < len(minus)-1:
            result += minus[i] * minus[i+1]
            continue
        result += minus[i]

    if 1 in numbers: # 1은 곱할필요없이 무조건 더하는게 이득이기 때문에 따로 뺀다
        result += 1
    return result


main()
