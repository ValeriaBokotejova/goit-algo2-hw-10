import random
import timeit
import statistics
from tabulate import tabulate
import matplotlib.pyplot as plt

def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr[:]
    pivot = random.choice(arr)
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return randomized_quick_sort(less) + equal + randomized_quick_sort(greater)

def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr[:]
    pivot = arr[len(arr)//2]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return deterministic_quick_sort(less) + equal + deterministic_quick_sort(greater)

def benchmark_sort(sort_func, data, repeats=5):
    stmt = lambda: sort_func(data)
    times = timeit.repeat(stmt, repeat=repeats, number=1)
    return statistics.mean(times)

def main():
    sizes = [10_000, 50_000, 100_000, 500_000]
    results = []

    for n in sizes:
        arr = [random.randint(0, n) for _ in range(n)]
        t_rand = benchmark_sort(randomized_quick_sort, arr)
        t_det = benchmark_sort(deterministic_quick_sort, arr)
        results.append((n, t_rand, t_det))
        print(f"Array size: {n}")
        print(f"  Randomized QuickSort: {t_rand:.4f} s")
        print(f"  Deterministic QuickSort: {t_det:.4f} s\n")

    # Table
    print("Summary:")
    print(tabulate(results,
                   headers=["Size", "Randomized (s)", "Deterministic (s)"],
                   tablefmt="pretty",
                   floatfmt=".4f",
                   numalign="center"))

    # Plot
    sizes, t_rand, t_det = zip(*results)
    plt.plot(sizes, t_rand, label="Randomized")
    plt.plot(sizes, t_det, label="Deterministic")
    plt.xlabel("Array Size")
    plt.ylabel("Time (s)")
    plt.title("QuickSort Variants Benchmark")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
