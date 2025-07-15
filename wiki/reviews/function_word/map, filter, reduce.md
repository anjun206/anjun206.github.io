
# map

- **개념**  
  각 요소에 함수 적용 → 새로운 반복가능 객체(iterable) 반환

- **문법**  
  ```python
  map(function, iterable)
  ```

- **예시**  
  ```python
  nums = [1, 2, 3, 4]
  result = map(lambda x: x * 2, nums)
  print(list(result))  # [2, 4, 6, 8]
  ```

---

# filter

- **개념**  
  각 요소에 함수 적용 → True인 값만 추출

- **문법**  
  ```python
  filter(function, iterable)
  ```

- **예시**  
  ```python
  nums = [1, 2, 3, 4]
  result = filter(lambda x: x % 2 == 0, nums)
  print(list(result))  # [2, 4]
  ```

---

# reduce

- **개념**  
  두 요소씩 함수 적용(누적) → 단일 값으로 축약  
  ※ `functools` 모듈 필요

- **문법**  
  ```python
  from functools import reduce
  reduce(function, iterable[, initializer])
  ```

- **예시**  
  ```python
  from functools import reduce
  nums = [1, 2, 3, 4]
  result = reduce(lambda x, y: x + y, nums)
  print(result)  # 10
  ```

---

# 한눈에 보는 비교표

| 함수    | 역할            | 반환값                  | 함수 인자 수 | 사용 예시                       |
| ------- | --------------- | ---------------------- | ----------- | ------------------------------- |
| map     | 함수 적용       | map 객체 (반복 가능)    | 1개         | 각 요소를 제곱: `map(f, arr)`    |
| filter  | 조건 걸러내기   | filter 객체 (반복 가능) | 1개         | 짝수만: `filter(f, arr)`        |
| reduce  | 누적 연산       | 단일 값                 | 2개         | 합계: `reduce(f, arr)`          |

---

# 참고

- `map`과 `filter` 결과는 반복자(iterator)  
- 결과를 리스트로 보려면 `list()`로 감싸기  
- `reduce`는 `functools`에서 import 필요

---

## 더 알아보기

- [공식 문서: map](https://docs.python.org/3/library/functions.html#map)
- [공식 문서: filter](https://docs.python.org/3/library/functions.html#filter)
- [공식 문서: functools.reduce](https://docs.python.org/3/library/functools.html#functools.reduce)
