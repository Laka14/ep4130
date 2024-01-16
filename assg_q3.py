import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, cauchy
meang=0
stdg=1.5
meanc=0
gammac=1.5
x = np.linspace(-20, 20, 1000)
gaussian_pdf = norm.pdf(x, loc=meang, scale=stdg)
cauchy_pdf = cauchy.pdf(x, loc=meanc, scale=gammac)

plt.plot(x, gaussian_pdf, label='Gaussian Distribution', linestyle='-', color='red')
plt.plot(x, cauchy_pdf, label='Cauchy Distribution', linestyle='--', color='blue')
plt.title('Gaussian and Cauchy Distributions')
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.legend()
plt.show()
