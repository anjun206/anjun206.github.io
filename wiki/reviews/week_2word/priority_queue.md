# 우선순위 [큐](../week1_word/word_stack.md#큐-queue)(Priority Queue)

## 개념
- 각 데이터마다 우선순위가 있는 큐

- 데이터를 넣을 때는 순서 상관없이 넣지만,

- 꺼낼 때는 항상 우선순위가 가장 높은 값이 먼저 나옴.

<br>

## 큐(Queue)와 차이점
___

|           | 일반 큐 (Queue)          | 우선순위 큐 (Priority Queue) |
| --------- | --------------------- | ----------------------- |
| **출입 방식** | FIFO (먼저 들어온 순서대로 나감) | 우선순위 높은 데이터가 먼저 나감      |
| **예시**    | 줄 서서 차례 기다리기          | 응급실 환자 진료, 할 일 우선 처리 등  |
| **구현 방식** | 배열, 리스트 등             | 힙(Heap), 배열, 리스트 등      |
| **사용 목적** | 순서대로 처리               | 중요한 것부터 빠르게 처리          |

___

<br><br>

## 예시
### 일반 큐
- 줄 서서 버스 타기
    - 먼저 줄 선 사람이 먼저 버스에 탐 (First-In, First-Out)

### 우선순위 큐
- 응급실 환자 진료
    - 도착한 순서와 관계없이, <br>
상태가 심각한(우선순위 높은) 환자부터 진료
    - > 예시 코드:
        ```py
        import heapq

        pq = []
        heapq.heappush(pq, (2, "보통 환자"))   # 우선순위 2
        heapq.heappush(pq, (1, "응급 환자"))   # 우선순위 1 (더 급함)
        heapq.heappush(pq, (3, "경증 환자"))   # 우선순위 3

        while pq:
            print(heapq.heappop(pq))
        ```
        > 출력 :
        ```bash
        (1, '응급 환자')
        (2, '보통 환자')
        (3, '경증 환자')
        ```
<br>

## 정리

일반 큐는 들어온 순서대로,<br>

우선순위 큐는 중요한 것 부터
<br><br>

거창하게 썼지만 이게 끝이다

<br><br>
<br><br>

<script src="https://utteranc.es/client.js"
        repo="anjun206/anjun206.github.io"
        issue-term="pathname"
        label="💬 utterances"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
