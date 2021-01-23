# 5.2 용량, 과적합 및 과소적합 Capacity, Overfitting and Underfitting

## 번역
머신 러닝의 중심 과제는 모델이 교육받은 입력뿐만 아니라 이전에는 볼 수 없었던 새로운 입력에 대해서도 잘 수행해야 한다는 것이다. 이전에 관찰되지 않은 입력에서 잘 수행할 수 있는 기능을 일반화라고 합니다. <br>
일반적으로 기계 학습 모델을 훈련할 때, 우리는 훈련 세트에 액세스할 수 있으며, 훈련 오류라는 훈련 세트에 대한 오류 측정을 계산할 수 있으며, 우리는 이 훈련 오류를 줄일 수 있다. 지금까지 우리가 설명한 것은 단순히 최적화 문제입니다. 머신 러닝과 최적화의 구별되는 점은 테스트 오류라고도 하는 일반화 오류도 낮기를 원한다는 것이다. 일반화 오류는 새 입력에 대한 오류의 예상 값으로 정의됩니다. 여기서 기대치는 시스템이 실제로 직면할 것으로 예상하는 입력의 분포에서 도출된 다양한 입력에 걸쳐 취해진다.<br>
우리는 일반적으로 훈련 세트와 별도로 수집된 예제의 테스트 세트에서 성능을 측정하여 기계 학습 모델의 일반화 오류를 추정한다.<br>

선형 회귀 예제에서는 훈련 오류를 최소화하여 모델을 훈련시켰다. <br>
1/m^(train) || X^(train)w - y^(train) || 2, 2 <br>
하지만 우리는 사실 시험 오류에 대해 신경을 쓰고 있습니다. 1/m^(test) || X^(test)w - y^(test) || 2. 2 <br>


교육 세트만 관찰하게 되면 테스트 세트의 성능에 어떤 영향을 미칠 수 있습니까? 통계 학습 이론 분야는 몇 가지 해답을 제공한다. 훈련과 시험 세트를 임의로 취합한다면 우리가 할 수 있는 일은 정말 거의 없다. 훈련과 테스트 세트가 수집되는 방식에 대해 몇 가지 가정을 할 수 있다면, 우리는 어느 정도 진전을 이룰 수 있습니다. <br>

훈련와 시험 데이터는 데이터 생성 프로세스라고 하는 데이터 세트에 대한 확률 분포에 의해 생성된다. 우리는 일반적으로 집합적으로 i.i.d 가정으로 알려진 일련의 가정을 만든다. 이러한 가정은 각 데이터 세트의 예가 서로 독립적이며, 훈련 세트와 테스트 세트가 서로 동일한 확률 분포에서 도출된 동일한 분포를 따른다는 것이다. 이 가정을 통해 단일 예에 대한 확률 분포를 사용하여 데이터 생성 프로세스를 설명할 수 있습니다. 그런 다음 동일한 분포를 사용하여 모든 훈련 예제와 모든 테스트 예제를 생성합니다. 우리는 이러한 공유 기본 배포를 pdata로 표시된 데이터 생성 배포라고 부른다. 이 확률론적 프레임워크와 i.i.d 가정은 훈련 오류와 시험 오류 사이의 관계를 수학적으로 연구할 수 있게 한다. <br>
훈련과 시험 오류 간에 우리가 관찰할 수 있는 즉각적인 연관성은 무작위로 선택된 모델의 예상 훈련 오류가 해당 모델의 예상 시험 오류와 같다는 것이다. 확률 분포 p(x, y)를 가지고 있고 반복하여 열차 세트와 테스트 세트를 생성한다고 가정합시다. 일부 고정 값 w의 경우, 두 기대 모두 동일한 데이터 세트 샘플링 프로세스를 사용하여 형성되기 때문에 예상되는 훈련 세트 오류는 예상 테스트 세트 오류와 정확히 동일하다. 두 조건 사이의 유일한 차이점은 샘플 데이터 세트에 할당한 이름이다. <br>
물론 기계 학습 알고리듬을 사용할 때 매개 변수를 미리 수정하지 않고 두 데이터 세트를 모두 샘플링한다. 우리는 훈련 세트를 표본으로 추출한 다음, 훈련 세트 오류를 줄이기 위해 매개변수를 선택한 다음, 시험 세트를 표본으로 추출한다. 이 과정에서 예상 시험 오차가 훈련 오차의 예상 값보다 크거나 같습니다. 머신 러닝 알고리듬의 성능을 결정하는 요소는 다음과 같은 능력이다.
- 교육 오류를 작게 만듭니다.
- 훈련과 시험 오차의 차이를 작게 한다.

