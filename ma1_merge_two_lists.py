#Merge two lists as shown below 

def merge_two_lists(list_1, list_2):
    output_list = []
    for string_1 in list_1:
        for string_2 in list_2:
            output_list.append(f'{string_1} {string_2}')

    return output_list

print(merge_two_lists(["Hello ","take"],["Dear","Sir"]))