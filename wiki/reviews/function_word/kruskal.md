# 크루스칼 알고리즘

[최소 신장 트리](../week3_word/min_spanning.md) 찾는데 써먹는다

## 🔶 개념

- **그래프의 모든 정점을 최소 비용으로 연결**하는 트리

- [그리디 알고리즘](../../learn/TIL_0718.md#그리디-알고리즘) 기반

- **간선을 기준**으로 정렬 뒤 **싸이클이 생기지 않도록** 트리 구성

<br>

## 🔶 알고리즘 순서

1. 모든 **간선 가중치 기준으로 오름차순**

2. **가중치 낮은 순서**대로 간선 선택

3. 간선 추가 후 **싸이클 유무 확인**

4. 싸이클 **생기지 않을 경우 최소 신장 트리에 포함**

5. **간선이 (정점 수 -1)가 되면 종료**

<br>

## 🔷 싸이클 판별 → 유니온 파인드

- 각 정점의 대표 노드를 관리해 **두 정점이 같은 집합인지 판단**

- `find()`로 루트 노드 찾고 `union()`으로 둘을 합침

- **싸이클은 같은 집합의 정점을 다시 연결 시** 발생

<br>

## 🔶 시간 복잡도

- 간선 정렬 : $O(ElogE)$

- Union-Find(유니온 파인드) : 거의 $O(1)$ (경로 압축시)

<br>

## 💠예제

### 🔸기본 정보

```js
정점 수: 4개  
간선 수: 5개  
간선 정보: (1-2, 3), (1-3, 1), (2-3, 2), (3-4, 4), (2-4, 5)
```

<br>

### 🔷 유니온 파인드

싸이클 판별용으로 사용한다

<br>

#### 🔹유니온 파인드 코드
```py
# 루트 노드를 찾는 함수 (경로 압축 포함)
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])  # 재귀적으로 루트까지 탐색 + 경로 압축
    return parent[x]

# 두 집합을 합치는 함수 (작은 루트를 큰 루트로 연결)
def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)
    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b
```

🔘 `find(parent, x)`

- 입력된 `x`의 **최상위 부모(루트 노드)** 를 찾아줌

- 예) 3 → 2 → 1 이면, `find(parent, 3)`은 1을 반환

> **경로 압축**: 노드들을 한번에 루트에 연결해 속도 🔺

<br>

🔘 `union(parent, a, b)`

- a와 b가 속한 두 집합을 합침

- 두 집합의 루트를 비교해서 더 작은 쪽 루트가 부모가 되도록 연결

> 같은 집합이라면 합치지 않음 → 싸이클 방지 핵심

<br>

___

<br>

### 🔶 크루스칼 알고리즘 본체

모든 간선을 비용 기준으로 정렬한 후,

싸이클이 생기지 않는 선에서 [MST](../week3_word/min_spanning.md)를 완성

<br>

#### 🔸간선 정렬 및 부모 배열 초기화

```py
edges.sort()
parent = [i for i in range(V + 1)]
```

- 모든 간선을 가중치 기준으로 오름차순 정렬

    - 가중치 낮은 것부터 선택할 준비

- 그리디 알고리즘 핵심

- 유니온 파인드를 위한 배열

- `parent[x] = x` 모든 정점이 자기 자신이 루트

<br>

#### 최소 신장 트리 구성 루프

```py
for cost, a, b in edges:
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        total_cost += cost
        mst_edges.append((a, b, cost))
```

정렬된 간선들을 꺼내며 판단

- `find(parent, a)` 와 `find(parent, b)`:
    - **서로 다른 집합**에 있으면 싸이클이 생기지 않음 → **선택**

- `union(...)`:
    - 두 정점을 **같은 집합으로 합침** (트리에 연결)

- `total_cost += cost`:
    - 선택한 간선의 비용을 **총합에 누적**

- `mst_edges.append(...)`:
    - 어떤 간선이 MST에 포함됐는지 **기록**

<br>

___

<br>

### 코드

```py
# 1. 유니온-파인드 함수 정의
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])  # 경로 압축
    return parent[x]

def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)
    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b

# 2. 정점, 간선 수 정의
V = 4
E = 5

# 3. 간선 정보: (비용, 정점1, 정점2)
edges = [
    (3, 1, 2),
    (1, 1, 3),
    (2, 2, 3),
    (4, 3, 4),
    (5, 2, 4)
]

# 4. 간선 정렬 (가중치 오름차순)
edges.sort()

# 5. 부모 배열 초기화 (1번부터 4번까지 정점)
parent = [i for i in range(V + 1)]

# 6. 크루스칼 핵심 로직
total_cost = 0
mst_edges = []

for cost, a, b in edges:
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        total_cost += cost
        mst_edges.append((a, b, cost))

# 7. 결과 출력
print("MST 간선들:")
for a, b, cost in mst_edges:
    print(f"{a} - {b}, 비용: {cost}")
print("총 비용:", total_cost)

```