# poisson

어떤 현상과 현상 사이에 걸리는 시간이나 실험 횟수는 푸아송 분포로 모델링 된다. 시간의 절댓값보다는 기다린 시간의 길이가 사건이 벌어질 확률에 영향을 준다던지, 기다리는 시간이 길어질수록 사건 확률이 커지는 것과 같은 받아들일만한 가정들로 모델링하면 푸아송 분포를 얻게된다.

## Poisson distributions

주어진 양수 람다에 대해, 랜덤 변수 x가 다음과 같은 pmf(probability mass function. 확률 질량 함수)를 가질 때 이를 푸아송 분포라고 한다.

이 함수가 pmf가 되는지 확인하기 위해, 총합이 1임을 확인해야 한다.  지수 함수 exponential function의 테일러 급수 Tylor series 로부터 1이 됨을 확인할 수 있다.

## Poisson process

상담 센터에서 고객 불만을 전화로 접수하는 없무를 하는 상황이라고 하자. 전화 접수 횟수를 통계적으로 분석할 때 다음과 같은 특징을 예상할 수 있다.

1. 업무 시작 순간에는 걸려온 전화 수가 없다.
2. 겹치지 않는 시간대에 걸려온 전화 수는 서로 독립이다.
3. 걸려온 전화 수는 시간 길이에만 영향응ㄹ 받는다.
4. 업무 시간이 짧을 때는 전화 수는 시간에 비례한다.
5. 동시에 여러 전화를 처리하지 않는다.

쉽게 말해 일정 시간 동안 발생하는 사건의 수를 나타내는 확률과정

# Reference

- [tistory. poisson dis. poisson process]([https://elementary-physics.tistory.com/138](https://elementary-physics.tistory.com/138))