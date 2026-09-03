# Dreamhack-study
1 Day 1 Problem 

2026.9.1. Web-ssrf
  1. 문제 개요
     - 내부망(Localhost)의 랜덤 포트(1500~1800)에 숨겨진 'flag.txt'에 접근해 플래그 획득
     - 방어 매커니즘 : netlog를 통해 localhost & 127.0.0.1 문자열 필터링
  2. 공격 기법
     - 대소문자 우회 : netloc이 대소문자 구분하므로 Localhost로 코드 생성
     - requests와 tqdm을 이용해 1500~1800 포트 자동으로 브루트포스 진행
     - PNG 파일의 시그니처를 이용해 열린 포트만 찾을 수 있도록 함
  3. 배운점
     - 블랙리스트 방식의 문자열 매칭 방어는 우회 가능성이 높으므로 화이트리스트 방식의 보안이 필요
     - 직접 파이썬 코드를 짜보고 실행해보는 좋은 기회였음. png 파일의 시그니처에 대해 알게됨

2026.9.2. return to shellcode
  1. 문제 개요
       - 카나리가 적용된 코드에서 return to shellcode를 통해 쉘을 따고 플래그 획득
  2. 공격 기법
       - canary Leak : 더미값을 이용한 bof를 시도해 카나리 값 획득
       - shellcode 생성 및 주입 : asm(shellcraft.sh())를 통해 쉘 코드 생성 및 페이로드 주입
  3. 배운점
       - 카나리의 존재 이유와 버퍼, 카나리, SFP, RET으로 진행되는 메모리 구조
       - 익스플로잇 코드를 직접 짜보고 오류를 직접 찾아 고쳐봄
