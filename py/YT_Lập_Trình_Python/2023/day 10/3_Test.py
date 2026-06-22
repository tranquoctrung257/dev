

people = {
  "Emma": 71,
  "Jack": 45,
  "Amy": 15,
  "Ben": 29
}

dict_new = {
    
}
for k,v in people.items():
    # dict_new[k] = v*2 
    dict_new.update({k:v*2})

print(dict_new)