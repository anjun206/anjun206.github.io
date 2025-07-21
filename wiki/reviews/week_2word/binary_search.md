# 이분 탐색(Binary Search)

## 개념 요약
- **이분 탐색**은 **정렬된 배열**에서 원하는 값을 **반씩 줄여가며** 찾는 효율적인 탐색 알고리즘입니다.
- 시간복잡도는 **O(log N)**으로 매우 빠릅니다.
- 전제 조건: **리스트가 오름차순(또는 내림차순)으로 정렬되어 있어야 함**

## 동작 원리
1. 리스트의 가운데 값을 확인한다.
2. 찾는 값이 가운데 값보다 작으면 **왼쪽 절반**을 탐색한다.
3. 크면 **오른쪽 절반**을 탐색한다.
4. 같으면 탐색 종료 (찾음).
5. 찾는 값이 없을 때까지 위 과정을 반복한다.

---

## 예제 코드 (Python)

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # 찾은 경우 인덱스 반환
        elif arr[mid] < target:
            left = mid + 1  # 오른쪽 절반 탐색
        else:
            right = mid - 1  # 왼쪽 절반 탐색

    return -1  # 찾는 값이 없는 경우
```

> 예시

```py
arr = [1, 3, 5, 7, 9, 11, 13]
target = 9

result = binary_search(arr, target)
print(result)  # 출력: 4 (인덱스 4에 9가 있음)
```

## 참고사항
- **정렬되지 않은 배열**에서는 사용 불가 (오답 나옴)

- 중복 값이 있는 경우, 첫 번째 혹은 마지막 인덱스를 원하면 **변형된 이분 탐색** 필요
