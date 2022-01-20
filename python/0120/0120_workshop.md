1. ```python
   # ASCII 변환 함수 이용	
   def get_secret_word(numbers):
       for i in numbers:
           print(chr(i), end = '')
   
   get_secret_word([83,115,65,102,89])
   ```



2. ```python
   def get_secret_number(name):   
       sum_name = 0
       for i in name:
           sum_name += ord(i)
       return print(sum_name)
   ```



3. ```python
   def get_secret_number(name):   
       sum_name = 0
       for i in name:
           sum_name += ord(i)
       return sum_name
   
   def get_strong_word(*strings):
       strength = [[],[]]
       for iter, string in enumerate(strings):
           strength[iter] = get_secret_number(string)
   
       if strength[0] > strength[1]:
           return strings[0]
       else:
           return strings[1]
   ```

   