이 두 요인은 기계 학습의 두 가지 중심 과제인 언더피팅과 오버피팅에 해당한다. 적합성 결여는 모델이 교육 세트에서 충분히 낮은 오차 값을 얻을 수 없을 때 발생합니다. 오버피팅은 훈련 오류와 시험 오류 사이의 간격이 너무 클 때 발생한다. <br>
우리는 모델의 용량을 변경하여 모델의 오버피팅 또는 언더피팅 가능성을 제어할 수 있습니다. 비공식적으로, 모델의 용량은 다양한 기능을 장착할 수 있는 능력입니다. 용량이 작은 모델은 교육 세트를 맞추기가 어려울 수 있습니다. 용량이 큰 모델은 테스트 세트에서 제대로 작동하지 않는 교육 세트의 속성을 암기하여 오버핏할 수 있습니다. <br>
학습 알고리듬의 용량을 제어하는 한 가지 방법은 그 가설 공간, 즉 학습 알고리듬이 해결책으로 선택할 수 있는 함수 집합을 선택하는 것이다. 예를 들어, 선형 회귀 알고리즘에는 입력의 모든 선형 함수의 집합이 가설 공간으로 있습니다. 우리는 선형 회귀 분석을 일반화하여 가설 공간에 단순한 선형 함수가 아닌 다항식을 포함할 수 있다. 이렇게 하면 모델의 용량이 증가합니다. <br>
1도의 다항식은 예측과 함께 이미 친숙한 선형 회귀 모델을 제공한다.
y(^) = b + wx. <br>

선형 회귀 모델에 제공되는 또 다른 특징으로 x 2를 도입함으로써, 우리는 x의 함수로 2차인 모델을 배울 수 있다.
y(^) = b + w(1)x + w(2)x^2. <br>

이 모델은 입력의 2차 함수를 구현하지만 출력은 여전히 매개 변수의 선형 함수이므로 정규 방정식을 사용하여 닫힌 형태로 모델을 훈련시킬 수 있다. 우리는 예를 들어 9도의 다항식을 얻기 위해 x의 더 많은 힘을 추가 기능으로 계속 추가할 수 있다.
y(^) = b (9 Sigma i=1)w(i)x^i. <br> <br>

머신 러닝 알고리듬은 일반적으로 수행해야 하는 작업의 진정한 복잡성과 제공되는 훈련 데이터의 양에 용량이 적합할 때 가장 잘 수행될 것이다. 용량이 부족한 모델은 복잡한 작업을 해결할 수 없습니다. 용량이 큰 모델은 복잡한 작업을 해결할 수 있지만, 용량이 현재 작업을 해결하는 데 필요한 것보다 많을 경우 지나치게 적합할 수 있다. <br>
그림 5.2 는 이 원리를 실제와 같이 보여주고 있다. 우리는 실제 기본 함수가 2차인 문제를 적합시키려고 시도하는 선형, 2차 및 9차 예측 변수를 비교한다. 선형 함수는 실제 기본 문제의 곡면성을 포착할 수 없으므로 적합하다. 도-9 예측 변수는 올바른 함수를 나타낼 수 있지만 훈련 예보다 매개 변수가 많기 때문에 훈련 지점을 정확히 통과하는 다른 함수를 무한히 많이 나타낼 수도 있습니다. 매우 다양한 솔루션이 존재할 때 잘 일반화되는 솔루션을 선택할 가능성은 거의 없습니다. 이 예에서 2차 모델은 작업의 실제 구조와 완벽하게 일치하므로 새로운 데이터에 잘 일반화된다.
 <br>
