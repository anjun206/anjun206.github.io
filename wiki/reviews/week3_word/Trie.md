<br><br>
Trie...(트리아님, 트라이임)
<br><br>
기본적으로 N진 [트리](tree.md) 기반이기에 [트리](tree.md)에 대해서 공부해야 한다
<br><br><br>
만약 안했더라면...
<br><br><br>
...
<br><br><br>
뭘봐?
<br><br><br>
안나가고
<br><br><br>
나가 ㅡㅡ+
<br><br><br>
...
<br><br><br>
트리도 모르는 코린이(코딩 어린이라는 뜻)들은 나갔으니 이제 시작하겠다
<br><br>

# 트라이
트라이는 트리 기반 자료구조다

특히 접두사 처리가 특기라<br>
문자열 집합 검색, 사전 검색, **자동 완성** 등이 자주 사용된다

## 개념 요약

- 트리는 문자 단위로 분기, 각 노드는 하나의 문자 표현

- 루트에서 리프까지 경로가 하나의 단어

- 공통 접두사 공유로 중복 회피

<br><br>

## 예시

`"cat"`, `"cap"`, `"can"` 이라는 단어가 있다면, Trie는 이리 표현
```scss
(root)
  └── c
       └── a
            ├── t (끝 표시)
            ├── p (끝 표시)
            └── n (끝 표시)
```

- `"ca"`까지는 공유

- `"t"`, `"p"`, `"n"`으로 나뉨

<br><br>

## 특징

| 기능     | 시간 복잡도 |
| ------ | ------ |
| 삽입     | O(L)   |
| 검색     | O(L)   |
| 접두사 탐색 | O(L)   |

> L은 문자열의 길이


## 코드 예시

### 🔹 `TrieNode` 클래스

```py
class TrieNode:
    def __init__(self):
        self.children = {}   # 현재 노드에서 이어지는 자식 노드들을 저장할 딕셔너리
        self.is_end = False  # 단어의 끝인지 여부
```
- `children`: `dict` 자료형으로 자식 문자를 키로, 그 문자에 해당하는 `TrieNode`를 값으로 저장.

- `is_end`: 단어의 끝인지 여부 (`"cat"`이 들어왔다면 `'t'` 노드에서 True)

<br><br>

### 🔹 `Trie` 클래스

#### 1. 초기화
```py
class Trie:
    def __init__(self):
        self.root = TrieNode()
```
- 시작점(root)은 빈 노드로 시작

<br><br>

#### 2. 단어 삽입(`insert`)
```py
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True
```
- 단어의 각 문자 `ch`를 따라간다
    - 그 문자에 자식노드가 없을 시 새로 `TrieNode()` 추가
    - 해당 노드로 이동
- 반복 종료시 `is_end = True`로 설정해 단어 끝 표시
<br><br>

#### 3. 단어 검색 (`search`)
```py
    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end
```
- 주어진 `word`를 따라가며 하나라도 없으면 `False`
- 끝까지 탐색했을 경우 마지막 노드의 `is_end`가 `True`면 단어 발견
<br><br>

#### 4. 접두사 검색 (`starts_with`)
```py
    def starts_with(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True
```
- `prefix` 문자열을 따라가다가 없으면 `False`

- 마지막까지 다 찾으면 `True` (단어의 끝 여부는 신경 안 씀)

#### 한번에 보기
```py
class TrieNode:
    def __init__(self):
        self.children = {}        # 자식 노드들을 저장하는 딕셔너리
        self.is_end = False       # 해당 노드가 단어의 끝인지 여부 표시

class Trie:
    def __init__(self):
        self.root = TrieNode()   # 루트 노드 생성

    def insert(self, word):
        node = self.root
        for ch in word:                      # 단어의 각 문자에 대해
            if ch not in node.children:      # 자식 노드에 문자가 없으면 새로 생성
                node.children[ch] = TrieNode()
            node = node.children[ch]         # 다음 문자로 이동
        node.is_end = True                   # 단어의 끝 지점 표시

    def search(self, word):
        node = self.root
        for ch in word:                      # 단어의 각 문자 확인
            if ch not in node.children:      # 문자 없으면 False
                return False
            node = node.children[ch]         # 다음 문자로 이동
        return node.is_end                   # 단어의 끝인지 확인하고 결과 반환

    def starts_with(self, prefix):
        node = self.root
        for ch in prefix:                    # 접두사의 각 문자 확인
            if ch not in node.children:      # 문자 없으면 False
                return False
            node = node.children[ch]         # 다음 문자로 이동
        return True                          # 두사 존재하면 True
```