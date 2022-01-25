# 0125_workshop

## 1. 무엇이 중복일까

```python
def duplicated_letters(letters):
    dup_letter_list = []
    for letter in letters:
        if letters.count(letter) > 1:
            dup_letter_list.append(letter)

    dup_letter_list = list(set(dup_letter_list))   
         
    return print(dup_letter_list)

# set 을 사용했기에 알파벳 순서대로 나오지 않을 수도 있다. 이 문제에서는 상관없는 듯하다.
```



## 2. 소대소대

```python
def low_and_up(letters):
    letters_bank = [letters[0]]
    

    if letters[0].isupper() == True:
            letter = letters[1].lower()
            letters_bank.append(letter)
    elif letters[0].islower() == True:
            letter = letters[1].upper()
            letters_bank.append(letter)
    
    for i in range(1,len(letters)-1):
        if letters_bank[i].isupper() == True:
            letter = letters[i+1].lower()
            letters_bank.append(letter)

        elif letters_bank[i].islower() == True:
            letter = letters[i+1].upper()
            letters_bank.append(letter)
            
    return print(letters_bank)
```



## 3. 솔로 천국 만들기

```python
# not in 이용

def lonely(lists):
    lonely_list = [lists[0]]
    for i in range(1,len(lists)):
        if lists[i] not in lonely_list:
            lonely_list.append(lists[i])
            
    return print(lonely_list)        

# in 이용

def lonely(lists):
    lonely_list = [lists[0]]
    for i in range(1,len(lists)):
 
        if lists[i] in lonely_list:
            lonely_list.remove(lists[i])
        lonely_list.append(lists[i])
        
    return print(lonely_list)
```

