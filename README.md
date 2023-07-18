# RopeGame
---
다음과 같은 두 연산이 있다.  
연산 A: 1을 더하기  
연산 B: 역수를 취한 뒤 -1을 곱하기  

**매듭이론**이란 매듭이 꼬인 상태를 어떤 유리수에 대응시키는 것이다. 완전히 풀린 줄을 '0'이라 하자.  
이 때 예를 들어, 시계방향으로 세 번 꼬은 뒤 시게방향으로 한 번 회잔한 후 다시 시계방향으로 한 번 꼬은 매듭의 상태는 '-2/3'에 대응한다.  
위에서 정의한 연산은 매듭이론에서 매듭의 꼬임과 회전에 대응하는 연산이다.  
연산 A: 1을 더하기 = 줄을 반시계방향으로 한 번 꼬기  
연산 B: 역수를 취한 뒤 -1을 곱하기 = 줄을 반시계방향으로 한 번 회전하기  
줄을 시계방향으로 꼬은다면 -1을 더하면 된다.  
줄을 시계방향으로 한 번 회전하는 것은 역수를 취하고 -1을 곱하면 된다는 것도 유추할 수 있다.  

이 게임은 이런 연산들을 사용해 매듭을 푸는 것을 목표로 한다.  
만약 매듭의 상태가 -2/3라면, 줄이 완전히 풀린 목표상태 0을 갖기 위해 ABAAA라는 연산을 수행하면 된다.  
  
이 프로그램은 직접 문제상황을 입력받고, 목표상태에 도달하기 위한 연산들을 출력한다.

실행: `python main.py`