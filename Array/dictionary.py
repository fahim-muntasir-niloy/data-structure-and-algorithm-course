country_map = {'BD':'Bangladesh',
               'IN':'India',
               'USA':'United States of America'}
language = {
    'BD':'Bangla',
    'USA':'Dollar',
    'UGANDA':'Dollar'
}

# getting keys -> same outputs
for i in country_map:
    print(i)

for i in country_map.keys():
    print(i)


# getting values -> same ouputs
for i in (country_map):
    print(country_map[i])

for i in country_map.values():
    print(i)


# To get both key and values
for i,j in country_map.items():
    print(i,j)