# 1. print()
소괄호안의 정보를 출력한다.

``` py
# python

print(Hello World!)

---

# 출력 : Hello world!
```
<br>
### 1 - 1. 추가 정보 f-string
`print(f's : {s}')`
문자열 안에 **중괄호 {}**를 쓰면
그 안에 변수값이 자동으로 들어감

`f'문자열{변수}'`처럼 쓰면
문자열 중간 `{}` 안의 값을 바로 넣을 수 있음

```py
# python

name = "Tom"
age = 20
print(f'이름: {name}, 나이: {age}')
# 출력: 이름: Tom, 나이: 20
```
___
<br>
<br>
<br>

# 2. input()
소괄호 안의 정보를 출력한다.

```py
# python

name = input("이름을 입력하세요: ")
print("안녕하세요,", name)
```
```
이름을 입력하세요: 홍길동
안녕하세요, 홍길동
```
`input()`으로 받는 값은 **항상 문자열**이기에 숫자로 쓰려면 변환해야함

## 2 - 1. input() + f-string
input도 f-string과 자주 사용
```py
# python

age = input(f"나이를 입력하세요: ")
print(f'당신의 나이는 {age}살입니다.')
```
# 3. map()
- `map()`은 여러개의 값을 한번에 같은 방식으로 변환할때 쓰는 함수
- **기본 형태 :**
```py
  # python

mapp(함수, 반복가능한값)
```
- **함수 :** 적용할 기능 (ex: int, float, str, 사용자 정의 함수 등)
- **반복가능한값 :** 리스트, 튜플, 문자열 등


```py
a, b, c = input().split()  # '1 2 3' 입력 → a='1', b='2', c='3'
a = int(a)
b = int(b)
c = int(c)
```
같은 귀찮은 일을
___
```py
a, b, c = map(int, input().split())
```
한번에 간단히 변환 가능하다!

## 3 - 1. 작동 방식
- `input().split()` => `['1', '2', '3']` (문자열들의 리스트)
- `map(int, ['1', '2', '3',])` => `[1, 2, 3]` (정수로 변환)
- 변수 여러 개에 동시 할당 혹은
- `list()`로 감싸서 리스트로 만들 수도 있음

## 3 - 2. 예시
#### 1. 리스트로 만들기
```py
nums = list(map(int, input().split()))
print(nums)
```
- 입력 : `10 20 30`
- 출력 : `[10, 20, 30]`

#### 2. 소수로 바꾸기
```py
scores = list(map(float, input().split()))
print(scores)
```
- 입력 : `1.5 3.7 8.2`
- 출력 : `[1.5, 3.7, 8.2]`
- 
#### 3. 문자열 대문자로 바꾸기
```py
words = list(map(str.upper, input().split()))
print(words)
```
- 입력: `hello world`
- 출력: `['HELLO', 'WORLD']`

# split()
- 소괄호 안의 문자로 스플릿한다.
- 문자열 타입에서만 사용가능하다.

```py
# python

print(str(133.345).split('.'))  #str로 문자열로 전환

# 출력: ['133', '345']
```
※ 유의 사항 `'.'` 과 같은 인자도 문자열로 넣어야 함
















