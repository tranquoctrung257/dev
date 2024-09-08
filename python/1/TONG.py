
N,K = input().split()
    # Dòng thứ hai chứa dãy số
numbers = list(map(int,input().split()))

# Sắp xếp dãy số theo thứ tự giảm dần
numbers.sort(reverse=True)


result = sum(numbers[:int(K)])


print(result)