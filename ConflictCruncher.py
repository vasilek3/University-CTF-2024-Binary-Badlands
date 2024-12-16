# Input two dictionaries as strings
dict1_str = input().strip()
dict2_str = input().strip()

dict1 = eval(dict1_str)
dict2 = eval(dict2_str)

merged_dict = dict1.copy()
merged_dict.update(dict2)

print(merged_dict)
#Author: voloshka_3 / vasilek3
#Name: Conflict Cruncher
#Level: very easy
