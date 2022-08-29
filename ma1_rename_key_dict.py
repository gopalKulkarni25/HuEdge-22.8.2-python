# Rename key city to location

def rename_key(input_dict):
    input_dict['location'] = input_dict['city']
    del input_dict['city']
    return input_dict

simple_dict={"name":"Kelly","age":25,"salary":8000,"city":"New york"}
print(rename_key(simple_dict))