그림 5.2: 이 예제 교육 세트에 세 가지 모델을 적합합니다. 훈련 데이터는 무작위로 x 값을 샘플링하고 2차 함수를 평가하여 결정적으로 y를 선택하여 합성적으로 생성되었다. (왼쪽) 데이터에 대한 선형 함수는 데이터에 있는 곡면성을 캡처할 수 없기 때문에 적합도가 낮습니다. (중앙)데이터에 적합된 2차 함수는 보이지 않는 점으로 잘 일반화됩니다. 과적합 또는 과소적합은 유의하지 않습니다. (오른쪽) 데이터에 대한 9도 다항식의 과적합은 과적합입니다. 여기서 우리는 무어-펜로즈 의사 역수를 사용하여 결정되지 않은 정규 방정식을 해결했다. 해결책은 모든 훈련 포인트를 정확히 통과하지만, 우리는 그것이 정확한 구조를 추출할 만큼 운이 좋지 못했다. 그것은 이제 진정한 기본 기능에 나타나지 않는 두 훈련 지점 사이에 깊은 골짜기를 가지고 있다. 또한 데이터의 왼쪽에서 급격히 증가하는 반면, 이 영역에서는 실제 함수가 감소합니다. <br> <br>

지금까지 모델의 용량을 변경하는 한 가지 방법만 설명했는데, 모델의 입력 기능 수를 변경하고 이러한 기능과 관련된 새 매개 변수를 동시에 추가하는 것이다. 사실 모델의 용량을 변경하는 방법은 여러 가지가 있습니다. 용량은 모델의 선택에 의해서만 결정되는 것이 아닙니다. 이 모델은 학습 목표를 줄이기 위해 매개 변수를 변경할 때 학습 알고리듬이 선택할 수 있는 기능 제품군을 지정한다. 이를 모델의 표현 능력이라고 합니다. 많은 경우, 이 제품군 내에서 최상의 기능을 찾는 것은 매우 어려운 최적화 문제입니다. 실제로 학습 알고리듬은 실제로 최상의 기능을 찾는 것이 아니라 훈련 오류를 크게 줄이는 기능만 찾는다. 최적화 알고리듬의 불완전성과 같은 이러한 추가 제한은 학습 알고리듬의 유효 용량이 모델군의 표현 능력보다 작을 수 있다는 것을 의미한다. <br>
기계 학습 모델의 일반화를 개선하는 우리의 현대적인 아이디어는 적어도 프톨레마이오스만큼 일찍이 철학자로 거슬러 올라가는 사고의 개선이다. 많은 초기 학자들은 현재 가장 널리 알려진 오캄의 면도칼(1287년경-1347년경)로 알려진 파시모니의 원리를 발동한다. 이 원칙은 알려진 관측치를 동등하게 잘 설명하는 경쟁 가설 중에서 가장 단순한 것을 선택해야 한다고 명시한다. 이 아이디어는 통계 학습 이론의 창시자들에 의해 20세기에 공식화되고 더 정확하게 만들어졌다. (Vapnik and Chervonenkis, 1971; Vapnik, 1982; Blumer et al., 1989; Vapnik, 1995) <br>
통계 학습 이론은 모델 용량을 정량화하는 다양한 수단을 제공한다. 이 중에서 가장 잘 알려진 것은 Vapnik-Chervonenkis 치수 또는 VC 치수이다. VC 차원은 이진 분류기의 용량을 측정합니다. VC 치수는 분류기가 임의로 레이블을 지정할 수 있는 m 서로 다른 x 점의 훈련 세트가 존재하는 m의 가능한 가장 큰 값으로 정의됩니다. <br>
모델의 용량을 정량화하면 통계 학습 이론이 정량적 예측을 할 수 있다. 통계 학습 이론에서 가장 중요한 결과는 훈련 오류와 일반화 오류 사이의 불일치가 모델 용량이 증가할수록 증가하지만 훈련 예제의 수가 증가할수록 줄어드는 양으로 위에서 제한된다는 것을 보여준다(Vapnik and Chervonenkis, 1971;
apnik, 1982; Blumer 등, 1989; Vapnik, 1995). 이러한 한계는 머신 러닝 알고리듬이 작동할 수 있다는 지적 정당성을 제공하지만 딥 러닝 알고리듬으로 작업할 때는 실제로 거의 사용되지 않는다. 이는 부분적으로는 한계가 상당히 느슨한 경우가 많기 때문이며, 부분적으로는 딥 러닝 알고리듬의 용량을 결정하는 것이 상당히 어려울 수 있기 때문이다. 딥 러닝 모델의 용량을 결정하는 문제는 유효 용량이 최적화 알고리듬의 기능에 의해 제한되고 딥 러닝과 관련된 매우 일반적인 비볼록 최적화 문제에 대한 이론적 이해가 거의 없기 때문에 특히 어렵다. <br>
단순한 함수가 일반화될 가능성이 더 높지만(훈련과 시험 오류 사이에 작은 차이를 가지기 위해) 여전히 훈련 오류를 낮게 달성할 수 있는 충분히 복잡한 가설을 선택해야 한다는 점을 기억해야 한다. 일반적으로 훈련 오류는 모델로서 가능한 최소 오차 값으로 점증할 때까지 감소합니다.
용량이 증가합니다(오류 측정값이 최소값인 경우). 일반적으로 일반화 오류는 모델 용량의 함수로 U자형 곡선을 가진다. 이는 그림 5.3에 예시되어 있다. <br>
임의적으로 용량이 큰 가장 극단적인 사례에 도달하기 위해 그림 5.3: 용량과 오류 사이의 일반적인 관계를 소개한다. 교육 오류와 테스트 오류는 다르게 작동합니다. 그래프의 왼쪽 끝에는 교육 오류와 일반화 오류가 모두 높습니다. 이것은 가장 적합하지 않은 정권이다. 용량을 늘리면 훈련 오류는 줄어들지만 훈련과 일반화 오류 간 격차는 커진다. 결국, 이 격차의 크기는 훈련 오류의 감소를 능가하며, 우리는 용량이 너무 큰 과적합 시스템에 최적 용량 이상으로 진입한다. <br> <br>

