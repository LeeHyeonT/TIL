1. len, max, min, sum, print, abs, chr, divmod, enumerate, filter, lambda, zip



2. ```python
   def get_middle_char(word):
       if len(word) % 2:
           print(word[int(len(word)//2)])
       else:
           print(word[int(len(word)//2)-1:int(len(word)//2)+1])
   
   ```



3. (4) 번이 실행시 오류가 발생합니다.  위치를 먼저 키워드화하게 되면 이후 변수에서 위치를 잃게 되어 위치의 표현으로 표현이 불가합니다. 



4.  10



5. ```python
   def my_avg(*x):
      print(sum(x)/len(x))
   ```

   