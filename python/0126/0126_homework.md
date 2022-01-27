# 0126_homework

## 1. Type Class

bool, int, str, list, tuple, set, dict 등이 있습니다. 전에 배운 이것들도 사실 하나의 class인 것입니다.



## 2. Magic Method

\__init__ : class를 실행할 시  바로 실행되는 것으로 인스턴스가 만들어지고 호출되기 전에 실행됩니다.

\__del__ : 인스턴스가 사라지기 전에(del instance)  그 내용을 호출합니다.

\__str__ : str(), format(), print() 내장 함수에 의해 호출됩니다. 왼쪽에 오는 object의 비형식적인 문자열 표현을 계산합니다.

\__repr__ : repr() 내장 함수에 의해 호출됩니다. 왼쪽에 오는 object의 형식적인 문자열 표현을 계산합니다.



## 3. Instance Method

list.append(x) : x값을 list에 추가합니다. 

list.remove(x) : x값을 list에서 제거합니다. 만약 없다면 오류가 발생하고 2개 이상이라면 왼쪽 값부터 제거됩니다.

string.upper : string이 알파벳으로 이루어졌다면 모두 대분자로 바꿉니다.

string.lower : string이 알파벳으로 이루어졌다면 모두 소문자로 바꿉니다.

string.strip([x]) : string에서 좌우 방향으로 특정 x값을 제거합니다. x값이 없는 경우 빈 공간을 제거합니다.

## 4. Module Import

(a) : fibo 						 --> 가장 큰 범위인 파일이름을 불러옵니다.

(b) : fibo_recursion	   --> 파일 안에 있는 쓸 함수를 불러옵니다.

(c) : recursion			    --> 쓸 함수를 여기선 (c)로 부르기로 합니다.