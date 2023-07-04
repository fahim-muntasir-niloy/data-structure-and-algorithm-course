word = "[{(}]"

# This is surprisingly a solution to a great extent. 
# This passed 85/93 testcases in Leetcode.
# However this is not the correct approach

# if word.count("(") == word.count(")") and word.count("{") == word.count("}") and word.count("[") == word.count("]"):
#     print(True)
# else:
#     print(False)
    

# Lets use stack
stack = []
parentheses_Map = {
    ")":"(",
    "}":"{",
    "]":"["
}
def val_par(word):
    for p in word:
        if p in parentheses_Map.values():
            stack.append(p)
            
        elif stack and parentheses_Map[p] == stack[-1]:
            stack.pop()
            
        else:
            return False
            
    return stack == []

print(val_par(word))