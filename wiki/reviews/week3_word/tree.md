<br><br>
**트리**(나무라는 뜻) 구조를 알아보자 🌲🌲🔥🔥💀
<br><br>
ㄹㅇ 참트루로다가 유명하니 꼭 잘 기억하자
<br><br><br>

# 트리
**"계층적 구조를 이루는 비선형 자료구조"** 다

누가 물어보면 이렇게 답해라

지적 허영심을 뽐낼 좋은 기회니
<br><br>
(따봉하는 개구리 짤)
<br><br><br>

## 트리 기본
트리는 [노드](graph_ele.md#노드-버택스)와 [간선](graph_ele.md#엣지)으로 이루어진 자료구조로<br>
(그래프의 일종)<br>
이러한 특징을 갖고 있다

- 계층적 구조

- 하나의 루트 노드에서 시작

- 사이클이 없음

- 부모가 하나임;;

### 기본 용어

| 용어                | 설명                    |
| ----------------- | --------------------- |
| **노드(Node)**      | 데이터를 담는 기본 단위         |
| **루트(Root)**      | 트리의 시작점이 되는 노드        |
| **부모 노드(Parent)** | 특정 노드를 가리키는 상위 노드     |
| **자식 노드(Child)**  | 부모에 연결된 하위 노드         |
| **리프 노드(Leaf)**   | 자식이 없는 노드             |
| **간선(Edge)**      | 노드와 노드를 연결하는 선        |
| **서브트리(Subtree)** | 어떤 노드를 루트로 하는 트리      |
| **레벨(Level)**     | 루트부터의 깊이 (루트는 0 또는 1) |
| **높이(Height)**    | 가장 깊은 리프 노드까지의 거리     |

<br>

### 트리의 종류

| 종류                             | 설명                           |
| ------------------------------ | ---------------------------- |
| **이진 트리**                      | 모든 노드가 최대 두 개의 자식을 가짐        |
| **이진 탐색 트리(BST)**              | 왼쪽 자식 < 부모 < 오른쪽 자식          |
| **힙(Heap)**                    | 부모와 자식 간의 우선순위 관계            |
| **균형 트리(AVL, Red-Black Tree)** | 트리의 높이를 일정하게 유지              |
| [**트라이(Trie)**](Trie.md)                  | 문자열 검색에 최적화된 트리              |
| **B-트리**                       | 데이터베이스, 파일 시스템 등에 사용되는 다진 트리 |

<br><br>

## 트리 대표적 순회 방식

지방 순회 공연 비스무리하게 순회를 도는데

이게 중요하다

**대표 순회 방식:**
1. **전위 순회 (Preorder):** `부모 → 왼쪽 → 오른쪽`

2. **중위 순회 (Inorder):** `왼쪽 → 부모 → 오른쪽`

3. **후위 순회 (Postorder):** `왼쪽 → 오른쪽 → 부모`

4. **레벨 순회 (Level-order):** `위에서 아래로, 왼쪽에서 오른쪽` [(BFS)](BFS_DFS.md#bfs)
