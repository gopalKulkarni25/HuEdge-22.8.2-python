#Using zip and dict functions create a dictionary which has its key-value pairs coming from lst1 and lst2.   

lst1=["Netflix", "Hulu", "Sling", "Hbo"]

lst2=[198, 166, 237, 125]

def create_dict(list_1,list_2):
    return dict(zip(list_1,list_2))

print(create_dict(lst1,lst2))
