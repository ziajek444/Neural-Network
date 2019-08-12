#neuron
import math
import random


def sigmoid(x):
  return 1 / (1 + math.exp(-x))


def mnozenie_list(l1,l2):
    if(len(l1) == len(l2)):
        pass
    else:
        raise ValueError
    retVal = []
    for e1,e2 in zip(l1,l2):
        retVal.append(e1*e2)
    return retVal


class neuron:
    def __init__(self,act_fun_def = lambda x : x):
        self.value = None
        self.output = 1
        self.activiation = act_fun_def

    def fit(self,in_values,in_weights):
        if(in_values == None or type(in_values) != list or len(in_values) == 0):
            raise IOError
        else:
            self.value = sum(mnozenie_list(in_values,in_weights[0:len(in_values)]));
            self.output = self.activiation(self.value)

    def getOutput(self):
        return self.output

    def getValue(self):
        return self.value

    def set_act_fun(self,act_fun):
        self.activiation = act_fun

    def set_sigmoid(self):
        self.activiation = sigmoid


class NeuralNetwork:
    def __init__(self):
        # dodac cala siec na raz
        # praca wielowatkowa
        pass


# l_weights's len is obtained by multiply l_input len and l_neurons len.  len(l_weights) = len(l_input) * len(l_neurons)
def do_layer(l_inputs, l_weights, l_neurons, safe_flag=1):
    if bool(safe_flag):
        if len(l_weights) != len(l_inputs) * len(l_neurons):
            raise IOError
    i_len = len(l_inputs)
    i = 0
    j = i_len
    retList = []
    for e1 in l_neurons:
        e1.fit(l_inputs, l_weights[i:j])
        retList.append(e1.getOutput())
        i += i_len
        j += i_len
    return retList



##################### test 1 ####################
print("\n######## test 1 ######")
# 2 inputs
x1 = [2,3]
# 1 layer
layer1 = [neuron(sigmoid)] * 3
weights1 = [0] * len(layer1)*len(x1)
for i in range(len(weights1)):
    weights1[i] = random.uniform(-1.0, 1.0)
# 2 layer
x2 = [0] * len(layer1)
layer2 = [neuron(sigmoid)] * 2
weights2 = [0] * len(layer2)*len(x2)
for i in range(len(weights2)):
    weights2[i] = random.uniform(-1.0, 1.0)
# 3 layer -> 1 output
x3 = [0] * len(layer2)
layer3 = [neuron(sigmoid)]
weights3 = [0] * len(layer3)*len(x3)
for i in range(len(weights3)):
    weights3[i] = random.uniform(-1.0, 1.0)

print(x1)
x2 = do_layer(x1, weights1, layer1)
print(x2)
x3 = do_layer(x2, weights2, layer2)
print(x3)
y = do_layer(x3, weights3, layer3)
print(y)
print("###############\n")


##################### test 2 ####################
print("##### test 2 ########")
# 2 inputs
x1 = [2,3]
# 1 layer (4 neurons)
layer1 = [neuron()] * 4
weights1 = [2,2,2,3,4,5,3,3]
# 2 layer -> 1 output
x2 = [0] * len(layer2)
layer2 = [neuron()]
weights2 = [1,2,2,1]

print(x1)
x2 = do_layer(x1, weights1, layer1)
print(x2)
y = do_layer(x2, weights2, layer2)
print(y)
print("###############\n")


     








