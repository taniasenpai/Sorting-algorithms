import random
import time
import csv
import copy

# -------------------------------
# Sorting Algorithms
# -------------------------------

def bubble_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def selection_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def python_sort(arr):
    return sorted(arr)

def merge_three(arr, left, mid1, mid2, right):
    left_arr = arr[left:mid1 + 1]
    mid_arr = arr[mid1 + 1:mid2 + 1]
    right_arr = arr[mid2 + 1:right + 1]

    i = j = k = 0
    index = left

    while i < len(left_arr) or j < len(mid_arr) or k < len(right_arr):
        min_value = float('inf')
        min_idx = -1

        if i < len(left_arr) and left_arr[i] < min_value:
            min_value = left_arr[i]
            min_idx = 0
        if j < len(mid_arr) and mid_arr[j] < min_value:
            min_value = mid_arr[j]
            min_idx = 1
        if k < len(right_arr) and right_arr[k] < min_value:
            min_value = right_arr[k]
            min_idx = 2

        if min_idx == 0:
            arr[index] = left_arr[i]
            i += 1
        elif min_idx == 1:
            arr[index] = mid_arr[j]
            j += 1
        else:
            arr[index] = right_arr[k]
            k += 1

        index += 1


def three_way_merge_sort(arr):
    a = arr.copy()

    def sort(a, left, right):
        if left >= right:
            return

        mid1 = left + (right - left) // 3
        mid2 = left + 2 * (right - left) // 3

        sort(a, left, mid1)
        sort(a, mid1 + 1, mid2)
        sort(a, mid2 + 1, right)

        merge_three(a, left, mid1, mid2, right)

    sort(a, 0, len(a) - 1)
    return a

def cycle_sort(arr):
    a = arr.copy()
    writes = 0

    for cycleStart in range(0, len(a) - 1):
        item = a[cycleStart]

        pos = cycleStart
        for i in range(cycleStart + 1, len(a)):
            if a[i] < item:
                pos += 1

        if pos == cycleStart:
            continue

        while item == a[pos]:
            pos += 1

        a[pos], item = item, a[pos]
        writes += 1

        while pos != cycleStart:
            pos = cycleStart
            for i in range(cycleStart + 1, len(a)):
                if a[i] < item:
                    pos += 1

            while item == a[pos]:
                pos += 1

            a[pos], item = item, a[pos]
            writes += 1

    return a

def heap_sort(arr):
    a = arr.copy()

    def heapify(a, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and a[l] > a[largest]:
            largest = l

        if r < n and a[r] > a[largest]:
            largest = r

        if largest != i:
            a[i], a[largest] = a[largest], a[i]
            heapify(a, n, largest)

    n = len(a)

    for i in range(n // 2 - 1, -1, -1):
        heapify(a, n, i)

    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        heapify(a, i, 0)

    return a

def counting_sort(arr):
    if len(arr) == 0:
        return arr

    a = arr.copy()
    max_val = max(a)
    min_val = min(a)

    range_of_elements = max_val - min_val + 1
    count = [0] * range_of_elements
    output = [0] * len(a)

    for num in a:
        count[num - min_val] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for num in reversed(a):
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1

    return output

def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for num in arr:
        index = (num // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    return output


def radix_sort(arr):
    a = arr.copy()

    if len(a) == 0:
        return a

    max_val = max(a)
    exp = 1

    while max_val // exp > 0:
        a = counting_sort_for_radix(a, exp)
        exp *= 10

    return a

def bucket_sort(arr):
    a = arr.copy()
    n = len(a)
    if n == 0:
        return a

    buckets = [[] for _ in range(n)]

    for num in a:
        index = int(num * n)
        if index == n:
            index = n - 1
        buckets[index].append(num)

    for i in range(n):
        buckets[i].sort()

    result = []
    for bucket in buckets:
        result.extend(bucket)

    return result


# -------------------------------
# Data Generators
# -------------------------------

def random_list(n):
    return [random.randint(0, 100000) for _ in range(n)]


def sorted_list(n):
    return list(range(n))


def reverse_sorted_list(n):
    return list(range(n, 0, -1))


def almost_sorted_list(n):
    arr = list(range(n))
    for _ in range(max(1, n // 50)):  # ~2%
        i, j = random.randint(0, n-1), random.randint(0, n-1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr


def few_unique_list(n):
    return [random.randint(0, 10) for _ in range(n)]


# -------------------------------
# Timing Function
# -------------------------------

def measure_time(sort_func, arr):
    start = time.perf_counter()
    sort_func(arr)
    end = time.perf_counter()
    return (end - start) * 1000  # ms


# -------------------------------
# Experiment Setup
# -------------------------------

sorting_algorithms = {
    "Bubble": bubble_sort,
    "Insertion": insertion_sort,
    "Selection": selection_sort,
    "Merge": merge_sort,
    "Quick": quick_sort,
    "Heap": heap_sort,
    "3-Way Merge": three_way_merge_sort,
    "Cycle": cycle_sort,
    "Counting": counting_sort,
    "Radix": radix_sort,
    "Bucket": bucket_sort,
    "Python": python_sort
}

data_types = {
    "Random": random_list,
    "Sorted": sorted_list,
    "Reverse": reverse_sorted_list,
    "AlmostSorted": almost_sorted_list,
    "FewUnique": few_unique_list
}

sizes = [20, 50, 100, 1000, 5000]


# -------------------------------
# Run Experiments
# -------------------------------

def run_experiments():
    results = []

    for size in sizes:
        for dtype_name, generator in data_types.items():
            print(f"\nSize={size}, Type={dtype_name}")

            # generate one dataset
            base_data = generator(size)

            for algo_name, algo_func in sorting_algorithms.items():

                # skip slow algorithms on large data
                if size > 1000 and algo_name in ["Bubble", "Insertion", "Selection", "Cycle"]:
                    continue

                # ❗ skip incompatible algorithms
                if algo_name == "Counting" and dtype_name != "Random":
                    continue

                if algo_name == "Radix" and dtype_name != "Random":
                    continue

                if algo_name == "Bucket" and dtype_name != "Random":
                    continue

                if algo_name == "Bucket":
                    continue

                data_copy = copy.deepcopy(base_data)
                time_taken = measure_time(algo_func, data_copy)

                print(f"{algo_name}: {time_taken:.3f} ms")

                results.append([algo_name, size, dtype_name, time_taken])

    return results


# -------------------------------
# Save Results
# -------------------------------

def save_results(results, filename="results.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Algorithm", "Size", "Type", "Time(ms)"])
        writer.writerows(results)


# -------------------------------
# Main
# -------------------------------

if __name__ == "__main__":
    results = run_experiments()
    save_results(results)
    print("\nResults saved to results.csv")