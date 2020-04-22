import json

lat =[]
long =[]
with open('data2.json','r') as f:
    data = json.load(f)
for thedata in data:
    lat.append(thedata['location']['latitude'])
    long.append(thedata['location']['longitude'])
