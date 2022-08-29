from collections import Counter

class StringClass:

    input_string = ""

    def __init__(self,input_string):
        self.input_string = input_string
    
    def length_of_str(self):
        return len(self.input_string)
    
    def str_to_ch(str_args):
        return [ch for ch in str_args]


my_string = StringClass("12314532")

print(my_string.length_of_str())

class PairsPossible(StringClass):
    pairs = []
    input_child_string = ""

    def __init__(self,input_string):
        self.input_child_string = input_string

    def store_pairs(self):
        temp_arr = StringClass.str_to_ch(self.input_child_string)
        pairs = [[a, b] for idx, a in enumerate(temp_arr) for b in temp_arr[idx + 1:]]
        return pairs
    
    def print_possible_pairs(self,stored):
        str = ""
        for entry in stored:
            for el in entry:
                print(''.join(el), end="")
            print(end=",")
        print()


my_child = PairsPossible("1234")
print(my_child.store_pairs())
my_child.print_possible_pairs(my_child.store_pairs())

class SearchCommonElements(PairsPossible):
    input_search_string = ""

    def __init__(self,input_string):
        self.input_search_string = input_string

    def compare_strings(self,str_1,str_2):
        dict1 = Counter(str_1)
        dict2 = Counter(str_2)

        commonDict = dict1 & dict2
 
        if len(commonDict) == 0:
            print (-1)
            return

        commonChars = list(commonDict.elements())

        commonChars = sorted(commonChars)

        print (','.join(commonChars))


search_common = SearchCommonElements("1234567")

search_common.compare_strings(my_string.input_string,my_child.input_child_string)


class EqualSumPairs(SearchCommonElements):

    sum_arr = []
    not_repeated_pairs = []

    def __init__(self):
        pass

    def sum_of_pairs(self,pos_pairs):
        for el in pos_pairs:
            self.sum_arr.append(sum([int(i) for i in el]))
        
        for item in self.sum_arr:
            if(self.sum_arr.count(item) ==1):
                self.not_repeated_pairs.append(item)
        
        #print the not repeated sum pairs count
        # print(self.sum_arr)
        print(len(self.not_repeated_pairs))


my_sum = EqualSumPairs()

my_sum.sum_of_pairs(my_child.store_pairs())
