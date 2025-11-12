def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Тестирование алгоритма
print("=== Тест 1 ===")
test1 = [5, 2, 9, 1, 5, 6]
print("До сортировки:", test1)
print("После сортировки:", bubble_sort(test1.copy()))

print("\n=== Тест 2 ===")
test2 = [3, 0, -1, 8, 7]
print("До сортировки:", test2)
print("После сортировки:", bubble_sort(test2.copy()))

print("\n=== Тест 3 ===")
test3 = [1]
print("До сортировки:", test3)
print("После сортировки:", bubble_sort(test3.copy()))