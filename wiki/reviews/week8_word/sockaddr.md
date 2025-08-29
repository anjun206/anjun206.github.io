csapp 교재에서 번역도 그렇고 내용도 그렇고 빈약해서 추가했다

# 껍데기 구조체 struct sockaddr

## `struct sockaddr`이 껍데기 구조체인 이유?

- `struct sockaddr`은 **실제 주소 데이터를 담으려 만든 구조체가 아닌,<br>
  주소 취급되는 것의 포인터**를 위한 **공용 인터페이스 타입**이다

- 여러 매개변수 타입을 하나로 고정하기 위해 `struct addr *`(포인터)를 표준으로 잡았다

- **실제 내용은 `addrlen`(길이)와 `sa_family`를 보고 해석**

```perl
sockaddr_in   ┐
sockaddr_in6  ├── (struct sockaddr *) 로 캐스팅 → bind/connect/accept
sockaddr_un   ┘
```

- `sockaddr_in`: IPv4
- `sockaddr_in6`: IPv6
- `sockaddr_un`: 유닉스 도메인

<br>

## 쓰이는 방식

커널/라이브러리는 **포인터(struct sockaddr \*)와 길이(socklen_t)** 를 받아 **그 바이트들을 그대로 복사**

이후 `sa_family`를 보고 어떤 타입인지 해석

`addrlen`을 올바르게 주는게 중요

<br>

## `sockaddr_in *`에 대해서

**IPv4 전용 실제 주소 구조체**다

```c
struct sockaddr_in {
    sa_family_t    sin_family;  // AF_INET ( IPv4라는 뜻 )
    in_port_t      sin_port;    // 16비트, 네트워크 바이트 오더( htons )
    struct in_addr sin_addr;    // 32비트 IPv4 주소( htonl/inet_pton )
    unsigned char  sin_zero[8]; // 패딩
};
```

이번에 사용할 대상이고 말이다