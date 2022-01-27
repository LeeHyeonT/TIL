# 0127_homework

## 1. Circle 인스턴스 만들기

```python
circle = Circle(3,2,4)
print(circle.area())			# 3.14 * 3 * 3
print(circle.circumference())	# 2 * 3.14 * 3
```





## 2. Dog과 Bird는 Animal이다

```python
class Dog(Animal):
    def walk(self):
        print(f'{self.name}! 달린다!')
    def bark(self):
        print(f'{self.name}! 짖는다!')
        
class Bird(Animal):
    def fly(self):
        print(f'{self.name}! 푸드덕!')
```



## 3. 오류의 종류

- ZeroDivisionError

  어떠한 숫자를 0으로 나누려고 할 때 발생한다.

- NameError

  변수의 이름을 찾을 수 없을 때 발생한다.

- TypeError

  서로 다른 type으로 연산을 시도할 때 발생한다.

- IndexError

  없는 index값에 접근하려고 할 때 발생한다.

- KeyError

  없는 Key값에 접근하려고 할 때 발생한다.

- ModuleNotFoundError

  현재 경로에 import 할 모듈이 존재하지 않을 때 발생한다.

- ImportError

?		import 할 모듈을 설치하지 않았을 시 발생한다.

