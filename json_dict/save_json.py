import json
data={
    "name":"himanshu sngh",
    "age":21,
    "address":"varansi, UP 221301"
}
filepath="./json_dict/ans.json"
with open('','w') as file:
    json.dump(data, file,indent=5)
