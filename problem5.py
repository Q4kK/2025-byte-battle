import math

def main():
    numbers = input()
    numarr = numbers.split()
    num1 = int(numarr[0])
    num2 = int(numarr[1])


    output = int(math.log(num2, 2) - math.log(num1, 2))
    if 2 ** int(math.log(num1, 2)) == num1:
        output += 1
    print(output)

main()