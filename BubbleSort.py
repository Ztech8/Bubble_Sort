def mysort(n):
    for i in range(len(n)):
        for j in range(i + 1, len(n)):
            if n[i] > n[j]:
                n[i], n[j] = n[j], n[i]


numbers = [10, 3, 7, 8, 4, 2, 5, 6, 1, 9]
mysort(numbers)
print(numbers)
