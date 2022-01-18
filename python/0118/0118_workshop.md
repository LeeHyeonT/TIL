1. ```python
   N = int(input())
   for i in range(1,1001):
       if N % i == 0:
           print(i)
   ```



2. ```python
   numbers = [
   	85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67,
   	51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64,
   	52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24
   ]
   
   for i in range (len(numbers)-1):
       for j in range (len(numbers)-1):
           if numbers[j]>numbers[j+1]:
                temp=numbers[j]
                numbers[j]=numbers[j+1]
                numbers[j+1]=temp
                   
   if len(numbers)%2==1:
           print ('중간값 : %d' %numbers[int(len(numbers)/2)])
   else:
           print ('중간값 : %d %d' %(numbers[int(len(numbers)/2)-1],numbers[int(len(numbers)/2)]))
   ```



3. ```python
   number = int(input())
   
   for i in range(1,number+1):
       for k in range(1,i+1):
           print(k, end = '')
           if k == i:
               print('')
   ```

   