
# Morris Inorder Tree Traversal (모리스 중위 순회)

재귀도 스택도 안 쓰고, 임시 스레딩(threading) 으로 O(1) 추가 메모리만으로 중위순회 하는 기법

<br>

## 개념

- 각 노드 `cur`의 **중위 선행자**[^1] `pred`의 `right` 포인터를 잠깐 `cur`로 연결(스레딩)[^2]해 두고, 왼쪽 서브트리 처리가 끝났을 때 그 스레드를 따라 원 위치로 복귀한다

- 방문(visit) 규칙은 중위순서 그대로: **Left → Node → Right**

- 순회가 끝나면 모든 임시 연결을 **원래대로 복구**하므로 트리는 변하지 않는다

<br><br>

## 특징

- **시간복잡도**: `O(n)` (각 간선이 최대 2번(내려갈 때/복귀할 때) 사용)

- **공간복잡도**: `O(1)` (재귀 스택/명시적 스택 불필요)

- **트리 보존**: 임시 스레딩을 **반드시 되돌리는 것**이 핵심

- **장단점**

    - 장점: 스택 없이 중위순서 보장, 깊은 트리에서도 스택 오버플로우 위험 없음

    - 단점: 순회 중 포인터를 건드리므로 **동시 접근/불변 구조**에는 부적합, 구현 실수 시 복구 누락 위험

<br><br>

## 동작 흐름(중위)

1. `cur`가 왼쪽 자식이 **없으면**: `cur`를 방문하고 `cur = cur->right`

2. 왼쪽 자식이 **있으면**:

    1. `pred = cur->left`에서 시작해 `pred->right`가 `nil`(또는 `cur`)일 때까지 오른쪽으로 최대로 진행해 pred를 찾는다

    2. `pred->right`가 `nil`이면 스레딩 생성(`pred->right = cur`) 후 `cur = cur->left`

    3. `pred->right`가 `cur`이면 스레딩 해제(`pred->right = nil`) → `cur` 방문 → `cur = cur->right`

이 과정을 `cur`가 `nil`이 될 때까지 반복

<br><br>

## 코드 예시

<br>

```c
// 모리스 순회 (중위 순회 에디션)
while (cur != t->nil) {
    // cur 노드의 왼쪽 자식이 없을 경우 
    if (cur->left == t->nil) {
        // 각주 대신 cur 배열에 push하는 거 넣기
        cur = cur->right;
    } 
    else {
        node_t *pred = cur->left;
        while (pred->right != cur && pred->right != t->nil) {
        pred = pred->right;
        }
        if (pred->right == t->nil) {
        // 우측 자식 노드 cur로 연결
        pred->right = cur;
        cur = cur->left;
        } else {
        // 우측 자식 노드 복원
        pred->right = t->nil;
        // 각주 대신 cur 배열에 push하는 거 넣기
        cur = cur->right;
        }
    }
}
return 0;
```

> 쓰고 싶다면 각주 부분에 배열에 삽입하는거나 프린트 넣어서 쓰면된다

<br><br>

___

[^1]: **중위 선행자(inorder predecessor)** — 현재 노드 `cur`보다 **바로 작은** 키를 가진 노드. 구현상 `cur->left`에서 시작해 오른쪽으로 최대로 내려간 노드

[^2]: **스레딩(threading)** — 원래 `nil`이어야 할 `pred->right`를 **임시로 `cur`로 연결**해 되돌아올 경로를 만든 뒤, 복귀 시 반드시 원복하는 테크닉