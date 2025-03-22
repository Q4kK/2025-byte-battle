def main():
    # array input
    print("how many rows? ")
    rows = int(input())
    arr = []
    for i in range(rows):
        arr.append(input().split())
    print(checkArr(arr))

def checkArr(arr):
    for i in range(len(arr) - 1):
        r1 = i
        r2 = i + 1
        for j in range(len(arr[i]) - 1):
            c1 = j
            c2 = j + 1
            while c2 < len(arr[i]):
                c2 += 1
                if (arr[r1][c1] + arr[r2][c2]) >= (arr[r2][c1] + arr[r1][c2]):
                    return False
        while r1 < len(arr[i]):
            if (arr[r1][c1] + arr[r2][c2]) >= (arr[r2][c1] + arr[r1][c2]):
                return False
            r2 += 1
            
    return True

main()