def firstInd(A, left, right, C):
    if left <= right:
        mid = left + (right - left) // 2

        if (mid == left or A[mid - 1] < C) and A[mid] == C:
            return mid
        elif A[mid] < C:
            return firstInd(A, mid + 1, right, C)
        else:
            return firstInd(A, left, mid - 1, C)

    return -1  

def lastInd(A, left, right, C):
    if left <= right:
        mid = left + (right - left) // 2

        if (mid == right or A[mid + 1] > C) and A[mid] == C:
            return mid
        elif A[mid] <= C:
            return lastInd(A, mid + 1, right, C)
        else:
            return lastInd(A, left, mid - 1, C)

    return -1  


A = [1, 2, 2, 2, 3, 4, 5]
C = 2
index1 = firstInd(A, 0, len(A) - 1, C)
index2 = lastInd(A, 0, len(A) - 1, C)

print(f"Chỉ số đầu tiên của {C} là: {index1}")
print(f"Chỉ số cuối cùng của {C} là: {index2}")
