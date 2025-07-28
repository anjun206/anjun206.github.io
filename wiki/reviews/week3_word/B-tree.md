# B-tree
B-tree는 **균형 잡힌 다진 검색트리**다

균형 트리 + 다진 트리 라는 거다

대용량 데이터를 효율적으로 저장하고 검색하기 위한 자료구조다

주로, 데이터베이스나 파일 시스템에 사용된다

<br>

## 핵심 개념 요약

| 개념           | 설명                                   |
| ------------ | ------------------------------------ |
| **균형 트리**    | 모든 리프 노드가 동일한 깊이에 있어 탐색 성능이 일정       |
| **다진 트리**    | 하나의 노드가 자식을 여러 개 가질 수 있음 (이진트리 아님)   |
| **정렬 유지**    | 노드 내의 키들이 오름차순으로 정렬되어 있음             |
| **노드 분할/병합** | 삽입/삭제 시 트리의 균형을 유지하기 위해 노드를 분할하거나 병합 |

<br><br>

# B-tree의 구조

- 한 노드는 최대 `m`**개의 자식**을 가질 수 있음 → `m`은 차수(degree)

- 각 노드는 **최소 `⌈m/2⌉`개의 자식**을 가져야 함 (루트 제외)

- 각 노드는 **최소 `⌈m/2⌉ - 1`개의 키값**을 가져야 함

- 자식 포인터들은 키 사이의 값들을 가리킴

```
예시 (차수 4인 B-tree):

       [10 | 20]    ←  키값
        /  |   \
       /   |    \
      /    |     \
   [1 5] [11 15] [25 30 35]  ←  자식
```

<br>

## 특징

- 키들은 **정렬된 상태**로 저장됨

- **모든 리프 노드의 레벨 동일**

- 키는 **중복되지 않음**

- **검색/삽입/삭제 모두 $O(loh N)$**

## 키값에 대한 보충 설명

#### 키값

- 정렬된 데이터 값

- 각 키는 하위 자식 노드들이 어떤 값 범위르 포함하는지 결정

- 탐색할 때 다음 어디로 갈지 결정해주는 길잡이 역할

- 자식과 별개다

<br>

## 주요 연산

### 1. 탐색 (Search)
- 이진 탐색처럼 노드 안의 키들을 검색

- 적절한 자식 노드로 이동하며 반복

- 시간 복잡도: $O(log n)$

### 2. 삽입 (Insert)
- 항상 리프 노드에 삽입

- 노드가 꽉 차면 **분할(split)** 발생

- 상위 노드로 **키가 전파**됨

### 3. 삭제 (Delete)
- 리프에서 제거하거나 자식에서 교체

- **부족한 키를 채우기 위해 병합 또는 이동** 수행

- 복잡하지만 균형 유지가 핵심

<br>

# B-tree 코드 예시

## B-tree (3차수)


### BtreeNode 정의
```py
class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t                      # 최소 차수 (t = 2라면 최대 3개의 자식 가질 수 있음)
        self.keys = []                 # 노드의 키 리스트
        self.children = []            # 자식 노드 리스트
        self.leaf = leaf              # 리프 노드 여부
```
B-tree를 구성할 노드를 우선 만들어준다

<br>

### 탐색함수
```py
    def search(self, key):
        i = 0
        while i < len(self.keys) and key > self.keys[i]:
            i += 1

        if i < len(self.keys) and self.keys[i] == key:
            return True

        if self.leaf:
            return False

        return self.children[i].search(key)
```
1. 현재 노드에서 키를 좌측부터 **순차 탐색**해 `key`보다 큰 값이 나올때까지 인덱스 증가

2. `key`가 현재 노드 키중 존재하면 `True` 반환

3. 현재 노드가 **리프 노드**면 끝까지 온것이니 `False`반환

4. 아니라면 자식 childern[i]노드로 **재귀 탐색 진행** (다시 1번부터)

> 이진 탐색과 다르게 B-tree는 한 노드에 여러 키가 존재해 n진 탐색 구조의 일종

<br>

### 노드 분할 함수
```py
def split_child(self, i):
    t = self.t
    y = self.children[i]          # 분할 대상 노드
    z = BTreeNode(t, y.leaf)      # 새로운 형제 노드 z

    z.keys = y.keys[t:]           # y의 오른쪽 절반 키를 z로 복사
    y.keys = y.keys[:t - 1]       # y는 왼쪽 절반만 유지

    if not y.leaf:
        z.children = y.children[t:]  # 자식도 나눔
        y.children = y.children[:t]

    self.children.insert(i + 1, z)   # z를 자식 리스트에 추가
    self.keys.insert(i, y.keys.pop())  # 중간 키를 부모로 끌어올림
```
- 노드 `y`가 **가득 찼을 경우** (`2t-1`개 도달), **두 개의 노드로** 갈라야함

- **가운데 키** 하나를 **부모노드**로 끌어올리고 **나머지** 절반을 **새로운 형제 노드** `z`로 넘김

<br>

### 삽입 함수
```py
def insert_non_full(self, key):
    i = len(self.keys) - 1

    if self.leaf:
        self.keys.append(None)  # 빈 자리 만들기
        while i >= 0 and key < self.keys[i]:
            self.keys[i + 1] = self.keys[i]  # 오른쪽으로 밀기
            i -= 1
        self.keys[i + 1] = key  # 빈 자리에 key 삽입
    else:
        while i >= 0 and key < self.keys[i]:
            i -= 1
        i += 1  # 이동할 자식 인덱스

        if len(self.children[i].keys) == 2 * self.t - 1:
            self.split_child(i)  # t보다 많으면 많으면 반으로 가르기
            if key > self.keys[i]:
                i += 1
        self.children[i].insert_non_full(key)
```
- 현재 노드가 **리프면 바로 삽입**

- **리프가 아니면**, 어느 자식 노드로 내려갈 지 결정 후

    - 꽉 찼으면 **split**

    - 그리고 **split**결과에 따라 올바른 자식으로 **다시** 내려가 삽입 시도

<br>

### BTree 클래스
```py
class BTree:
    def __init__(self, t):
        self.root = BTreeNode(t, leaf=True)
        self.t = t

    def search(self, key):
        return self.root.search(key)

    def insert(self, key):
        root = self.root
        if len(root.keys) == 2 * self.t - 1:  # 루트가 가득 찼을 때
            new_root = BTreeNode(self.t, leaf=False)
            new_root.children.append(root)
            new_root.split_child(0)          # 루트를 분할해 새로운 루트 생성
            self.root = new_root
        self.root.insert_non_full(key)       # 삽입 시작
```
- 최초엔 루트 노드 하나로 시작 (`leaf=True`)

- 삽입할 때 **루트가 가득 차면, 루트를 쪼개고 새로운 루트 생성**

- 그런 다음 항상 **비어 있는 노드에만 삽입** 시도 (`insert_non_full`)
