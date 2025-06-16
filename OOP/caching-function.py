print("======================== Caching Function ========================")
from functools import lru_cache
import time

# mostly it used in fetching Data from database and in APIs


@lru_cache(maxsize=None)
def fx(n):
    time.sleep(3)
    return n * 3


@lru_cache(maxsize=None)
def table(n):
    time.sleep(3)
    result = []
    for i in range(11):
        result.append(f"{n} * {i+1} = {n*(i+1)}")
    return "\n".join(result)


# when a value is already calculated then it cache and show when it gtake that input
print(fx(3))
print(fx(4))
print(fx(5))
print(fx(7))
# it will load quickly because it already calculated stored in cache
print(fx(3))
print(fx(4))
print(f"Table of 2 is:\n{table(2)}")

print(f"Table of 4 is:\n{table(4)}")

print(f"Table of 2 is:\n{table(2)}")
