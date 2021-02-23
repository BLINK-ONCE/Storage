# organization 6

# 5.7 Supervised Learning Algorithms

## simply says Supervised Learning Algoritms
- kNN: data point에서 가장 가까운(nearest) Training data point, 최근접 이웃을 찾는 알고리즘. 작은 data set일 경우에 기본모델로서 좋고 이해하기 쉽다.
- linear model: 선형적인 직선이나 평면, 초평면 등을 이용하여 출력을 찾는 알고리즘. 첫 번째로 시도하기 좋으며, 대용량 data set과 high dimension data set에 가능하다.
- naive bayes: 데이터의 특성을 독립적이라 가정하여 각 상황의 확률을 계산하여 결과를 출력한다. 분류 문제에만 적용할 수 있다. 대용량 데이터 셋과 고차원 데이터에 사용가능하다. 선형모델보다 훨씬 빠르나 정확도는 떨어진다.
- decision tree: 데이터를 이진 분류하는 것을 반복하여 최종적으로 결과를 출력한다. 매우 빠르고 데이터 스케일의 조정이 필요 없다. 시각화하기 좋고 설명하기 쉬우나 과대적합되는 경향이 있다.
- random forest: 과대적합된 단일 결정 트리를 여러 개 묶어 하나의 모델로 만든 것. 결정 트리 하나보다 거의 항상 좋은 성능을 낸다. 매우 안정적이고 강력하며 데이터 스케일의 조정이 필요가 없다. 다만 시간이 오래 걸리고 텍스트같은 고차원 희소 데이터에는 잘 맞지 않는다.
- gredient boosting decision tree: 깊이가 깊지 않은 단일 결정 트리를 여러 개 묶어 하나의 모델로 만든 것. 랜덤 포레스트보다 조금 더 성능이 좋다. 랜덤 포레스트보다 학습은 느리나 예측은 빠르고 메모리를 적게 사용한다. 다만 랜덤 포레스트보다 매개변수의 튜닝이 많이 필요하다.
- support vector machine: 클래스 사이의 경계에 위치한 데이터 포인트(서포트 벡터) 간의 거리를 최대화하여 결과를 찾는 알고리즘. 비슷한 의미의 특성으로 이루어진 중간 규모 데이터 세트에는 잘 맞지만, 데이터 스케일의 조정이 필요하고 매개변수에 민감하다.
- neural network: 대용량 데이터 세트에서 매우 복잡한 모델을 만들 수 있다. 다만 매개변수의 선택과 데이터 스케일에 민감하며, 큰 모델에는 학습이 오래 걸린다.





------------

# 추가내용

# 시그모이드 함수
```
sigmoid function
hard sigmoid function
```

- s자형 또는 sigmoid 형태이다. 
- 단조증가 혹은 단조감소이다. 
- 변곡점 1개이다.


# logistic regression
- 목적은 일반적인 회귀 분석의 목표와 동일하다.
- 종속 변수와 독립 변수간의 관계를 구체적인 함수로 나타내어 향후 예측 모델에 사용한다.
- 종속 변수가 범주형 데이터를 대상으로 하며 입력 데이터가 주어졌을 때 해당 데이터의 결과가 특정 분류로 나뉘기 때문에 일종의 분류기법으로도 볼 수 있다.(선형 회귀 분석과 다른 점)



------

# presentation

# 5.7
지도 학습 알고리즘은 입력 예제의 훈련 세트가 주어지면 일부 입력을 일부 출력과 연결하는 방법을 배우는 학습 알고리즘이다.

# 5.7.1 probablistic supervised learning
이 책에 나오는 대부분의 지도 학습 알고리즘은 확률 분포 추정을 기반으로 한다.
MLE를 사용해 최상의 매개 변수 벡터를 찾기만 하면 된다.

선형 회귀는 패밀리다.

다른 확률 분포 패밀리를 정의하여 분류 시나리오에 대한 선형 회귀를 일반화할 수 있다. 이는 베르누이 함수의 특징을 가진다.

선형 회귀에 사용한 실수값에 대한 정규 분포는 평균으로 모수화된다. 

이진 변수에 대한 분포는 항상 0과 1사이여야 하기 때문에 어렵다. 이 경우에는 로지스틱 시그모이드 함수를 사용하여 선형 함수의 출력을 구간(0, 1)로 스쿼시한다. 그리고 그 값을 확률로 해석한다.

선형 회귀의 경우 정규 방정식을 풀어 최적의 가중치를 찾을 수 있다. 

로지스틱 회귀는 조금 어렵다. 최적의 가중치를 위한 확실한 솔루션은 없다.

하지만 log-likelihood를 최대화하여 찾을 수 있다. 또한 Nagative log-likelihood를 최소화하여 찾을 수도 있다.


# 5.7.2 SVM



#5.7.3 other simple supervised learning algorithms

## kNN

## decision tree







----------

# Reference
- [지도학습 알고리즘: 정리](https://kolikim.tistory.com/25)
- [machine learning 실무. 지도 학습 알고리즘 1](https://medium.com/@osm0644/machine-learning-%EC%8B%A4%EB%AC%B4-%EC%A7%80%EB%8F%84-%ED%95%99%EC%8A%B5-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%981-3fba2b0afbd3)
- [머신러닝 - 2. 서포트 벡터 머신(SVM) 개념](https://bkshin.tistory.com/entry/%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D-2%EC%84%9C%ED%8F%AC%ED%8A%B8-%EB%B2%A1%ED%84%B0-%EB%A8%B8%EC%8B%A0-SVM)
- [시그모이드 함수](https://ko.wikipedia.org/wiki/%EC%8B%9C%EA%B7%B8%EB%AA%A8%EC%9D%B4%EB%93%9C_%ED%95%A8%EC%88%98)
- [logistic regression](https://ko.wikipedia.org/wiki/%EB%A1%9C%EC%A7%80%EC%8A%A4%ED%8B%B1_%ED%9A%8C%EA%B7%80)
- [* 머신러닝. 9. 머신러닝 학습 방법(part 4) - SVM(1)](http://blog.naver.com/PostView.nhn?blogId=laonple&logNo=220845107089&categoryNo=31&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=postView)
- [SVM의 사용자로서 꼭 알아야 할 것들. 매개변수 C와 gamma](https://bskyvision.com/163)
- [* ML #7 머신러닝 kNN 알고리즘 장단점](https://muzukphysics.tistory.com/131?category=1111219)
- [* ML #8 머신러닝 SVM 기본 개념과 장단점](https://muzukphysics.tistory.com/135)