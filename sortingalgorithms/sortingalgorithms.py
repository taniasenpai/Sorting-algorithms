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


def merge_three(arr, left, mid1, mid2, right):
    left_arr = arr[left:mid1 + 1]
    mid_arr = arr[mid1 + 1:mid2 + 1]
    right_arr = arr[mid2 + 1:right + 1]

    i = j = k = 0
    index = left

    while i < len(left_arr) and j < len(mid_arr) and k < len(right_arr):
        if left_arr[i] <= mid_arr[j] and left_arr[i] <= right_arr[k]:
            arr[index] = left_arr[i]
            i += 1
        elif mid_arr[j] <= left_arr[i] and mid_arr[j] <= right_arr[k]:
            arr[index] = mid_arr[j]
            j += 1
        else:
            arr[index] = right_arr[k]
            k += 1
        index += 1

    while i < len(left_arr) and j < len(mid_arr):
        if left_arr[i] <= mid_arr[j]:
            arr[index] = left_arr[i]
            i += 1
        else:
            arr[index] = mid_arr[j]
            j += 1
        index += 1

    while j < len(mid_arr) and k < len(right_arr):
        if mid_arr[j] <= right_arr[k]:
            arr[index] = mid_arr[j]
            j += 1
        else:
            arr[index] = right_arr[k]
            k += 1
        index += 1

    while i < len(left_arr) and k < len(right_arr):
        if left_arr[i] <= right_arr[k]:
            arr[index] = left_arr[i]
            i += 1
        else:
            arr[index] = right_arr[k]
            k += 1
        index += 1

    while i < len(left_arr):
        arr[index] = left_arr[i]
        i += 1
        index += 1

    while j < len(mid_arr):
        arr[index] = mid_arr[j]
        j += 1
        index += 1

    while k < len(right_arr):
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

minRUN = 32
def calcMinRun(n):
    r = 0
    while n >= minRUN:
        r |= n & 1
        n >>= 1
    return n + r

def insertionSort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge1(arr, l, m, r):
    left = arr[l:m+1]
    right = arr[m+1:r+1]
    i = j = 0
    k = l
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

def findRun(arr, start, n):
    end = start + 1
    if end == n: return end
    if arr[end] < arr[start]:
        # descending
        while end < n and arr[end] < arr[end - 1]:
            end += 1
        arr[start:end] = reversed(arr[start:end])
    else:
        # ascending
        while end < n and arr[end] >= arr[end - 1]:
            end += 1
    return end

def timsort(arr):
    n = len(arr)
    minRun = calcMinRun(n)
    runs = []

    i = 0
    while i < n:
        runEnd = findRun(arr, i, n)
        runLen = runEnd - i

        if runLen < minRun:
            end = min(i + minRun, n)
            insertionSort(arr, i, end - 1)
            runEnd = end

        runs.append((i, runEnd))
        i = runEnd

        while len(runs) > 1:
            l1, r1 = runs[-2]
            l2, r2 = runs[-1]
            len1, len2 = r1 - l1, r2 - l2
            if len1 <= len2:
                merge1(arr, l1, r1 - 1, r2 - 1)
                runs.pop()
                runs[-1] = (l1, r2)
            else:
                break

    while len(runs) > 1:
        l1, r1 = runs[-2]
        l2, r2 = runs[-1]
        merge1(arr, l1, r1 - 1, r2 - 1)
        runs.pop()
        runs[-1] = (l1, r2)

        return arr;




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

def random_float_list(n):
    return [random.uniform(0, 100000) for _ in range(n)]


def sorted_float_list(n):
    return sorted(random_float_list(n))


def reverse_sorted_float_list(n):
    return sorted(random_float_list(n), reverse=True)


def random_string_list(n, length=5):
    letters = "abcdefghijklmnopqrstuvwxyz"
    return [
        ''.join(random.choice(letters) for _ in range(length))
        for _ in range(n)
    ]


def sorted_string_list(n):
    return sorted(random_string_list(n))


def reverse_sorted_string_list(n):
    return sorted(random_string_list(n), reverse=True)


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
    "Timsort": timsort
}

data_types = {
    # integers
    "Random": random_list,
    "Sorted": sorted_list,
    "Reverse": reverse_sorted_list,
    "AlmostSorted": almost_sorted_list,
    "FewUnique": few_unique_list,

    # floats
    "RandomFloat": random_float_list,
    "SortedFloat": sorted_float_list,
    "ReverseFloat": reverse_sorted_float_list,

    # strings
    "RandomString": random_string_list,
    "SortedString": sorted_string_list,
    "ReverseString": reverse_sorted_string_list
}

sizes = [20, 50, 100, 1000, 5000, 10000, 50000, 100000]


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

                # Counting & Radix ONLY for integers
                if algo_name in ["Counting", "Radix"] and "Float" in dtype_name:
                    continue
                if algo_name in ["Counting", "Radix"] and "String" in dtype_name:
                    continue

                # Bucket ONLY for floats (optional)
                if algo_name == "Bucket" and "Float" not in dtype_name:
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