import numpy as np
from scipy.spatial.distance import hamming
import matplotlib.pyplot as plt
import seaborn as sns

#Hamming distance for hypervectors of different dimensions
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
fig, axes = plt.subplots(2, 2, figsize=(12, 6), sharey=True, sharex=True)
fig.tight_layout(h_pad=2)
sns.kdeplot(data=np.array(ham_array_10k),ax=axes[0,0],color='blue',label='d=10,000')
sns.kdeplot(data=np.array(ham_array_1k),ax=axes[0,0],color='red',label='d=1,000')
sns.kdeplot(data=np.array(ham_array_100),ax=axes[0,0],color='black',label='d=100')
axes[0,0].set_xlim(0, 1)
axes[0,0].set_ylim(0,100)
axes[0,0].set_ylabel("Probability(%)",fontsize=8)
axes[0,0].set_xlabel("Hamming Distance",fontsize=8)
axes[0,0].set_title("Hamming Distance for 15,000 randomly generated pairs of hypervectors of 100, 1,000,and 10,000 dimensions",fontsize=8)
axes[0,0].legend()

#Hypevector Addition Hamming Distance (3,000 iterations)
d = 10000
n = 3000
def most_frequent(List):
    return max(set(List), key = List.count)
ham_array_A_B=[]
ham_array_A_C=[]
ham_array_B_C=[]
ham_array_X_A=[]
ham_array_X_B=[]
ham_array_X_C=[]
for i in range(n+1):
    arrA = np.random.randint(2, size=(d))
    arrB = np.random.randint(2, size=(d))
    arrC = np.random.randint(2, size=(d))
    arrX = []
    lst = [arrA,arrB,arrC]
    for j in range(d):
        arrT = [item[j] for item in lst]
        arrX.append(most_frequent(arrT))
    ham_array_A_B.append(hamming(arrA,arrB))
    ham_array_A_C.append(hamming(arrA,arrC))
    ham_array_B_C.append(hamming(arrB,arrC))
    ham_array_X_A.append(hamming(arrX,arrA))
    ham_array_X_B.append(hamming(arrX,arrB))
    ham_array_X_C.append(hamming(arrX,arrC))
sns.kdeplot(data=np.array(ham_array_A_B),ax=axes[0,1],color='blue',label='Ham(A,B)')
sns.kdeplot(data=np.array(ham_array_A_C),ax=axes[0,1],color='red',label='Ham(A,C)')
sns.kdeplot(data=np.array(ham_array_B_C),ax=axes[0,1],color='black',label='Ham(B,C)')
sns.kdeplot(data=np.array(ham_array_X_A),ax=axes[0,1],color='orange',label='Ham(X,A)')
sns.kdeplot(data=np.array(ham_array_X_B),ax=axes[0,1],color='green',label='Ham(X,B)')
sns.kdeplot(data=np.array(ham_array_X_C),ax=axes[0,1],color='cyan',label='Ham(X,C)')
axes[0,1].set_xlim(0, 1)
axes[0,1].set_ylim(0,100)
axes[0,1].set_ylabel("Probability(%)",fontsize=8)
axes[0,1].set_xlabel("Hamming Distance",fontsize=8)
axes[0,1].set_title("Hamming Distance for 3,000 additions of three 10,000 dimension random binary hypervectors",fontsize=8)
axes[0,1].legend()

#Hypevector Multiplication Hamming Distance (3,000 iterations)
ham_array_A_B=[]
ham_array_X_A=[]
ham_array_X_B=[]
for i in range(n):
    arrA = np.random.randint(2, size=(d))
    arrB = np.random.randint(2, size=(d))
    arrX = list(a^b for a,b in zip(arrA,arrB))
    ham_array_X_A.append(hamming(arrX, arrA))
    ham_array_X_B.append(hamming(arrX, arrB))
    ham_array_A_B.append(hamming(arrA, arrB))

sns.kdeplot(data=np.array(ham_array_A_B),ax=axes[1,0],color='blue',label='Ham(A,B)')
sns.kdeplot(data=np.array(ham_array_X_A),ax=axes[1,0],color='red',label='Ham(X,A)')
sns.kdeplot(data=np.array(ham_array_X_B),ax=axes[1,0],color='black',label='Ham(X,B)')
axes[1,0].set_xlim(0, 1)
axes[1,0].set_ylim(0,100)
axes[1,0].set_ylabel("Probability(%)",fontsize=8)
axes[1,0].set_xlabel("Hamming Distance",fontsize=8)
axes[1,0].set_title("Hamming Distance for 3,000 multiplications of three 10,000 dimension random binary hypervectors",fontsize=8)
axes[1,0].legend()
plt.show()