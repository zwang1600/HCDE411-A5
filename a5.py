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

print(len(cleaned_lst2))

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


# by_review_count = sorted(cleaned_lst,key=lambda item:item["review_count"],reverse=True)
# print(by_review_count[0]["review_count"])
# print(by_review_count[1]["review_count"])
# print(by_review_count[2]["review_count"])
# print(by_review_count[3]["review_count"])
# print(by_review_count[4]["review_count"])
# print(by_review_count[5]["review_count"])


