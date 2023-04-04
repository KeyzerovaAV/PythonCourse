"""
Напишите программу для печати всех уникальных значений в словаре. 
Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {"V": " S009 "}, {"VIII": " S007 "}] 
Output: {'S005', 'S002', 'S007', 'S001', 'S009'} 
Список словарей задан изначально. Пользователь его не вводит.
"""

dictionaries_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {"V": " S009 "}, {"VIII": " S007 "}]
unique_values_set = set()
for dict_i in dictionaries_list:
    for key in dict_i:
        dict_i[key] = dict_i[key].strip()
        unique_values_set.add(dict_i[key])        
print(unique_values_set)
