# check.m file interpret

매트랩은 명령어 다음 줄에 바로 값을 출력한다.
매트랩에서 세미콜론(;)을 입력한다면 명령어 다음에 값을 출력하지 않는다. 이 이외의 의미는 **없다**.


```
%% SPIKING NEURAL NETWORK FOR HANDWRITING RECOGNITION (MNIST)---UNSUPERVISED LEARNING APPROACH
```
필기 인식을 위한 스파이킹 뉴럴 네트워크. unsupervised learning 적용


## cleat data

```
%% clear data
clc;
clear all;
close all;
```

데이터를 비움

## pre-processing. 0, 1, 2, 3의 숫자로 이루어진 인풋이미지를 마련한다. 

```
%% pre-processing of input images for digits 0,1,2 and 3 with 250 training instances for each digit
num_train=100;  % no of training instances of each image
load P_vs_I_20kT_PW.mat;
load MNIST_Greyscale_0_9.mat; % load MNIST dataset
num_digits=10;   % no of digits used for recognition
```

- 각 자리마다 250개의 트레이닝 인스턴스에서 얻은 입력값을 각각  0, 1, 2, 3으로 하여 pre-processing.
- num_train=100 : 각각의 이미지마다 트레이닝 인스턴스의 개수
- load 명령어는 폴더 안에 있는 파일을 불러오는 명령어이다.
각각 "load P_vs_I_20kT_PW.mat", "MNIST_Greyscale_0_9.mat" 파일을 로드했다. (MNIST 데이터 셋)
- num_digits=10 : digit은 숫자를 뜻한다. 이 변수는 인식에 사용될 숫자의 개수를 나타낸다. (0~9이므로 10개)


```
temp=diag(ones(1,num_digits));
y=[];           % label for each image
```

- diag() func : 대각 행렬을 생성하거나 행렬의 대각선 요소 가져오기 (영단어 diagonal)
- 대각 행렬(diagonal matrix) : 주대각선 성분이 아닌 모든 성분이 0인 정사각 행렬.
- ones() func : 모두 1로 구성된 배열 생성
- temp=diag(ones(1,num_digits)) : 1부터 num_digits까지의 크기를 가지는 모두 1로 구성된 대각 행렬을 temk에 저장
- y=[] : 각 이미지마다 레이블링


```
for i=0:num_train-1
    x(1+num_digits*i,:)=Zero(:,1+i);
    x(2+num_digits*i,:)=One(:,1+i);
    x(3+num_digits*i,:)=Two(:,1+i);
    x(4+num_digits*i,:)=Three(:,1+i);
    x(5+num_digits*i,:)=Four(:,1+i);
    x(6+num_digits*i,:)=Five(:,1+i);
    x(7+num_digits*i,:)=Six(:,1+i);
    x(8+num_digits*i,:)=Seven(:,1+i);
    x(9+num_digits*i,:)=Eight(:,1+i);
    x(10+num_digits*i,:)=Nine(:,1+i);    
    
    y=[y;temp];
end;
```

- for i=0:num_train-1 : 트레이닝 수만큼 for statement
- 잘 모르겠지만 아마 프리 프로세싱 하는 것 같음
- 인풋 이미지들이 아마 레이블링 돼 있는 이미지일 건데
- 이 이미지들을 스파이킹 정보로 바꾸어주는 것인듯 

## 스파이크 형태로 저장된 인풋 이미지들

```
%% images applied as input spike trains and synaptic weights modified by STDP

% Fixed parameters
timeStepS = 1;                          % 1 msec
epochs = num_train*num_digits;          % No of training epochs
InNeurons = size(x,2);                  % No of input neurons
num_PF=0;
```

- images applied as input spike trains and synaptic weights modified by STDP : 인풋 스파이크 훈련 데이터(레이블)가 적용된 이미지. STDP를 통해서 시냅틱 가중치가 적용된 이미지. 
- Fixed parameters : 고정된 파라미터들이다. 각각, (timeStepS, epochs, InNeurons, num_PF)
- timeStepS = 1 : 타임스텝의 시간은 1미리초이다.
- epochs : 트레이닝 에포크의 수
- InNeurons = size(x,2) : 인풋 뉴런의 개수
- size() func : 배열 크기.

```
% Tunable parameters

OpNeurons = 10;                         % No of output neurons
durationS = 290;                         % 40 msec simulation for each image
tau_EPSP = 50;                               % EPSP/STDP response time in msec


Inh = 500;                                % Inhibitory strength
K_leak = 0.018;
Kconst = 300;


Ki = .05e05;                                 % scaling factor for probability
Kf = .05e09;
del_K = 0.018;
tau_STDP1 = 4.5;
tau_STDP2 = 5;
tau_Inh = 50;
eta1 = 0.03;                              % Learning rate
eta2 = 0.01;

```

- Tunable parameters : 조정가능한 파라미터
- OpNeurons : 아웃풋 뉴런의 개수
- durationS = 290 : 각각 이미지마다 40미리초의 시뮬레이션을 가지기 때문에 250 + 40 = 290미리초
- STDP(Spike timing dependent plasticity) : 스파이크 타이밍 종속 소성은 뇌의 뉴런 사이의 연결 강도를 조정하는 생물학적 과정이다. 프로세스는 특정 뉴런의 출력 및 입력 동작 전위의 상대적인 타이밍에 따라 연결 강도를 조정한다.
- EPSP(Excitatory postsynaptic potential) : 이온통로가 열리면서 연접 후부로 양이온이 흘러들어가는 것으로 인해 연접후부의 막전위가 일시적으로 탈분극되는 것이다.
- tau_EPSP = 50 : 미리초 단위에서의 EPSP/STDP의 반응속도
- Inh = 500 : Inhibitory strength(억제력). 즉 EPSP들로 인해 활동전위를 일으킨 후에 휴지기 동안 활동전위가 발생하지 않도록 억제한다.
- K_leak = 0.018 : ?
- Kconst = 300 : ?
- Ki = .05e05 : scaling factor for probability. 즉, 확률에 따라 요인(factor)을 조정한다.
- Kf = .05e09 : ?
- del_K = 0.018 : ?
- tau_STDP1 = 4.5 : ?
- tau_STDP2 = 5 : ?
- tau_Inh = 50 : ?
- eta1 = 0.03 : Learning rate
- eat2 = 0.01 : ?


```
sum_weights = zeros(1,OpNeurons);
volt = zeros(OpNeurons);
K = Ki*ones(1,OpNeurons);
weights_e = 0.13*rand(InNeurons,OpNeurons);  % synaptic weight matrix
weights_com = zeros(280,280);
```

- zeros() : 모두 0으로 구성된 배열 생성
- sum_weights = zeros(1,OpNeurons) : 행렬 sum_weights. 1 * OpNeurons 행렬.
- volt = zeros(OpNeurons) : 행렬 volt. 0으로 구성된 OpNeurons * OpNeurons 행렬.
- K = Ki*ones(1,OpNeurons) : 행렬 K. 1*OpNeurons 행렬.
- weights_e = 0.13*rand(InNeurons,OpNeurons) : 시냅틱 가중치 행렬. 난수로 구성된 InNeurons*OpNeurons 행렬 * 0.13.
- weights_com = zeros(280,280) : ?. 0으로 구성된 280*280 행렬.





# Reference
- [rand 함수](https://kr.mathworks.com/help/matlab/ref/rand.html)
- [size 함수](https://kr.mathworks.com/support/search.html?q=size&page=1)
- [ones 함수](https://kr.mathworks.com/help/matlab/ref/ones.html)