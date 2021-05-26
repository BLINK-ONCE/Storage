import random
import math

random.seed(1)

# Activation Function
## Activation
def sigmoid(x):
    return 1.0/(1.0+math.exp(-x))
    
## Sigmoid's Gradient
def grad_sigmoid(x):
    return sigmoid(x)*(1.0-sigmoid(x))

## ReLU
def ReLU(x):
    return max(0,x)

## ReLU's Gradient
def grad_ReLU(x):
    if (x > 0):
        return 1
    else:
        return 0

# Data preprocessing
def predata(data):
    
    x = list()
    
    for i in range(len(data)):
        x.append(data[i][:2])
        
    # one-hot encoding
    y = list()
    for j in range(len(data)):
        label =list()
        if (data[j][2] == 0):
            label.append(0)
            label.append(1)
        else:
            label.append(1)
            label.append(0)
        y.append(label)
        
    return x, y


# Node Class
class Node:
    def __init__(self, front_node) -> None:
        
        self.weight = list()
        self.errors = list()
        self.delta = list()
        self.output = 0.0
        
        for x in range(front_node+1):
            self.weight.append(random.random())
            self.errors.append(0)
            self.delta.append(0)

            
# Sigmoid를 활성함수로 사용하는 MLP
class MLP_Sigmoid:
    def __init__(self, num_input_node, num_hidden_node, num_output_node) -> None:
        
        self.hidden = list()
        self.out = list()
        
        for i in range(num_hidden_node):
            self.hidden.append(Node(num_input_node))
        
        for j in range(num_output_node):
            self.out.append(Node(num_hidden_node))
            
    # Data 한 번에 하나씩 넣어야 함 (스토캐스틱 방식)
    def FeedForward(self, X_train):
        
        # Hidden Layer
        # Node의 수만큼
        for i in range(len(self.hidden)):
            # Input 차원만큼
            for j in range(len(X_train)):
                self.hidden[i].output = self.hidden[i].output + self.hidden[i].weight[j] * X_train[j]
            #Bias
            self.hidden[i].output = self.hidden[i].output + self.hidden[i].weight[-1]
        
        # Output Layer
        # Node의 수만큼
        for i in range(len(self.out)):
            # Input 차원만큼
            for j in range(len(self.hidden)):
                self.out[i].output = self.out[i].output + self.out[i].weight[j] * sigmoid(self.hidden[j].output)
            #Bias Node
            self.out[i].output = self.out[i].output + self.out[i].weight[-1]
    
    def BackPropagation(self, x_train, y_train):
        
        # Output Layer
        # Output Layer의 Node의 수만큼
        for i in range(len(self.out)):
            # Hidden Layer의 Node의 수만큼
            for j in range(len(self.hidden)):
                self.out[i].delta[j] = (sigmoid(self.out[i].output) - y_train[i]) * grad_sigmoid(self.out[i].output)
                self.out[i].errors[j] = self.out[i].delta[j] * sigmoid(self.hidden[j].output)
            ## Bias Node
            self.out[i].delta[-1] = (sigmoid(self.out[i].output) - y_train[i]) * grad_sigmoid(self.out[i].output)
            self.out[i].errors[-1] = self.out[i].delta[-1] * 1
                
        # Hidden Layer
        # Hidden Layer의 Node의 수만큼
        for i in range(len(self.hidden)):
            # Input Layer의 차원 수만큼
            for j in range(len(x_train)):
                delta = 0.0
                # Output Layer의 Node 수만큼
                for h in range(len(self.out)):
                    delta = delta + self.out[h].delta[i] * self.out[h].weight[i]
                self.hidden[i].delta[j] = delta * grad_sigmoid(self.hidden[i].output)
                self.hidden[i].errors[j] = self.hidden[i].delta[j] * x_train[j]
            # Bias Node
            delta = 0.0
            for h in range(len(self.out)):
                delta = delta + self.out[h].delta[i] * self.out[h].weight[i]
            self.hidden[i].delta[-1] = delta * grad_sigmoid(self.hidden[i].output)
            self.hidden[i].errors[-1] = self.hidden[i].delta[-1]
        
    # 각 Node별로 저장한 FeedForward 값을 초기화
    def node_initialize(self):

        # Hidden Layer Node
        for i in range(len(self.hidden)):
            self.hidden[i].output = 0.0
            for a in range(len(self.hidden[i].weight)):
                self.hidden[i].errors[a] = 0.0
                self.hidden[i].delta[a] = 0.0
        
        # Output Layer Node
        for i in range(len(self.out)):
            self.out[i].output = 0.0
            for a in range(len(self.out[i].weight)):
                self.out[i].errors[a] = 0.0
                self.out[i].delta[a] = 0.0
        
    def update(self, lr):
        
        # Hidden Layer의 Node 수만큼
        for i in range(len(self.hidden)):
            # Hidden Layer의 Weight 수만큼
            for j in range(len(self.hidden[i].weight)):
                self.hidden[i].weight[j] = self.hidden[i].weight[j] - lr * self.hidden[i].errors[j]
        
        # Output Layer의 Node 수만큼
        for i in range(len(self.out)):
            # Output Layer의 Weight 수만큼
            for j in range(len(self.out[i].weight)):
                self.out[i].weight[j] = self.out[i].weight[j] - lr * self.out[i].errors[j]

                
