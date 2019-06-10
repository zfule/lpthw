# create a mapping of state to abbreviation
states = {
    '河北': '冀',
    '北京': '京',
    '天津': '津',
    '浙江': '浙',
    '上海': '沪'
}

# create a basic set of states and some cities in them
cities = {
    '津': '天津',
    '沪': '上海',
    '京': '北京',
}

# add some more cities
cities['浙'] = '南京'
cities['冀'] = '石家庄'

# print out some cities
print("-" * 10)
print("浙省有: ", cities['浙'])
print("冀省有: ", cities['冀'])

# print some states
print("-" * 10)
print("上海市的简称是: ", states['上海'])
print("北京市的简称是: ", states['北京'])

# do it by using the state then cities dict
print("-" * 10)
print("上海市有: ", cities[states['上海']] )
print("北京市有: ", cities[states['北京']])

# print every state abbreviation
print("-" * 10)
for state, abbrev in list(states.items()):
    print(f"{state} 简称是 {abbrev}")

# print every city in state
print("-" * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} 有 {city}")

# now do both at the same time
print("-" * 10)
for state, abbrev in list(states.items()):
    print(f"{state} 简称是 {abbrev}")
    print(f"这还有{cities[abbrev]}市")

print("-" * 10)
# safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is : {city}")