비모수 모델의 개념 지금까지는 선형 회귀와 같은 모수 모델만 보아 왔다. 매개 변수 모델은 데이터가 관측되기 전에 크기가 유한하고 고정된 매개 변수 벡터에 의해 설명되는 함수를 학습한다. 비모수 모형에는 이러한 제한이 없습니다. <br>
때때로 비모수 모델은 실제로 구현될 수 없는 이론적 추상화(모든 가능한 확률 분포를 검색하는 알고리즘 등)일 뿐이다. 그러나, 우리는 또한 그 복잡성을 훈련 세트 크기의 함수로 만들어 실용적인 비모수 모델을 설계할 수 있다. 이러한 알고리즘의 한 예는 가장 가까운 인접 회귀 분석입니다. 무게의 고정된 길이 벡터를 갖는 선형 회귀와는 달리, 가장 가까운 인접 회귀 모델은 훈련 세트의 X와 Y를 간단히 저장한다. 검정 점 x를 분류하도록 요청하면 모형은 교육 세트에서 가장 가까운 항목을 찾아 관련 회귀 분석 대상을 반환합니다. 즉, y = yi 여기서 i = argmin ||Xi,: - x||22. 알고리즘은 학습된 거리 메트릭과 같은 L2 표준 이외의 거리 메트릭으로 일반화할 수도 있다(Goldberger et al., 2005). 알고리즘이 모든 Xi에 대한 yi 값(가장 가까운 Xi에 대해 같은 값)을 평균하여 동점을 끊을 수 있는 경우
그의 알고리듬은 회귀 데이터 세트에서 가능한 최소 훈련 오류(두 개의 동일한 입력이 서로 다른 출력에 연결된 경우 0보다 클 수 있음)를 달성할 수 있다. <br>
마지막으로, 필요에 따라 매개 변수의 수를 늘리는 다른 알고리듬 내부에 매개 변수 학습 알고리듬을 래핑하여 비모수 학습 알고리듬을 생성할 수도 있다. 예를 들어, 우리는 입력의 다항식 확장 위에 선형 회귀에 의해 학습된 다항식의 정도를 변경하는 학습의 외부 루프를 상상할 수 있다. <br>
이상적인 모델은 단순히 데이터를 생성하는 실제 확률 분포를 아는 오라클입니다. 그러한 모델도 여전히 분포에 약간의 잡음이 있을 수 있기 때문에 많은 문제에 약간의 오류가 발생할 것이다. 감독 학습의 경우, x에서 y까지의 매핑은 본질적으로 확률적일 수도 있고, y는 x에 포함된 변수 외에 다른 변수를 포함하는 결정론적 함수일 수도 있다. 실제 분포 p(x, y)에서 예측되는 오라클에 의해 발생하는 오류를 베이즈 오류라고 합니다. <br>
교육 세트의 크기가 달라짐에 따라 교육 및 일반화 오류가 달라집니다. 교육 예제의 수가 증가함에 따라 예상되는 일반화 오류는 결코 증가할 수 없다. 비모수 모델의 경우, 가능한 한 최고의 오차가 달성될 때까지 더 많은 데이터가 더 나은 일반화를 산출한다. 최적 용량보다 작은 고정 모수 모형은 베이즈 오류를 초과하는 오류 값으로 점증합니다. 그림은 그림 5.4를 참조한다. 모델이 최적의 용량을 가지면서도 훈련 오류와 일반화 오류 사이에 큰 차이가 있을 수 있다는 점에 유의한다. 이 상황에서, 우리는 더 많은 훈련 사례를 수집함으로써 이 격차를 줄일 수 있을 것이다.


