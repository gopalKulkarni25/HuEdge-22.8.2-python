#Using map() function and lambda and count() function create a list consisted of the number of occurence of both letters: A and a.   

lst1=["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]

def custom_letter_filter(list_1):
    temp_A = []
    temp_a =[]
    temp_A = list(map(lambda item: item.count('A'),list_1))
    temp_a = list(map(lambda item: item.count('a'),list_1))
    return {'A': sum(temp_A), 'a':sum(temp_a)}


print (custom_letter_filter(lst1))