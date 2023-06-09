# Set method

# def isAnagram(s,t):
#     s_set = set()
#     whole_set = set()
    
#     if s == t:
#         return True
#     elif t<s:
#         return False
#     else:
#         for i in s:
#             s_set.add(i)
#             whole_set.add(i)
            
#         for i in t:
#             whole_set.update(i)

        
#         return s_set, whole_set, len(s_set)==len(whole_set)

            

# More efficient way, may be the correct way as well

def count_dict(lst):
    dict_item = {item: (lst.count(item)) for item in lst}
    return dict_item


def isAnagram(s,t):
    return count_dict(s) == count_dict(t)
      
          
print(isAnagram("anagram","engreji"))
