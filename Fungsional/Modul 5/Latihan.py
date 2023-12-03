import matplotlib.pyplot as plt
import numpy as np
from numpy.random import normal
from numpy import mean, std
from scipy.stats import norm
# PERCOBAAN 1

# xpoints = np.array([1, 8])
# ypoints = np.array([3, 10])

# plt.plot(xpoints, ypoints)
# plt.show()

#PERCOBAAN 2
# xpoints = np.array([1, 8, 10])
# ypoints = np.array([3, 10, 5])

# plt.figure(figsize=(5,5))
# plt.plot(xpoints, ypoints, color='green', linestyle='dashed', marker='o', markerfacecolor='blue', markersize=8)
# plt.xlim([0,15])
# plt.ylim([0,15])

# plt.xlabel('Sumbu X') 
# plt.ylabel('Sumbu Y') 
# plt.title('Lalala') 
# plt.legend(['titik sumbu']) # Legenda

# plt.show()

# PERCOBAAN 3
# y1=np.array([1, 8, 10,10])
# y2=np.array([3, 10, 5,11])
# y3=np.array([5, 15, 14,20])
# y4=np.array([10, 20, 19,25])

# plt.plot(y1, label="Garis 1")
# plt.plot(y2, label="Garis 2")
# plt.plot(y3, label="Garis 3")
# plt.plot(y4, label="Garis 4")
# plt.title('plot Dua Garis')
# plt.xlabel('Sumbu X') 
# plt.ylabel('Sumbu Y') 

# plt.title('Lalala') 
# plt.legend() # Legenda seluler
# plt.show()

#PERCOBAAN 4
# x= [1,2,3,4,5]
# y=[3,7,2,8,5]

# plt.figure(figsize=(5,5))
# plt.scatter(x, y, color='red', marker='o')

# # Menambahkan garis dengan fungsi plot
# z = np.polyfit(x, y, 1)
# p = np.poly1d(z)
# plt.plot(x,p(x),"r-") # Mengubah gaya garis menjadi solid dan warna menjadi merah

# plt.xlabel('Sumbu X') # Label sumbu X
# plt.ylabel('Sumbu Y') # Label sumbu Y
# plt.title('Scatter Plot dengan Garis') # Judul plot
# plt.legend(['scatternya', 'Data']) # Legenda

# plt.show()

# PERCOBAAN  5
sample = normal(loc=50, scale=5,size=1000)
sample_mean = mean(sample)
sample_std = std(sample)
dist = norm(sample_mean,sample_std)
values = {value for value in range(30,70)}
probabilitas = [dist.pdf(value) for value in values]
plt.figure(figsize=(5,4))
plt.hist(sample, bins=10, density=True)
plt.plot(values, probabilitas)
plt.show()




