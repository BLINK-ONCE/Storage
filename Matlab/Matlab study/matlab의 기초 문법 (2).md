# matlab의 기초 문법 (2)

## M-file 만들기

매트랩을 이용해 원하는 기능을 수행하는 방법은 크게 두 가지로 구분된다.

- Command window에 직접 명령어를 입력하는 방법
- 스크립트(Script) 파일을 이용하는 것


매트랩에서 사용하는 파일을 보통 M-file 이라고 부르며 파일의 확장자는 .m으로 저장된다.

```
스크립트 파일은 여러 개의 명령어가 저장된 파일이며, 순차적으로 실행됩니다.


스크립트 파일 명이 ex.m이라고 하면,


Command Window에서 스크립트 파일을 실행하려면 F5를 누르거나,


다음과 같이 입력합니다.

 >>ex

스크립트 파일을 수정 시에는 다음과 같이 입력합니다.

 >>edit ex.m`

```

스크립트를 이용해 코드를 작성하는 것이 편하고, 수정도 쉽다.


## for ~ end 문

```matlab
for 변수명=초기값:(증분:)최종값
	문장
end
```

- 예) 1부터 10까지 홀수들의 합을 구하는 코드

```matlab
s=0 % sum이라고 하면 안 됩니다. sum이라는 함수이름이 존재하기 때문입니다.
for x=1:2:10 % x는 1부터 10까지 2씩 증가한다.
	s=s+x;
end
s
```

## if ~ else ~ end 문

```matlab
if 조건 1
   문장 1
elseif 조건 2
   문장 2
else
   문장 3
end
```

- 예) 2차방정식이 주어졌을 때 근을 구하는 코드

```matlab
a=1; b=2; c=3; % ax^2+bx+c=0
D=b^2-4*a*c; % 판별식

if D>0
	x1=(-b+sqrt(D))/(2*a); x2=(-b-sqrt(D))/(2*a);
elseif D==0
	x1=-b/(2*a); x2=-b/(2*a);
else
	x1=(-b+sqrt(-D)i)/(2*a); x2=(-b-sqrt(-D)i)/(2*a);
end
x=[x1 x2];
x
```


## while ~ end

```matlab
while 조건
   문장
end
```


- 예) 1부터 100보다 작은 수 중 소수를 판별해 배열로 출력하는 코드

```matlab
A=[];
N=100;
i=1;
while i<N
	if isprime(i) % isprime은 소수인지 판별해주는 MATLAB 내의 함수
		A=[A i];
	end
	i=i+1;
end
A
```


아래와 같이 배열에 원소를 추가할 수도 있다.

```matlab
N=100;
i=1;
j=1;
while i<N
	if isprime(i) 
		A(1,j)=i;
		j=j+1;
	end
	i=i+1;
end
```


## linspace 문

linspace는 a와 b사이의 간격이 동일한 n개의 성분을 갖는 벡터를 만드는 데 사용된다.

```matlab
linspace(a,b,n)
linspace(시작점,끝점,점의 총수)
```

linspace는 구간을 나눌 때 용이한 함수이다.

- 예)

```matlab
 >>x=linspace(0,5,6)
 x = 0   1   2   3   4   5
```


- 예) 101부터 -2씩 감소시켜 100개의 성분을 갖는 벡터

```matlab
linspace(101,-97,100) % 101부터 -97까지 100등분 하면 -2가 됩니다.
```

## 매트랩에서 미리 정의해 둔 변수 (convention)

```matlab
i,j : 허수 단위를 나타냅니다. 

따라서 for문을 쓸 때 index를 i를 사용하는 경우가 많은데 조심하여야합니다.


NaN : 숫자가 아님, Not a Number의 약자로써 부정 혹은 불능 값을 나타냅니다.

예를들어 0/0이나 Inf/Inf 그리고 Inf-Inf 값이 NAN이 됩니다.


Inf : 무한대


pi : 원주율 
```


## function

매트랩도 다른 언어와 마찬가짖로 반환 값이 있는 함수가 존재한다. 스크리브 파일명과 함수 명을 같게 저장해서 함수를 정의할 수 있다. (함수 M-file) 

- 예) 이전 예시에 있던 매트랩 내부에 정의된 함수인 isprime을 function을 이용해 정의

```matlab
function y=my_isprime(n)
if n==1
	y=false;
	return
