#Convert Dictionary to list

def dictionary_to_list(input_dictionary):
    output_list = []
    for key,values in input_dictionary.items():
        values.insert(0,key)
        output_list.append(values)

    return output_list


print(dictionary_to_list({'HuEx': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}))
