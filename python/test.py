# Test
def test(model, dataset):
    
    X_train, y_train = predata(dataset)
    
    for i in range(len(dataset)):
        
        model.FeedForward(X_train[i])
        
        if ((sigmoid(model.out[0].output) > 0.5) & (sigmoid(model.out[1].output) < 0.5)):
            pred_0 = 1
            pred_1 = 0
        else:
            pred_0 = 0
            pred_1 = 1
        print(f"\n---------------------data[{i}]---------------------------")
        print(f"predict label : [{pred_0} ,{pred_1}]")
        print(f"answer label : [{y_train[i][0]}, {y_train[i][1]}]")
        
        model.node_initialize()