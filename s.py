# import os
# import uuid
# import json
# def file_read(file_path):
#    with open(file_path,'r') as file:
#        return json.load(file)
   
# file=file_read('sample.json')
# print(file)


import os
import json

# Get the path to 'sample.json' relative to the script
data_file = os.path.join(os.path.dirname(__file__), 'sample.json')
log_file = os.path.join(os.path.dirname(__file__), 'api_test.log')
print(log_file)
print(data_file)

def file_read(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)  # Read and parse the JSON content

file_content = file_read(data_file)
# print(file_content)
