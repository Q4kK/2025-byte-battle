import math

def isPrime(num):
    if num == 2 or num == 1:
        return True
    if num%2 == 0:
        return False
    i = 3
    end = math.sqrt(num)
    while (i < end):
        if num%i == 0:
            return False
        i += 2

    return True


def main():
    digit = input()
    window_size = len(digit)
    primes = []
    while window_size >= 0:
        for i in range(len(digit) - window_size):
            num = int(digit[i:i + window_size + 1])
            if isPrime(num):
                primes.append(num)
        if len(primes) > 0:
            print(max(primes))
            break
        window_size -= 1

main()