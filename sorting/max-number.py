

def main():
    print(get_number([1,2,3,4,0]))
    print(get_number([6,10,2]))
    print(get_number([3, 30, 333, 303, 392]))
    print(get_number([0,0,1]))

def get_number(numbers):
    ns = [str(i)*3 for i in numbers]
    result = ""
    ns.sort(reverse=True)
    for n in ns:
        for i in range(int(len(ns)/3)):
            result += n[i]
    return result




main()
