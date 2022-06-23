

def main():
    print(get_number([1,2,3,4,0]))
    print(get_number([6,10,2]))
    print(get_number([3, 30, 34, 5, 9]))
    print(get_number([9534330, 9534303]))

def get_number(numbers):
    ns = {str(i):str(i)*3 for i in numbers}
    sorted_dict = sorted(ns.items(),key = lambda item: item[1], reverse=True)
    result = ""
    for z, _ in sorted_dict:
        result += z
    return result




main()
