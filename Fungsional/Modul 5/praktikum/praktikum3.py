import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# Data tinggi badan individu dalam sentimeter
tinggi_badan = [165, 170, 155, 172, 180, 160, 175, 165, 185, 175, 170, 160] 

# Mengelompokkan tinggi badan ke dalam interval tertentu
bins = range(150, 200, 10)

# Menghitung frekuensi tinggi badan dalam interval
hist, bin_edges = np.histogram(tinggi_badan, bins)

# Visualisasi data dalam bentuk histogram
plt.hist(tinggi_badan, bins, alpha=0.5, color='g', density=True)

# Menambahkan kurva pdf pada hasil visualisasi data
mu, std = norm.fit(tinggi_badan)
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)
plt.plot(x, p, 'r', linewidth=2)

plt.title('Histogram dan PDF Tinggi Badan')
plt.xlabel('Tinggi Badan (cm)')
plt.ylabel('Frekuensi')
plt.show()
