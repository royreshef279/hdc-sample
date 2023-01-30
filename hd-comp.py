import random
import numpy as np
from scipy.spatial.distance import hamming
import matplotlib.pyplot as plt
import seaborn as sns

#Hamming distance distribution of 15,000 random pairs of hypervectors of different sizes
d_0 = 10000
d_1 = 1000
d_2 = 100
n = 15000
ham_array_10k=[]
ham_array_1k=[]
ham_array_100=[]
for i in range(n+1):
    arr1 = np.random.randint(2, size=(d_0))
    arr2 = np.random.randint(2, size=(d_0))
    ham_array_10k.append(hamming(arr1, arr2))
for i in range(n+1):
    arr1 = np.random.randint(2, size=(d_1))
    arr2 = np.random.randint(2, size=(d_1))
    ham_array_1k.append(hamming(arr1, arr2))
for i in range(n+1):
    arr1 = np.random.randint(2, size=(d_2))
    arr2 = np.random.randint(2, size=(d_2))
    ham_array_100.append(hamming(arr1, arr2))
fig, ax = plt.subplots()
sns.kdeplot(data=np.array(ham_array_10k),ax=ax,color='blue',label='d=10,000')
sns.kdeplot(data=np.array(ham_array_1k),ax=ax,color='red',label='d=1,000')
sns.kdeplot(data=np.array(ham_array_100),ax=ax,color='black',label='d=100')
ax.set_xlim(0, 1)
ax.set_ylim(0,100)
plt.ylabel("Probability(%)")
plt.xlabel("Normalized Hamming Distance")
plt.title("Hamming Distance for 15,000 randomly generated pairs of hypervectors of 100, 1,000, and 10,000 dimensions")
plt.legend()
plt.show()