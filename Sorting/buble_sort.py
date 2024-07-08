A = [64, 25, 12, 22, 11]
n =len(A)
def bubble(A):
    for i in range(len(A)):
        swapped = False
        for j in range(0,n-i-1):
            if A[j] > A[j-1]:
                A[j], A[j+1] = A[j+1], A[j]
                swapped = True
        if swapped == False:
            break
print(A)
bubble(A)
print(A)