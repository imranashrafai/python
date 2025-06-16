print("======================== Multi Threading ========================")
import threading
import time
from concurrent.futures import ThreadPoolExecutor


def func_for_threading(seconds):
    print(f"Function is done by {seconds} seconds.")
    time.sleep(seconds)


def main():
    ti = time.perf_counter()

    t1 = threading.Thread(target=func_for_threading, args=[4])
    t2 = threading.Thread(target=func_for_threading, args=[3])
    t3 = threading.Thread(target=func_for_threading, args=[1])
    t1.start()
    t2.start()
    t3.start()
    tf = time.perf_counter()
    totalTime = tf - ti
    print(totalTime)


# threadpool excutor
def poolDemo():
    print("=================Using Manually Method====================")

    with ThreadPoolExecutor() as ex:
        f1 = ex.submit(func_for_threading, 5)
        f2 = ex.submit(func_for_threading, 4)
        f3 = ex.submit(func_for_threading, 3)
        # print returned value of that function on which we apply ThreadPoolExecutor
        print(f1.result())
        print(f2.result())
        print(f3.result())


poolDemo()


def poolDemowithMapfunc():
    print("=================Using Map Function====================")
    with ThreadPoolExecutor() as ex:
        l = [1, 4, 5, 8, 9]
        results = ex.map(func_for_threading, l)
        for result in results:
            print(result)


poolDemowithMapfunc()
