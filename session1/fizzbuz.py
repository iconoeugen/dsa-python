# Solve https://leetcode.com/problems/fizz-buzz/

import sys

def getFizzBuzz(n:int) -> str:
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 5 == 0:
        return "Buzz"
    elif n % 3 == 0:
        return "Fizz"
    return str(n)

def createFizzBuzz(n: int) -> list[str]:
    resp = []
    for i in range(1, n+1):
        resp.append(getFizzBuzz(i))

    return resp

def main() -> int:
    """Echo the input arguments to standard output"""
    fizz_buzz = createFizzBuzz(20)
    print(fizz_buzz)
    return 0

if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit