def in_asc_order(arr,a):
    is_ascending = True
    for i in range(a - 1):
        if arr[i] > arr[i + 1]:
            is_ascending = False
            break
    
    return is_ascending

sequences = [
    [1, 2, 4, 7, 19],
    [1, 2, 3, 4, 5],
    [1, 6, 10, 18, 2, 4, 20],
    [9, 8, 7, 6, 5, 4, 3, 2, 1]
]
    
for seq in sequences:
    result = in_asc_order(seq, len(seq))
    print(f"Послідовність {seq} у порядку зростання: {result}")
