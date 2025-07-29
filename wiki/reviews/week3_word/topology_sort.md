# 위상 정렬
기본적으로 위상 정렬은

비순환 [방향 그래프](graph_type.md#방향-그래프)(DAG)에서만 가능하다

이유는<br>
위상 정렬은 $G$가 간선$(u, v)$를 가질 때,<br>$u$가 $v$보다 순서 상으로 먼저 나타나도록하는<br> 모든 정점의 선형순서라

순환하게 되는 순간 선형 나열이 불가하니
<br>
비순환 그래프에서만 가능한 것이다

## 개념
위에 말했듯이 순서대로 나열하는 것을 의미한다

단, 이 순서는 모든 간선 (A → B)에 대해 A가 B보다 먼저 나오는 순서를 만족해야 한다

## 예시
이런 식으로 주어진다면
```
A → C  
B → C  
C → D
```

가능한 위상 정렬 결과는<br>
`A → B → C → D` 또는 `B → A → C → D`<br>
가 된다

## 구현
구현 방식은 대표적으로 2가지가 존재한다

**진입 차수 방식(Kahn's Algorithm)** 과 **DFS 기반 방식** 말이다

### 진입 차수 방식
```py
from collections import deque

indegree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

# 그래프 및 진입 차수 초기화
for u, v in edges:
    graph[u].append(v)
    indegree[v] += 1

# 진입 차수가 0인 노드 큐에 삽입
queue = deque([i for i in range(1, N + 1) if indegree[i] == 0])
result = []

while queue:
    cur = queue.popleft()
    result.append(cur)
    for neighbor in graph[cur]:
        indegree[neighbor] -= 1
        if indegree[neighbor] == 0:
            queue.append(neighbor)

print(result)

```
<br>

[추가 내용](/wiki/learn/TIL_0725+.md#진입-차수-방식)
<br><br>

### DFS 방식
```py
def dfs(node):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor)
    result.append(node)  # 후위 순회처럼 나중에 추가

# 초기화
visited = [False] * (N + 1)
result = []

for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)

result.reverse()  # 뒤집어서 위상 정렬 결과 도출
print(result)
```

<br>

[추가 내용](/wiki/learn/TIL_0725+.md#dfs-기반-방식)
<br><br>

## 비교

<br>

| 항목              | Kahn’s Algorithm (진입 차수 방식) | DFS 방식                            |
| --------------- | --------------------------- | --------------------------------- |
| **시간 복잡도**      | O(V + E)                    | O(V + E)                          |
| **자료구조**        | 큐 사용                        | 재귀 또는 명시적 스택                      |
| **사이클 감지**      | 자연스럽게 감지 가능 (노드 수로 판단)      | 별도 사이클 체크 필요                      |
| **정렬 순서**       | 진입 차수 0 순서대로 → 결과 예측 쉬움     | 종료 시점 역순 → 예측 어려움                 |
| **재귀 깊이**       | 거의 없음                       | 깊은 재귀로 스택 오버플로우 위험 (특히 노드 수 많을 때) |
| **병렬화/스케줄링 적합** | 적합함 (선후 작업 명확)              | 보통 적합하지 않음                        |
| **구현 난이도**      | 약간 더 복잡                     | 더 간단 (재귀만 잘 쓰면)                   |

___

<br>

- 시간 복잡도는 $O(V + E)$ (노드 + 간선 수)로 동일

- 그러나 상항에 따라 효율이 다름
<br><br><br>

___

| 상황                                 | 추천 방식                                    |
| ---------------------------------- | ---------------------------------------- |
| **사이클도 같이 체크하고 싶다**                | Kahn’s 방식 추천                             |
| **작업 종료 시점이 중요하다 (예: DFS로 탐색 순서)** | DFS 방식 추천                                |
| **노드 수가 매우 많고 재귀 깊이 우려된다**         | Kahn’s 방식이 안전                            |
| **구현이 간단한 게 좋다**                   | DFS 방식 간단함 (특히 Python 등 재귀 제한이 느슨한 언어에서) |

___