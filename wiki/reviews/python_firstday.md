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

# split()
- 소괄호 안의 문자로 스플릿한다.
- 문자열 타입에서만 사용가능하다.

```py
# python

print(str(133.345).split('.'))  #str로 문자열로 전환

# 출력: ['133', '345']
```
※ 유의 사항 `'.'` 과 같은 인자도 문자열로 넣어야 함
















