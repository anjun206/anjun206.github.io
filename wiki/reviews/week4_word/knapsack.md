배낭 문제란 뜻이다

<br>

대강 설명해 보자면

<br>

배낭에 효율적으로 물건 담기다

<br>

# Knapsack Problem

## 개념

주어진 무게 제한 내에서 최대의 가치를 얻도록<br>
물건을 선택하는 조합 최적화 문제이다

알고리즘과 CS에서 대표적 [동적 계획법(DP)](DP.md) 문제로 자주 나온다
<br><br>

## 기본 가정
- 물건이 `n`개 있음

- 각 물건 `i`는 다음 정보를 가짐 :

    - 무게 : `w[i]`

    - 가치 : `v[i]`

- 배낭에 담을 수 있는 최대 무게 `w`

**목표 :**
- 배낭의 무게 제한을 넘지 않고 가치 총합 최대화하기

<br>

### 문제 종류

1. **0-1 Knapsack Problem**

    - 각 물건을 최대 1번만 선택 가능

    - **대표적 DP문제**

<br>

1. **Unbounded Knapsack Problem**

    - 각 물건을 무한히 많이 선택 가능

<br>

3. **Fractional Knapsack Proble**

    - 물건 쪼개기 가능 (비율만큼 넣기)

    - **[그리디 알고리즘](greedy.md)으로 해결 가능**

<br>

## 0-1 배낭 문제

- 각 물건을 한 번만 담을 수 있음.

- 물건을 담을지 말지를 결정 → 선택은 0 또는 1

- **동적 계획법(DP)** 으로 풀이

<br>

**핵심 아이디어는**

- `dp[i][j]`: `i`번째까지의 물건으로, **무게 `j` 이하로 담았을 때의 최대 가치**

<br>

### 예제

```py
# 물건 수 N, 최대 배낭 무게 W
N = 4
W = 7
weights = [6, 4, 3, 5]   # 각 물건의 무게
values = [13, 8, 6, 12]  # 각 물건의 가치

# dp[i][w] = i번째 물건까지 고려했을 때, 무게 w로 만들 수 있는 최대 가치
dp = [[0] * (W + 1) for _ in range(N + 1)]

for i in range(1, N + 1):  # i번째 물건까지 고려
    for w in range(W + 1):  # 무게 w에 대해서
        if weights[i-1] > w:
            # 현재 물건 무게가 가방보다 크면, 못 담음 → 이전값 그대로
            dp[i][w] = dp[i-1][w]
        else:
            # 담지 않을 경우 vs 담을 경우 중 최대 가치 선택
            dp[i][w] = max(dp[i-1][w], dp[i-1][w - weights[i-1]] + values[i-1])

print("최대 가치:", dp[N][W])
```

### 좀더 세부하게

[방법 3가지만](0-1.md)

<br><br>

## 무한 배낭 문제

- 물건 여러 번 담기 ㄱㄴ

- 동전 문제, 재료 무제한 구매 등이 있음

<br>

**핵심 아이디어**

- `dp[w] = max(dp[w], dp[w - weight[i]] + value[i])`

- 한 줄 DP로도 ㄱㄴ

<br>

### 예제

```py
# 물건 수 N, 최대 배낭 무게 W
N = 3
W = 10
weights = [3, 4, 5]
values = [30, 50, 60]

# dp[w] = 무게 w일 때 얻을 수 있는 최대 가치
dp = [0] * (W + 1)

for i in range(N):  # 각 물건에 대해
    for w in range(weights[i], W + 1):  # 그 무게부터 끝까지
        # 현재 무게 w일 때, i번 물건을 하나 더 담는 경우 고려
        dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

print("최대 가치:", dp[W])
```


<br><br>

## 분할 가능 배낭 문제

- 물건을 쪼개 담기 ㄱㄴ (비율로 담기)

- 금이나 밀가루 등등

- **그리디**로 해결

<br>

**핵심 아이디어**

- 가치 밀도 (가치/무게)가 높은 순으로 정렬해 담음

- 남은 용량만큼 담고, 더 못담으면 멈춤

<br>

### 예제

```py
W = 50  # 배낭의 최대 용량
items = [(60, 10), (100, 20), (120, 30)]  # (가치, 무게) 튜플 리스트

# 가치 밀도(value/weight) 기준으로 내림차순 정렬
items.sort(key=lambda x: x[0]/x[1], reverse=True)

total_value = 0.0  # 누적된 가치

for value, weight in items:
    if W >= weight:
        # 통째로 담을 수 있으면 담기
        total_value += value
        W -= weight
    else:
        # 일부만 담아야 하면 비례해서 담기
        total_value += value * (W / weight)
        break  # 배낭이 가득 찼으므로 종료

print("최대 가치:", total_value)
```

# 요약

| 문제 유형  | 반복 여부  | 쪼갤 수 있음 | 풀이 방식       | 시간 복잡도     |
| ------ | ------ | ------- | ----------- | ---------- |
| 0-1 배낭 | ❌ 한 번만 | ❌ 불가    | DP (2차원)    | O(N × W)   |
| 무한 배낭  | ✅ 여러 번 | ❌ 불가    | DP (1차원)    | O(N × W)   |
| 분할 배낭  | ✅ 여러 번 | ✅ 가능    | Greedy (정렬) | O(N log N) |