# ReLU를 활성함수로 사용하는 MLP
class MLP_ReLU:
    def __init__(self, num_input_node, num_hidden_node, num_output_node) -> None:
        
        self.hidden = list()
        self.out = list()
        
        for i in range(num_hidden_node):
            self.hidden.append(Node(num_input_node))
        
        for j in range(num_output_node):
            self.out.append(Node(num_hidden_node))
            
    # Data 한 번에 하나씩 넣어야 함 (스토캐스틱 방식)
    def FeedForward(self, X_train):
        
        # Hidden Layer
        # Node의 수만큼
        for i in range(len(self.hidden)):
            # Input 차원만큼
            for j in range(len(X_train)):
                self.hidden[i].output = self.hidden[i].output + self.hidden[i].weight[j] * X_train[j]
            #Bias
            self.hidden[i].output = self.hidden[i].output + self.hidden[i].weight[-1]
        
        # Output Layer
        # Node의 수만큼
        for i in range(len(self.out)):
            # Input 차원만큼
            for j in range(len(self.hidden)):
                self.out[i].output = self.out[i].output + self.out[i].weight[j] * ReLU(self.hidden[j].output)
            #Bias Node
            self.out[i].output = self.out[i].output + self.out[i].weight[-1]
    
    def BackPropagation(self, x_train, y_train):
        
        # Output Layer
        # Output Layer의 Node의 수만큼
        for i in range(len(self.out)):
            # Hidden Layer의 Node의 수만큼
            for j in range(len(self.hidden)):
                self.out[i].delta[j] = (ReLU(self.out[i].output) - y_train[i]) * grad_ReLU(self.out[i].output)
                self.out[i].errors[j] = self.out[i].delta[j] * ReLU(self.hidden[j].output)
            ## Bias Node
            self.out[i].delta[-1] = (ReLU(self.out[i].output) - y_train[i]) * grad_ReLU(self.out[i].output)
            self.out[i].errors[-1] = self.out[i].delta[-1] * 1
                
        # Hidden Layer
        # Hidden Layer의 Node의 수만큼
        for i in range(len(self.hidden)):
            # Input Layer의 차원 수만큼
            for j in range(len(x_train)):
                delta = 0.0
                # Output Layer의 Node 수만큼
                for h in range(len(self.out)):
                    delta = delta + self.out[h].delta[i] * self.out[h].weight[i]
                self.hidden[i].delta[j] = delta * grad_ReLU(self.hidden[i].output)
                self.hidden[i].errors[j] = self.hidden[i].delta[j] * x_train[j]
            # Bias Node
            delta = 0.0
            for h in range(len(self.out)):
                delta = delta + self.out[h].delta[i] * self.out[h].weight[i]
            self.hidden[i].delta[-1] = delta * grad_ReLU(self.hidden[i].output)
            self.hidden[i].errors[-1] = self.hidden[i].delta[-1]
        
    # 각 Node별로 저장한 FeedForward 값을 초기화
    def node_initialize(self):

        # Hidden Layer Node
        for i in range(len(self.hidden)):
            self.hidden[i].output = 0.0
            for a in range(len(self.hidden[i].weight)):
                self.hidden[i].errors[a] = 0.0
                self.hidden[i].delta[a] = 0.0
        
        # Output Layer Node
        for i in range(len(self.out)):
            self.out[i].output = 0.0
            for a in range(len(self.out[i].weight)):
                self.out[i].errors[a] = 0.0
                self.out[i].delta[a] = 0.0
        
    def update(self, lr):
        
        # Hidden Layer의 Node 수만큼
        for i in range(len(self.hidden)):
            # Hidden Layer의 Weight 수만큼
            for j in range(len(self.hidden[i].weight)):
                self.hidden[i].weight[j] = self.hidden[i].weight[j] - lr * self.hidden[i].errors[j]
        
        # Output Layer의 Node 수만큼
        for i in range(len(self.out)):
            # Output Layer의 Weight 수만큼
            for j in range(len(self.out[i].weight)):
                self.out[i].weight[j] = self.out[i].weight[j] - lr * self.out[i].errors[j]

# Train
def train(model, dataset, lr, epoch):
        
    X_train, y_train = predata(dataset)
        
    for a in range(epoch):
        MSError = 0.0
            
        for b in range(len(dataset)):
                
            model.FeedForward(X_train[b])
            
            # Output Node의 수만큼
            for c in range(len(model.out)):
                MSError = MSError + (y_train[b][c]-sigmoid(model.out[c].output))**2
                
            model.BackPropagation(X_train[b], y_train[b])
                
            model.update(lr)
            
            model.node_initialize()
            
        if (a % 500 == 0):
            print(f"epoch : {a}, error : {MSError/20:.3f}")