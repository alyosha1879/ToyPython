from multiprocessing import Pool, TimeoutError
import time

def f(x):
    result = x*x
    print(result)
    time.sleep(2)
    return result

if __name__ == '__main__':
    with Pool(processes=4) as pool:         # start 4 worker processes

        multiple_results = [pool.apply_async(f, ([i])) for i in range(10)]

        try:
            results = [res.get(timeout=1) for res in multiple_results]
        except TimeoutError:
            print("We lacked patience and got a multiprocessing.TimeoutError")

        pool.close()
        pool.join()
        print("all processes end.")