## 정리

### 머신러닝의 과제
model은 train된 input 말고도 test set에도 잘 수행해야한다. generalization. 

선형 회귀 예제에서 보면 트레이닝 에러를 최소화해서 모델을 훈련시켰다. 하지만 우리가 따진 건 트레이닝 에러다. 이 트레이닝 셋이랑 테스트 셋이 임의로 생긴 거라면 우리가 할 수 있는 건 없지만 이것들이 만들어지는 과정과 방식에 대해 몇 가지 결정, 가정을 한다면 어느정도 에러를 줄일 수 있다.

### 트레이닝 셋, 테스트 셋
트레이닝 셋과 테스트 셋은 데이터 제네레이팅 프로세스라고 하는 데이트 셋에 대한 확률 분포에 의해 생긴다. 

i.i.d 가정으로 생겨난 것에서는 데이터 생성 프로세스가 테스트 셋과 동일하기 때문에 트레이닝 에러와 테스트 에러(generalization error)가 동일하다. 하지만 현실에서는 그런 경우는 거의 불가능하다.

그럼 현실에서는 어떻게 할까? 트레이닝 셋과 테스트 셋을 모두 샘플링한다.

샘플링된 트레이닝 셋에서 에러를 줄이기 위해 매개변수(parameter)를 선택한 다음, 테스트 셋을 샘플링한다. 이 과정에서 예상 테스트 에러가 트레이닝 에러 예상 값보다 크거나 같다. 여기서 머신러닝 알고리즘의 성능을 결정하는 요소는 다음과 같다.
- 트레이닝 에러를 작게 한다.
- 트레이닝 에러와 테스트 에러의 차이를 작게 한다.
이것은 머신러닝의 두 가지 중심 과제인 언더피팅과 오버피팅에 해당한다.
- 언더피팅: 모델이 트레이닝 셋에서 충분히 낮은 오차 값을 얻을 수 없을 때 발생한다.(바이어스 크고, 분산 작음)
- 오버피팅: 트레이닝 에러와 테스트 에러 사이의 간격이 너무 클 때 발생한다.(바이어스 작고, 분산 큼)

언더피팅된 모델은 용량이 작아 트레이닝 셋을 충분히 담아낼 수 없다. 오버피팅된 모델은 용량이 너무 커서 트레이닝 셋에서 세부적인 것까지 담아버린다. (모델의 다항식의 차수)

모델의 용량을 변경하는 것은 다항식의 차수만이 있는 것은 아니다.



# reference 
- [underfitting, overfitting 1](https://nittaku.tistory.com/289)
- [underfitting, overfitting 2](https://velog.io/@tmddn0311/%EB%94%A5%EB%9F%AC%EB%8B%9D-%ED%8A%9C%ED%86%A0%EB%A6%AC%EC%96%BC-%EC%98%A4%EB%B2%84%ED%94%BC%ED%8C%85-%EB%B0%A9%EC%A7%80)
- [curse of dimensionality](https://thesciencelife.com/archives/1001)