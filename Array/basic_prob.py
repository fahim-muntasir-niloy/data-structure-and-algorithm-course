# get minimum and maximum values from a list.

# The python way
a_list = [5,23,2,1,56,12,7,2,1,75]

a_list.sort()   # sorting the list from minimum to maximum
print(a_list[0])   # returns the first item of the list, which is the minimum value
print(a_list[-1])   # returns the last item of the list, which is the maximum value


# the interview way
blank_set = set()

for i,j in enumerate(a_list):
    blank_set.add(j)

print(list(blank_set))  # converting the set into list, and same result can be obtained as before.

