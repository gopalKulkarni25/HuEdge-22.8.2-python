def add_sublist(main_lst,sub_lst):
    main_lst[2][1][2].extend(sub_lst)
    return main_lst

main_list=["a","b",["c",["d","e",["f","g"],"k"],"l"],"m","n"]
sub_list = ["h","i","j"]

print(add_sublist(main_list,sub_list))