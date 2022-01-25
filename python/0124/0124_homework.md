1. ```python
   def count_vowels(values):
       vowels = 'aeiou'
       cnt = 0
       for i in vowels:
           cnt += values.count(i)
       return print(cnt)
   count_vowels('apple')
   ```



2. (4)번이 옳지 않습니다. 특정 문자를 지정하지 않으면 빈 공간을 제거합니다.



3. ```python
   def only_square_area(lengths, heights):
       area = int()
       area_list = []
       for length in lengths:
           for height in heights:
               area = height * length
               if height == length:
                   area_list.append(area)
   
       return print(area_list)
   ```

   