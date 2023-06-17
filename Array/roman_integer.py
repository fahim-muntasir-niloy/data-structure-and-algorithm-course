roman_num_dict = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000,
}

def roman_to_num(roman):
    int_num = 0
    nums = list(roman)
    for i in range(len(nums)):
        if roman_num_dict[i+1]<roman_num_dict[i]:
            int_num-=roman_num_dict[i]
        int_num+=roman_num_dict[i]
    return int_num
    
print(roman_to_num("MV"))