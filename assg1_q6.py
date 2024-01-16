import numpy as np
import matplotlib.pyplot as plt
#from scipy.stats import poisson, norm
from scipy import stats

data = np.genfromtxt("D:\EP4130\Assg 1\data.csv", delimiter = ',', skip_header=1)
d1=[]
for i in data: 
    if i>0: 
        d1.append(i)
        
update = stats.boxcox(d1, lmbda=None, alpha=None)
plt.hist(d1, label="given data", bins = 30, width = 0.1)
plt.hist(update, label="Gaussian", bins =30, width = 0.1)
plt.legend()
plt.show()