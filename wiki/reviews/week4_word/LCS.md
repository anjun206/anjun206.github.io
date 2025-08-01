<br><br><br>
LCS.
<br><br><br>
Longest Common Subsequence라는 뜻(meaning이라는 뜻)이다
<br><br><br>
...
<br><br><br>
음?
<br><br><br><br>
아.
<br><br><br>
이런... 실수로 영어가 튀어 나왔군요 my mistake~
<br><br><br>
외국에서 대략 20-yeasr 간 living~한터라 understand 바랍니다
<br><br><br>

# LCS
최장 공통 부분 수열이라는 뜻이다

걍 문자 그대로 이해하면 된다

두 시퀀스(문자열 또는 리스트 등)에서 순서를 유지한 채로 공통적으로 나타나는<br>
**가장 긴 부분 수열을 찾는 거다**

보통은 다이나믹 프로그래밍으로 해결한다

[다이나믹 프로그래밍](../week4_word/DP.md)이 궁금한 자는 나에게로...

## 개념
그래서 최장 공통 부분 수열이 뭐냐? 하면

예시로 알아보자

- $A$ : A `B` `C` `D` E `F`

- $B$ : G `B` `C` `D` `F` E

가 있다고 하면

최장 공통 부분 수열은

`B` `C` `D` `F`다<br>
순서를 유지하는 공통된 수열 중에서 가장 큰 거니 말이다

굳이 연속될 필요는 없다만 순서는 꼭 지켜야 한다

비슷한 걸로 [LCS](LCS2)가 있다

얜 최장 공통 문자열이란 뜻으로

Subsequence 대신 Substring을 사용한다

## 특징

부분 문자열과 달리 연속될 필요 없다

LCS는 주로 [동적 계획법](DP.md)으로 자주 해결한다

시간 복잡도는 $O(n * m)$다

$n, m$ 문자열 $a,b$ 의 길이

<br>

## 예시

**두 문자열의 LCS**를 구해보자

```py
def lcs(a, b):
    n, m = len(a), len(b)
    dp = [[0]*(m+1) for _ in range(n+1)]
```
- 일단 2차원 DP테이블을 채운다

<br><br>

```py
for i in range(n):
    for j in range(m):
        if a[i] == b[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
```

- `dp[i+1][j+1]`는 `a[0:i]`와 `b[0:j]`까지의 LCS 길이를 의미

- 문자가 같다면: 이전 LCS 길이 + 1

- 다르면: 두 선택지 중 큰 값

<br><br>

이제 만든 테이블로 역추적해 LCS를 만들어야 한다

```py
i, j = n, m
result = []
while i > 0 and j > 0:
    if a[i-1] == b[j-1]:
        result.append(a[i-1])
        i -= 1
        j -= 1
    elif dp[i - 1][j] >= dp[i][j - 1]:
        i -= 1
    else:
        j -= 1
```

- `dp` 테이블 끝에서 시작해서,

- 공통 문자를 발견하면 `result`에 추가하고 좌상단으로 이동

- 문자가 다르면 더 큰 쪽 방향으로 이동

<br><br>

최종 반환
```py
return ''.join(reversed(result))
```

- 주의할 점은 역추적한거라 **마지막에 뒤집어줘야 정순**으로 나온다

<br><br>

### 최종 코드
```py
def lcs(a, b):
    n, m = len(a), len(b)
    # LCS 길이 저장할 DP 테이블 초기화
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # DP 테이블 채우기
    for i in range(n):
        for j in range(m):
            if a[i] == b[j]:  # 문자가 같으면 왼쪽 위에서 +1
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:  # 아니면 왼쪽 또는 위쪽 중 큰 값 선택
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

    # LCS 문자열 역추적
    i, j = n, m
    result = []
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:  # 같은 문자면 결과에 추가하고 좌상단 이동
            result.append(a[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:  # 위쪽 값이 크면 위로 이동
            i -= 1
        else:  # 왼쪽 값이 크면 왼쪽으로 이동
            j -= 1

    # 결과는 거꾸로 되어 있으므로 뒤집어서 반환
    return ''.join(reversed(result))
```