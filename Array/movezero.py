nums = [0,4,3,0,12]

#  Brute Force Time complex method
def bad_moveZero(nums):
    count = 0
        
    for i,j in enumerate(nums):
        if j != 0:
            continue
        else:
            nums.remove(nums[i])
            count+=1
            
        while count !=0:
            nums.append(0)
            count-=1
            
    return nums


# Optimal Way
def moveZeroes(nums):
    s=0
    for i in range(len(nums)):
        
        if nums[i] != 0:
            nums[i], nums[s] = nums[s], nums[i]
            s+=1

    return nums 


print(moveZeroes(nums))