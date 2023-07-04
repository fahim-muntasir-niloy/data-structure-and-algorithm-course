height = [1,8,6,2,5,4,8,3,7]
# max(height)
def maxArea(height):
    for i, j in enumerate(height):
        area = i*j
        print(f"{i}__{j}____{area}")
    
    
print(max(height))