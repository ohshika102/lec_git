import matplotlib.pyplot as plt
import numpy as np

def sigmoid(data):
    return(1/(1+np.exp(-x)))

def softmax(data):
    return(np.exp(data)/np.sum(np.exp(data)))

def tanh(data):
    return((np.exp(data)-np.exp(-data))/(np.exp(data)+np.exp(-data)))

x = np.arange(-5.0, 5.0, 0.1)
y1=sigmoid(x)
y2=softmax(x)
y3=tanh(x)

plt.plot(x, y1,label='sigmoid')
plt.plot(x, y2,label='softmax')
plt.plot(x, y3,label='tanh')
plt.legend()
plt.ylim(-1.2, 1.2)
plt.title("sigmoid,softmax,tanh")
plt.xlabel("input")
plt.ylabel("output")
plt.show()
