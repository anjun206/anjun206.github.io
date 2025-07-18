# 스택 (Stack)
## 개념
- 데이터를 **쌓아올리는 구조**
- 나중에 넣은 데이터가 먼저 나오는 구조

  (LIFO: Last In First Out)
## 주요 연산
- **push**: 데이터 넣기(쌓기)

- **pop**: 데이터 꺼내기(맨 위에서 꺼냄)

- **peek/top**: 가장 위에 있는 데이터 확인
## 예시
- 프링글스 통에서 과자를 뺄 때

- 책 더미에서 제일 위에 있는 책을 꺼낼 때

```
Stack (bottom -> top):

   +-----+
   |  3  |  <-- push(3)
   +-----+
   |  2  |  <-- push(2)
   +-----+
   |  1  |  <-- push(1)
   +-----+

(pop을 하면 맨 위(top)에서 빠짐)

   +-----+
   |     |  <-- pop() -> 3이 나옴
   +-----+
   |  2  |
   +-----+
   |  1  |
   +-----+
```


```py
# 파이썬 예시

stack = []
stack.append(1)  # push
stack.append(2)
print(stack.pop())  # pop, 출력: 2
print(stack.pop())  # pop, 출력: 1
```
<br><br><br>

> 파이썬에서 list로 스택 비스무리하게 쓰는법

|    스택 연산    | 파이썬 기본 함수/방법 |     비고    |
| :---------: | :----------: | :-------: |
|     push    |  `append(x)` |  맨 뒤에 추가  |
|     pop     |    `pop()`   |  맨 뒤 꺼내기  |
|  top(peek)  |    `[-1]`    |  맨 뒤 값 확인 |
|     size    | `len(stack)` |           |
| empty check |  `not stack` | 빈 스택 True |
|    clear    |   `clear()`  |   전체 비우기  |


# 큐 (Queue)
## 개념
- 데이터를 **줄세우는 구조**
- 먼저 넣은 데이터가 먼저 나오는 구조

  (FIFO: First In First Out)
## 주요 연산
- **enqueue**: 데이터 넣기(뒤에 추가)

- **dequeue**: 데이터 꺼내기(앞에서 제거)

- **front/peek**: 맨 앞의 데이터 확인

<br><br>
ps. [우선순위 큐](../week_2word/priority_queue.md)

## 예시
- 상식적으로 줄 섰을때

- 편의점 선입선출

```
Queue (front -> rear):

front                        rear
  |                            |
  v                            v
+-----+  +-----+  +-----+  +-----+
|  1  |  |  2  |  |  3  |  |     |
+-----+  +-----+  +-----+  +-----+

(enqueue(3): 뒤에 추가, dequeue: 앞에서 꺼냄)

dequeue()
front                        rear
  |                            |
  v                            v
+-----+  +-----+  +-----+  +-----+
|     |  |  2  |  |  3  |  |     |
+-----+  +-----+  +-----+  +-----+
```


```py
# 파이썬 예시

from collections import deque
queue = deque()
queue.append(1)  # enqueue
queue.append(2)
print(queue.popleft())  # dequeue, 출력: 1
print(queue.popleft())  # dequeue, 출력: 2
```

# 비교

간지나게 표로 정리함

| 구분          | [스택(Stack)](#스택-stack)                  | [큐(Queue)](#큐-queue)                       |
|---------------|------------------------------|---------------------------------|
| 구조          | 쌓기(Last In First Out, LIFO)| 줄세우기(First In First Out, FIFO)|
| 데이터 추가   | push(맨 위에 쌓음)           | enqueue(맨 뒤에 넣음)           |
| 데이터 제거   | pop(맨 위에서 뺌)            | dequeue(맨 앞에서 뺌)           |
| 입출력 방향   | 한쪽(위)만                   | 양쪽(앞에서 꺼내고, 뒤에 넣음)   |
| 예시   | 쓰레기통 뒤질때 | 사람 인체 구조 <br> (입출구 따로 존재함 ※용도 외 사용금지※)        |