end
for i=2:sqrt(n)
	if mod(n,i)==0
		y=false;
		return
	end
end
y=true;
return
```

여기서 주의할 점

> 다른 언어와 다르게 세미콜론(;)은 오로지 <br>
> 출력을 하지 않는 용도로 쓰인다.


그렇기에 return 과 같은 곳에 ;을 붙이면 안 된다.


- 예) 어떤 수의 약수를 배열로 반환하는 코드, 함수
```matlab
function A=divisor(n)
A=[];
for i=1:1:n
	if mod(n,i)==0
		A=[A i];
	end
end
return
```

command window에서 실행은 아래와 같이 한다.
```matlab
>>my_isprime(3)
 1

 >>divisor(8)
 A = 1   2   4   8
```

## inline 함수
단순히 인자를 대입해 계산하는 함수는 function을 이용하기보다는 inline 함수를 사용하는 것이 좋다.

```matlab
%inline 함수

f=inline('x^3+2*x+1','x');

 >>f(1)
 ans = 4

%C++의 인라인 함수처럼 단순 치환 형태입니다~
```

eval 을 이용해도 위와 동일한 결과를 얻을 수 있다.

```matlab
%eval

f='x^3+2*x+1'; x=2;
eval(f)
```


## find
find를 이용하면 주어진 조건을 만족하는 index를 손쉽게 찾을 수 있다.
```matlab
x=[1 2 3 5 8]; y=[0 2 1 4 9];
find(x<=y)

%프로그램 실행 결과

ans = 2   5    % x의 2번째,5번째 원소가 y의 2번째,5번째 원소보다 작으므로 그 인덱스 출력
```

index를 이용해 값에도 접근할 수 있다.
```matlab
>>x(5)
 ans = 8
```

## file I/O

매트랩은 외부의 파일에 데이터를 쓰고 가져올 수도 있다.
```matlab
fp=fopen('test.m','w');   % test.m란 파일을 쓰기용으로 생성
fprintf(fp, '%d %d\n',1,2);  % 파일에 1 2 쓰기
fprintf(fp, '%f %f\n,3.5,4.5); % 파일에 3.5 4.5 쓰기
fclose(fp); %파일 close
```

C언어의 파일입출력과 비슷하다.

파일을 열었다면 꼭 닫아주어야 한다.


## 추가적인 내용
매트랩에서도 논리 연산(AND, OR)이 가능하다. 

실수벡터 또한 논리 연산이 가능하다.

```matlab
x=[1 0 0]; %실수 벡터

x=logical(x); %논리 벡터로 변환

y=logical([0 1 1]);

 >>x&y  %AND 연산
 ans = 0   0   0

 >>x|y %OR 연산 
 ans = 1   1   1
```


매트랩에서 모르는 함수는 도움말을 통해 알아볼 수 있다.

for statement 는 시간이 많이 걸리기 때문에 도움말을 통해 매트랩 내장함수가 있는지 꼭 확인해야 한다.

```matlab
% for 문에 열 벡터도 들어갈 수 있습니다.

for I=eye(4,3)
	disp(I)  %disp는 인자를 그대로 출력시키는 함수입니다.
end

% eye의 열을 차례대로 출력하게 됩니다. 

 I = 
      1
      0
      0
      0
      
 I = 
      0
      1
      0
      0
      
I = 
      0
      0
      1
      0


% find 함수 이해

 >>x=[1 0 2;0 1 1;0 0 4]
 x = 
      1   0   2
      0   1   1
      0   0   4

 >>k=find(x) % x의 열부터 차례대로 0이 아닌 값이 있는 인덱스를 출력합니다.
 k = 
     1
     5
     7
     8
     9 


% 0이 있는 인덱스를 찾고 싶으면 다음과 같이 입력합니다.

 >>find(~x); or find(x==0);
```









# Reference
- [matlab의 기초 문법 (2)](https://kookyungmin.github.io/language/2017/09/06/matlab02/)

