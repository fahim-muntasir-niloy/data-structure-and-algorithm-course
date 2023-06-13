
nums = [1,2,3,4,5,3,1,2,4,5]
k = 2

counter=dict()

for i,j in enumerate(nums):
    for j in nums:
        counter.update({j:nums.count(j)})

print(counter)

counter_sorted = sorted(counter.items(), key= lambda x: x[1], reverse=True)

print(list(dict(counter_sorted).keys())[:k])
