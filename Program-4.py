def cnt_of_multiples(arr):
    dict = {i: 0 for i in range(1, 10)}
    for n in arr:
        for i in range(1, 10):
            if n % i == 0:
                dict[i] += 1
    return dict

arr = [12, 15, 20, 9, 10, 27, 8, 14, 18, 7]
arr2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(cnt_of_multiples(arr))
print(cnt_of_multiples(arr2))