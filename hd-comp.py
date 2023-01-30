import random
import numpy as np
from scipy.spatial.distance import hamming
from scipy.stats import binom
import matplotlib.pyplot as plt
import seaborn as sns
d = 10000
d_1 = 1000
d_2 = 100
n = 15000
ham_array_10k=[]
ham_array_1k=[]
ham_array_100=[]
for i in range(n+1):
    arr1 = np.random.randint(2, size=(d))
    arr2 = np.random.randint(2, size=(d))
    ham_array_10k.append(hamming(arr1, arr2))
for i in range(n+1):
    arr1 = np.random.randint(2, size=(d_1))
    arr2 = np.random.randint(2, size=(d_1))
    ham_array_1k.append(hamming(arr1, arr2))
for i in range(n+1):
    arr1 = np.random.randint(2, size=(d_2))
    arr2 = np.random.randint(2, size=(d_2))
    ham_array_100.append(hamming(arr1, arr2))
fig, axes = plt.subplots(2, 2, figsize=(15, 15), sharey=True)
sns.kdeplot(data=np.array(ham_array_10k),ax=axes[0,0],color='blue',label='d=10,000')
sns.kdeplot(data=np.array(ham_array_1k),ax=axes[0,0],color='red',label='d=1,000')
sns.kdeplot(data=np.array(ham_array_100),ax=axes[0,0],color='black',label='d=100')
axes[0,0].set_xlim(0, 1)
axes[0,0].set_ylim(0,100)
axes[0,0].set_ylabel("Probability(%)")
axes[0,0].set_xlabel("Hamming Distance")
axes[0,0].set_title("Hamming Distance for 15,000\nrandomly generated pairs\nof hypervectors of 100, 1,000,\nand 10,000 dimensions",fontsize=10)
axes[0,0].legend()


plt.show()