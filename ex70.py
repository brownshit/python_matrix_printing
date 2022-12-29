#2차원 리스트 함수에 전달하기.
def getMat():
    matrix = []
    numofR = eval(input("row num input : "))
    numofC = eval(input("column num input : "))

    for row in range(numofR):
        matrix.append([])
        for col in range(numofC):
            value = eval(input("input val, and press enter : "))
            matrix[row].append(value)
    return matrix

def accumulate(m):      #축적...    all ele in matrix sum.
    total = 0
    for row in m:
        total += sum(row)
    return total

def main():
    m = getMat()
    #print matrix by structure...    아래의 구문은 그냥 익숙해지는게 나을거 같다.
    for r in m:
        for v in r:
            print(v, end=" ")
        print()

    print(" sum of matrix : ",accumulate(m))
    
main()