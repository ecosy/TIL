# Sliding Window
> 고정 사이즈의 윈도우가 이동하면서 윈도우 내에 있는 데이터를 이용해 문제를 풀이하는 알고리즘

* 투 포인터와 유사하지만 차이가 있음

이름 | 정렬 여부 | 윈도우 사이즈 | 이동
--- | :---: | :---: | ---
투 포인터 | 대부분 정렬 | 가변 | 좌우 포인터 양방향 이동
슬라이딩 윈도우 | 정렬 X | 고정 | 좌 / 우 한 방향만 이동

* 슬라이딩 윈도우는 2개의 네트워크 호스트 간의 패킷 흐름을 제어하기 위한 방법을 지칭하는 네트워크 용어임.
  * 패킷을 전송할 때 고정 사이즈의 윈도우가 옆으로 이동하면서 그다음 패킷을 전송하는 방식
