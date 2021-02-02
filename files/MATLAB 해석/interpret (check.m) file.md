# check.m file interpret

매트랩은 명령어 다음 줄에 바로 값을 출력한다.
매트랩에서 세미콜론(;)을 입력한다면 명령어 다음에 값을 출력하지 않는다. 이 이외의 의미는 **없다**.

```
%% SPIKING NEURAL NETWORK FOR HANDWRITING RECOGNITION (MNIST)---UNSUPERVISED LEARNING APPROACH
```
필기 인식을 위한 스파이킹 뉴럴 네트워크. unsupervised learning 적용

```
%% clear data
clc;
clear all;
close all;
```

데이터를 비움

```
%% pre-processing of input images for digits 0,1,2 and 3 with 250 training instances for each digit
num_train=100;  % no of training instances of each image
load P_vs_I_20kT_PW.mat;
load MNIST_Greyscale_0_9.mat; % load MNIST dataset
num_digits=10;   % no of digits used for recognition
```

각 자리마다 250개의 트레이닝 인스턴스에서 얻은 입력값을 각각  0, 1, 2, 3으로 하여 pre-processing.

num_train=100 : 각각의 이미지마다 트레이닝 인스턴스의 개수

load 명령어는 폴더 안에 있는 파일을 불러오는 명령어이다.
각각 "load P_vs_I_20kT_PW.mat", "MNIST_Greyscale_0_9.mat" 파일을 로드했다. (MNIST 데이터 셋)

num_digits=10 : digit은 숫자를 뜻한다. 이 변수는 인식에 사용될 숫자의 개수를 나타낸다. (0~9이므로 10개)

