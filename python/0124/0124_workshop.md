1. ```python
   def get_dict_avg(dicts):
       score_list = []
       score_list.append(list(dicts.values()))
       return print(sum(score_list[0]) / len(score_list[0]))
   
   ```



2. ```python
   def count_blood(lists):
       
       cnt_A = lists.count('A')
       cnt_B = lists.count('B')
       cnt_O = lists.count('O')
       cnt_AB = lists.count('AB')
   
       return print({'A': cnt_A, 'B': cnt_B, 'O': cnt_O, 'AB': cnt_AB})
   
   ```

