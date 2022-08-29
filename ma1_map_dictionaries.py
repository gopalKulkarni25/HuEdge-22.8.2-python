# Map the dictionary

def map_dictionaries(keys_list,values_list):
    result_dictionary = {}
    result_dictionary[keys_list[0]] = values_list[0]
    result_dictionary[keys_list[1]] = values_list[1]
    result_dictionary[keys_list[2]] = values_list[2]

    return result_dictionary

print(map_dictionaries(['Ten', 'Twenty','Thirty'],[10,20,30]))