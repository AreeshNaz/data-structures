
def insertion():
    arr = [6, 5, 14, 3, 2, 11, 1]
    i = 1
    while i < len(arr):
        insert = arr[i] 
        j = i - 1
        
        while j >= 0 and arr[j] > insert:
            j -= 1
        
        arr.insert(j + 1, insert)  
        arr.pop(i + 1)  
        
        print(arr)
        i += 1

def selection():
    arr = [6, 5, 14, 3, 2, 11, 1]
    
    for i in range(len(arr)):
        min_idx = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
      
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
        print(arr, f"Pass {i+1}")

print("Insertion Sort:")
insertion()


print("\nSelection Sort:")
selection()
