data = {"Name": "Singular",
"Score": [{"Math": 100, "English": 99}, 
{"Chinese": 98, "Nature": 97}]}

print(data['Score'][0]['English'])
print(data['Score'][1]['Chinese'])

print (type(data) )
json_str = json. dumps(data)
print (json_str)
print(type(json_str) )

json_dict = json. loads(json_str)
print (json_dict)
print (type(json_dict) )
print(json_dict ["Score"][0] ["English"])
print (json_dict ["Score"][1] ["Chinese" ])
