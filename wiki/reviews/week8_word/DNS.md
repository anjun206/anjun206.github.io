# 도메인 네임 시스템 (DNS)
Domain Name System

이것저것 다양하게 나오는데 일단 지금 배운내용 관련해서만 간략히 정리했다

DNS도 뭐 별거 아니고 도메인 이름을 IP주소로 바꿔는 시스템이다<br>
이거 없으면 매번 IP 외워야 하고 IP변경때마다 주소 다시 알아야하고 한단다

## 용어

- **라벨(label)**: 점(`.`)으로 구분된 각 부분. 오른쪽이 상위, 왼쪽이 하위<br>
예) `www.example.com.` → `.`(루트) > `com` > `example` > `www`

- **FQDN (Fully Qualified Domain Name)**: 끝에 점(`.`)까지 포함한 절대 이름<br>
예) `www.example.com.`