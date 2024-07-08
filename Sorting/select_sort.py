A = [64, 25, 12, 22, 11]
def select_sort(A):
    for i in range(len(A)-1):
        min_indx = i
        for j in range(i+1, len(A)):
            if A[min_indx] > A[j]:
                min_indx = j
        A[i], A[min_indx] = A[min_indx], A[i]
print(A)
select_sort(A)
print(A)