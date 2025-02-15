def merge(lA, rA):
    final = []
    i = 0
    j = 0
    
    # Merge both lists
    while i < len(lA) and j < len(rA):
        if lA[i] < rA[j]:
            final.append(lA[i])
            i += 1
        else:
            final.append(rA[j])
            j += 1

  
    final.extend(lA[i:])
    final.extend(rA[j:])
    
    return final

def mergeSort(arr):
    size = 1
    while size < len(arr):
        for i in range(0, len(arr), size * 2):
            left = arr[i:i + size]
            right = arr[i + size:i + size * 2]
            merged = merge(left, right)
            arr[i:i + len(merged)] = merged
        size *= 2
    return arr

arr = [10, 3, 5, 6, 7, 2, 4, 11]
print(mergeSort(arr))
