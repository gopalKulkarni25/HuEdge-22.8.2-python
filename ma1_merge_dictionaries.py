#Merge following two Python dictionaries into one

def merge_two_dictionaries(dict_1,dict_2):
    return dict_1| dict_2


print(merge_two_dictionaries({'Ten':10,'Twenty':20,'Thirty':30},{'Thirty':30,'Fourty':40,'Fifty':50}))

