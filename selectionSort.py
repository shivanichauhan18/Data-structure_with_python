A = [64, 25,6,44,0, 12, 22, 11] 
  
for i in range(len(A)-1): 
    min_idx = i 
    for j in range(i+1, len(A)): 
        if A[min_idx] > A[j]: 
            min_idx = j 

    A[i], A[min_idx] = A[min_idx], A[i]
print A

def selection_sort(L):
    # i indicates how many items were sorted
    for i in range(len(L)-1):
        min_index = i
        for j in range(i+1, len(L)-1):
            # Update the min_index if the element at j is lower than it
            if L[j] < L[min_index]:
                min_index = j
        L[i], L[min_index] = L[min_index], L[i]

L = [3, 1, 41, 59, 26, 53, 59]
print(L)
selection_sort(L)
print(L)