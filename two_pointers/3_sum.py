# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.


nums = [-1,0,1,2,-1,-4]


def threeSum(nums):
    nums.sort()
    result = []
    
    # returning empty list it there are less than 3 digits.
    if len(nums) < 3:
        return result

    else:
        
        # if two immediate values are equal, 
        # we dont include in the solution.
        
        for i,j in enumerate(nums):
            if i > 0 and j == nums[i-1]:
                continue
            
            # As we fix the first value {j}, 
            # we select the later two as the first and last item of the
            # rest of the array.
            
            s,e = i+1, len(nums)-1
            
            # this part is identical to the two-sumII problem, 
            # pointers are changed based on the sum
            
            while s<e :
                threesum = j + nums[s] + nums[e]

                if threesum < 0:
                    s+=1
                elif threesum > 0:
                    e-=1 
                else:
                    result.append([j,nums[s],nums[e]])
                    s+=1
                    
                    # Update the pointer once more, 
                    # if immediate values match
                    
                    while s<e and nums[s]==nums[s-1]:
                        s+=1
                        
    return result

print(threeSum(nums))