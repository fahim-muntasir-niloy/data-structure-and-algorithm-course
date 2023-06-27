# Remove Duplicates from Sorted Array

# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

nums = [1,1]

def removeDuplicates(nums) -> int:
    digits = []

    for num in nums:
        if num not in digits:
            digits.append(num)

    nums = list(digits)
    k = len(nums)

    return k, nums

print(removeDuplicates(nums))


# solution 2 -> as leetcode is being an ass
nums = [1,1]

def rmvDups(nums):
    i,j=0,1
    while i<=j and j<len(nums):
        if nums[i]==nums[j]:
            j+=1
        else:
            nums[i+1]=nums[j]
            i+=1
    return i+1
    
print(rmvDups(nums))