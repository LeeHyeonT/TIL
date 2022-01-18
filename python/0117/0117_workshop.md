1. ```python
   number = int(input())
   for line in range(1,number+1):
       print(line)
   ```



2. ```python
   number = int(input())
   for reverse in range(number,-1,-1):
       print(reverse)
   ```



3. ```python
   a = int(input())
   total = 0
   if a <=10000:
       for number in range(1,a+1):
           total +=number
       print(total)
   else:
       pass