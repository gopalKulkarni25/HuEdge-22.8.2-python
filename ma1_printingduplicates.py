#Return all the duplicate values from list of arraylist 

input_array_list = [[1,1,3,2],[9,8,8,1],[0,4,5,0,0,1,4]]

def count_duplicates(input_list):
    duplicates_output = {}
    
    for list in input_array_list:
        for item in set(list):
            if(list.count(item) > 1):
                duplicates_output[item] = list.count(item)


    return duplicates_output
        


print(count_duplicates(input_array_list))
