import matplotlib.pyplot as plt
import numpy as np

data_transaksi = [
    ("Produk A", 50, 10), 
    ("Produk B", 30, 25), 
    ("Produk C", 20, 30), 
    ("Produk D", 60, 8), 
    ("Produk E", 40, 15), 
    ("Produk F", 70, 5),
]

# Ekstrak harga produk dan jumlah produk terjual untuk visualisasi pertama
harga_produk = [data[1] for data in data_transaksi]
jumlah_terjual = [data[2] for data in data_transaksi]

# Buat scatter plot untuk hubungan antara harga produk dan jumlah produk terjual
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.scatter(harga_produk, jumlah_terjual)
plt.xlabel('Harga Produk')
plt.ylabel('Jumlah Produk Terjual')
plt.title('Hubungan Harga Produk dan Jumlah Produk Terjual')

# Hitung total pendapatan untuk setiap produk
pendapatan_produk = [data[1]*data[2] for data in data_transaksi]

# Tambahkan bar chart untuk menyajikan pendapatan produk
nama_produk = [data[0] for data in data_transaksi]
plt.subplot(1, 2, 2)
plt.bar(nama_produk, pendapatan_produk)
plt.xlabel('Nama Produk')
plt.ylabel('Pendapatan Produk')
plt.title('Pendapatan Produk')

plt.tight_layout()
plt.show()
