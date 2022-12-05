import json

# Load data
lst = []
filename = 'yelp_academic_dataset_business.json'
with open(filename, 'r') as f:
    for line in f:
        data = json.loads(line)
        lst.append(data)

cleaned_lst = []
for item in lst:
    if (item['state'] is None or item['state'] == 'AB' or item['state'] == 'XMS' or 
       item['categories'] is None or 'Restaurant' not in item['categories']):
        continue
    else:
        cleaned_lst.append(item)

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

by_state_dictionary = {}
for item in cleaned_lst2:
    state = item['state']
    cuisine = item['categories']
    if state not in by_state_dictionary:
        by_state_dictionary[state] = {}
    if cuisine not in by_state_dictionary[state]:
        by_state_dictionary[state][cuisine] = {'1.0':0, '1.5':0, '2.0':0, '2.5':0, '3.0':0, '3.5':0, '4.0':0, '4.5':0, '5.0':0}
    by_state_dictionary[state][cuisine][str(item['stars'])] += 1

# del(by_state_dictionary['NC'])
# del(by_state_dictionary['CO'])
# del(by_state_dictionary['HI'])
# del(by_state_dictionary['MT'])

# Output to file
outputfilename = "by_state_and_by_cuisine.csv"
f = open(outputfilename,'w')
f.write("State, Cuisine, Rating_1, Rating_1.5, Rating_2, Rating_2.5, Rating_3, Rating_3.5, Rating_4, Rating_4.5, Rating_5\n")
for state in by_state_dictionary:
    for cuisine in by_state_dictionary[state]:
        f.write("%s, %s, %d, %d, %d, %d, %d, %d, %d, %d, %d\n"%(
        state,
        cuisine,
        by_state_dictionary[state][cuisine]['1.0'],
        by_state_dictionary[state][cuisine]['1.5'],
        by_state_dictionary[state][cuisine]['2.0'],
        by_state_dictionary[state][cuisine]['2.5'],
        by_state_dictionary[state][cuisine]['3.0'],
        by_state_dictionary[state][cuisine]['3.5'],
        by_state_dictionary[state][cuisine]['4.0'],
        by_state_dictionary[state][cuisine]['4.5'],
        by_state_dictionary[state][cuisine]['5.0'],))
f.close()