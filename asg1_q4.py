import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson, norm
meang= 5
stdg=np.sqrt(5)
meanp = 5
x = np.arange(-15, 15)
x1 = np.linspace(-15,15,1000)
p_pmf = poisson.pmf(x, mu=meanp)
g_pdf = norm.pdf(x1, loc=meang, scale=stdg)
plt.plot(x1, g_pdf, label='Gaussian Distribution', alpha=0.7, linestyle='-', color='red')
plt.plot(x, p_pmf, label='Poisson Distribution', alpha=0.7, linestyle='--', color='blue', marker='*')
plt.title('Gaussian and Poisson Distributions')
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.legend()
plt.show()
