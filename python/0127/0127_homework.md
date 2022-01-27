# 0127_homework

## 1. Circle �ν��Ͻ� �����

```python
circle = Circle(3,2,4)
print(circle.area())			# 3.14 * 3 * 3
print(circle.circumference())	# 2 * 3.14 * 3
```





## 2. Dog�� Bird�� Animal�̴�

```python
class Dog(Animal):
    def walk(self):
        print(f'{self.name}! �޸���!')
    def bark(self):
        print(f'{self.name}! ¢�´�!')
        
class Bird(Animal):
    def fly(self):
        print(f'{self.name}! Ǫ���!')
```



## 3. ������ ����

- ZeroDivisionError

  ��� ���ڸ� 0���� �������� �� �� �߻��Ѵ�.

- NameError

  ������ �̸��� ã�� �� ���� �� �߻��Ѵ�.

- TypeError

  ���� �ٸ� type���� ������ �õ��� �� �߻��Ѵ�.

- IndexError

  ���� index���� �����Ϸ��� �� �� �߻��Ѵ�.

- KeyError

  ���� Key���� �����Ϸ��� �� �� �߻��Ѵ�.

- ModuleNotFoundError

  ���� ��ο� import �� ����� �������� ���� �� �߻��Ѵ�.

- ImportError

?		import �� ����� ��ġ���� �ʾ��� �� �߻��Ѵ�.

