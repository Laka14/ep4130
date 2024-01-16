import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
mean = 1.5
std= 0.5
draws = np.random.normal(mean, std, 1000)
plt.hist(draws, bins=30, density = True, color='red', alpha = 0.6, edgecolor='black', label='Histogram')
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mean, std)
plt.plot(x, p, 'k', linewidth=2, label='PDF')
plt.title('Normal Distribution: Mean = 1.5, Std Dev = 0.5')
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.legend()
plt.show()

sample_mean = np.mean(draws)
sample_variance = np.var(draws, ddof=1)
sample_skewness = np.mean(((draws-sample_mean)/std)**3)
sample_kurtosis = np.mean(((draws-sample_mean)/std)**4)-3
mad = np.median(np.abs(draws - np.median(draws)))
quart, threefourth = np.percentile(draws, [25, 75]) 
sigma_g = 0.74138(threefourth-quart)



print("Sample Mean:", sample_mean)
print("Sample Variance:", sample_variance)
print("Sample Skewness:", sample_skewness)
print("Sample Kurtosis:", sample_kurtosis)
print("Standard Deviation using MAD:", mad)
print("Standard Deviation using sigmaG:", sigma_g)

