import pickle
import numpy as np
import os




# Load the data
with open('dataset.pkl', 'rb') as f:
   dataset = pickle.load(f)

# Now create labels and targets for the ML CNN


X,y = np.hsplit(dataset,2)
print(X.shape,y.shape)

new_X = []
for i in range(len(X)):
    new_X.append(X[i][0])

with open('X.pkl', 'wb') as f:
    pickle.dump(np.array(new_X), f, protocol=4)

print("Finished generating training data")

new_y = []
for i in range(len(y)):
    value = y[i][0]
    zeros_1 = np.zeros((64,64))
    zeros_1[value[0],value[1]] = 1
    val = [zeros_1]
    new_y.append(val)

with open('y.pkl', 'wb') as f:
    pickle.dump(np.array(new_y), f, protocol=4)

print("Finished generating target labels")

