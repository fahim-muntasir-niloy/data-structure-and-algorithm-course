import time
a = time.time()

# def add(n):
#     sum =0
#     for i in range(0,n):
#         sum += i
        
#     return sum                # O(n)

def sum(n):
    return n*(n+1)/2            # O(1)


print(sum(232424))
b = time.time()
print(b-a)