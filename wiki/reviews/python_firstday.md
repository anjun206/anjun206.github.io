## 1. print()
소괄호안의 정보를 출력한다.

``` py
# python

print(Hello World!)

---

# 출력 : Hello world!
```
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

## split()
소괄호 안의 문자로 스플릿한다.
문자열 타입에서만 사용가능하다.

```py
# python

print(str(133.345).split('.'))  #str로 문자열로 전환
# 출력: ['133', '345']
```
