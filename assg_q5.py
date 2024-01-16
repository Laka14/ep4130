import numpy as np
#import matplotlib.pyplot as plt
#from scipy.stats import poisson, norm
measurements = np.array([0.8920, 0.881, 0.8913, 0.9837, 0.8958])
uncertainties = np.array([0.00044, 0.009, 0.00032, 0.00048, 0.00045])
weighted_mean = np.sum(measurements / uncertainties**2) / np.sum(1 / uncertainties**2)
error_mean = np.sqrt(1 / np.sum(1 / uncertainties**2))


print("Weighted Mean Lifetime:", weighted_mean)
print("Uncertainty of the Mean:", error_mean)
#plt.plot(x1, g_pdf, label='Gaussian Distribution', alpha=0.7, linestyle='-', color='red')
#plt.plot(x, p_pmf, label='Poisson Distribution', alpha=0.7, linestyle='--', color='blue', marker='o')
#plt.title('Gaussian and Poisson Distributions')
#plt.xlabel('Value')
#plt.ylabel('Probability Density')
#plt.legend()
#plt.show()
