print("======================== Recursion ========================")


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(7))

print("======================== Fibonacci Sequence ========================")


def fibonacciSeries(n, first=0, next=1):
    if n <= 0:
        return []
    else:
        result = [first] + fibonacciSeries(n - 1, next, first + next)
        return result


series = fibonacciSeries(5)
for number in series:
    print(number,end=" ")
