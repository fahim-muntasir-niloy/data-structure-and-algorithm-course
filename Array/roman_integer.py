

def roman_to_num(s):
    roman_num_dict = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000,
}
    
    int_num = 0
    e = len(s)-1
    
    for i in range(e):
        
        """ with this method, we are excluding the last digit. 
        Which is later added 
        in the return statement."""
        
        if(roman_num_dict[s[i]] < roman_num_dict[s[i+1]]):
            int_num -= roman_num_dict[s[i]]
            
        else:
            int_num+=roman_num_dict[s[i]]
        
        
    return int_num+roman_num_dict[s[-1]]
        
    
print(roman_to_num("III"))