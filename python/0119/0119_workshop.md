1. ```python
   def list_sum(x):
       sum = 0
       for i in x:
           sum += i
       print(sum)
   ```



2. ```python
   def dict_list_sum(x):
       sum_age = 0
       for i in x:
           sum_age += i['age']
       print(sum_age)
       
   # 두 가지 방법으로 구해봤습니다  
   
   def dict_list_sum(x):
       sum_age = 0
       for i in range(len(x)):
           
           sum_age += x[i]['age']
       print(sum_age)
       
   ```



3. ```python
   def all_list_sum(x):
       sum_all = 0
       for i in x:
           for k in i:
               sum_all += k
       print(sum_all)
   ```

   