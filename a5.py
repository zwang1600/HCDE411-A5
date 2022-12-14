import json

# Load data
lst = []
filename = 'yelp_academic_dataset_business.json'
with open(filename, 'r') as f:
    for line in f:
        data = json.loads(line)
        lst.append(data)

print(len(lst)) # should be 150346 rows

# CLean data so that:
#   Only places in the US are considered
#   Only resturants are considered
cleaned_lst = []
for item in lst:
    if (item['state'] is None or item['state'] == 'AB' or item['state'] == 'XMS' or 
       item['categories'] is None or 'Restaurant' not in item['categories']):
        continue
    else:
        cleaned_lst.append(item)

print(len(cleaned_lst)) # should be 49875 rows

# CLean data so that the "categories" column only include one of the following:
# Japanese
# Chinese
# Italian
# Fast food
# Vietnamese
# Thai
# Mexican
# Caribbean
# Cajun/Creole
# Mediterranean
# American (Traditional)

cleaned_lst2 = []
for item in cleaned_lst:
    if 'Chinese' in item['categories']:
        item['categories'] = 'Chinese'
        cleaned_lst2.append(item)
    elif 'Japanese' in item['categories']:
        item['categories'] = 'Japanese'
        cleaned_lst2.append(item)
    elif 'Italian' in item['categories']:
        item['categories'] = 'Italian'
        cleaned_lst2.append(item)
    elif 'Fast Food' in item['categories']:
        item['categories'] = 'Fast Food'
        cleaned_lst2.append(item)
    elif 'Vietnamese' in item['categories']:
        item['categories'] = 'Vietnamese'
        cleaned_lst2.append(item)
    elif 'Thai' in item['categories']:
        item['categories'] = 'Thai'
        cleaned_lst2.append(item)
    elif 'Mexican' in item['categories']:
        item['categories'] = 'Mexican'
        cleaned_lst2.append(item)
    elif 'Caribbean' in item['categories']:
        item['categories'] = 'Caribbean'
        cleaned_lst2.append(item)
    elif 'Cajun/Creole' in item['categories']:
        item['categories'] = 'Cajun/Creole'
        cleaned_lst2.append(item)
    elif 'Mediterranean' in item['categories']:
        item['categories'] = 'Mediterranean'
        cleaned_lst2.append(item)
    elif 'American' in item['categories']:
        item['categories'] = 'American'
        cleaned_lst2.append(item)

print(len(cleaned_lst2)) # should be 31619 rows

outputfilename = "cleaned_dataset.csv"
f = open(outputfilename,'w')
f.write("Name, City, State, Stars, Category, Review Count\n")
for item in cleaned_lst2:
    f.write("%s, %s, %s, %s, %s, %d\n"%(item["name"], item["city"], item["state"], item["stars"], item["categories"], item["review_count"]))

# Group by state
# The dict should be like this:
# {
#   'AZ': [3.00, 3.25, 5.00, ...],
#   'CA': [3.50, 4.00, 3.00, ...],
#   'ID': [4.00, 4.00, 3.00, ...],
#   'PA': [2.00, 5.00, 4.00, ...],
#   ...
# }
by_state_dictionary = {}
for item in cleaned_lst:
    state = item['state']
    if state not in by_state_dictionary:
        by_state_dictionary[state] = []
    by_state_dictionary[state].append(item['stars'])

print(by_state_dictionary.keys())

# Check for the number of resturants in each state
for key in by_state_dictionary.keys():
    print("%s: %d"%(key, len(by_state_dictionary[key])))
# Because NC, CO, HI, and MT only have one entry, we will exclude them
del(by_state_dictionary['NC'])
del(by_state_dictionary['CO'])
del(by_state_dictionary['HI'])
del(by_state_dictionary['MT'])

# Calculate the average rate by state
sum_of_rating_by_state = {}
for key in by_state_dictionary:
    sum_of_rating_by_state[key] = 0
    for entry in by_state_dictionary[key]:
        sum_of_rating_by_state[key] += entry

# Output to file
outputfilename = "average_star_by_state.csv"
f = open(outputfilename,'w')
for state in sum_of_rating_by_state:
    f.write("%s, %f\n"%(state, sum_of_rating_by_state[state] / len(by_state_dictionary[state])))
f.close()

# Calculate the star count by state
star_count_by_state = {}
for key in by_state_dictionary:
    star_count_by_state[key] = {'1.0':0, '1.5':0, '2.0':0, '2.5':0, '3.0':0, '3.5':0, '4.0':0, '4.5':0, '5.0':0}
    for entry in by_state_dictionary[key]:
        star_count_by_state[key][str(entry)]+=1

# Output to file
outputfilename = "num_of_stars_by_state.csv"
f = open(outputfilename,'w')
f.write("State, Total_Rating, Rating_1, Rating_1.5, Rating_2, Rating_2.5, Rating_3, Rating_3.5, Rating_4, Rating_4.5, Rating_5\n")
for state in star_count_by_state:
    f.write("%s, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d\n"%(state,
    len(by_state_dictionary[state]),
    star_count_by_state[state]['1.0'],
    star_count_by_state[state]['1.5'],
    star_count_by_state[state]['2.0'],
    star_count_by_state[state]['2.5'],
    star_count_by_state[state]['3.0'],
    star_count_by_state[state]['3.5'],
    star_count_by_state[state]['4.0'],
    star_count_by_state[state]['4.5'],
    star_count_by_state[state]['5.0']))
f.close()