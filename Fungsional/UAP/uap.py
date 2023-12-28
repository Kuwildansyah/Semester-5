# No. 1 Tuple

barang_harga = ('Pensil', 1500, 'Buku', 5000, 'Penggaris', 2000)

def memisahkan_data(data):
    nama_barang = []
    harga = []

    for i in range(0, len(data), 2):
        nama_barang.append(data[i])
        harga.append(data[i+1])

    return nama_barang, harga

nama_barang, harga = memisahkan_data(barang_harga)

def menggabungkan_list(nama_barang, harga):
    return dict(zip(nama_barang, harga))

dict_barang_harga = menggabungkan_list(nama_barang, harga)

print("Data barang dan harga:", barang_harga)
print("Nama barang:", nama_barang)
print("Harga:", harga)
print("Dictionary barang dan harga:", dict_barang_harga)

# No 2 .1 Fungsi pengecekan bilangan prima (easy)
# def is_prima(n):
#     if n == 2:
#         return True
#     if n < 2 or n % 2 == 0:
#         return False
#     for x in range(3, int(n**0.5) + 1, 2):
#         if n % x == 0:
#             return False
#     return True
# num = int(input("Masukkan bilangan bulat: "))
# if is_prima(num):
#     print(f"{num} adalah bilangan prima")
# else:
#     print(f"{num} bukan bilangan prima")

# No2.2 Fungsi Palindrome check (hard)
# def isPalindrome(string):
#     length = len(string)
#     for i in range(length // 2):
#         if string[i] != string[length - 1 - i]:
#             return False
#     return True

# string = 'radar'
# isPalindrome(string)
# print("Hasil ngecek palindrome: ", isPalindrome(string))

# no. 3 Pure Function
# def tambah_angka(total, angka):
#     total += angka
#     return total

# hasil = tambah_angka(0, 5) 
# hasil = tambah_angka(hasil, 10) 
# print(hasil)

# No 4.1 lambda (easy)
# tambah_angka = lambda total, angka: total + angka
# hasil = tambah_angka(0, 5) 
# hasil = tambah_angka(hasil, 10)

# No 4.2 Lambda (Hard)
# klasifikasi_angka = lambda x: "Positif" if x > 0 else ("Negatif" if x < 0 else "Nol")
# pencarian_angka = lambda list_angka, find: "found" if find in list_angka else "not found"
# hasil = klasifikasi_angka(5) 
# hasil = klasifikasi_angka(-10) 
# hasil = pencarian_angka([1, 2, 3, 4, 5], 3) 
# hasil = pencarian_angka([1, 2, 3, 4, 5], 6) 
# karena listnya error mulu, jadi saya definisikan saja langsung isinya biar ga error

# No.5 List Comprehension
# ganjil = [x for x in range(0, 51) if x % 2 != 0]
# print(ganjil)

# No.6 Generator Expression
# def ganjil_generator(n):
#     for x in range(n):
#         if x % 2 != 0:
#             yield x

# ganjil_gen = ganjil_generator(51)
# for number in ganjil_gen:
#     print(number)

# No.7 HOF
# sisagold = lambda a, b: a - b
# def kurang(a, b):
#     return a - b
# def operasi(a, b, op):
#     return op(a, b)
# hasil = operasi(10, 5, kurang)
# print(hasil) 

# No.8.1. Filter list angka kelipatan 3 (easy)
# def filter_kelipatan_tiga(data):
#     return [i for i in data if i % 3 == 0]
# data = [i for i in range(100)]
# hasil = filter_kelipatan_tiga(data)
# print(hasil)

# No.8.3 palindrome
# def is_palindrome(word):
#     return word == word[::-1]
# def filter_palindrome(text):
#     words = text.split()
#     palindromes = [word for word in words if is_palindrome(word)]
#     not_palindromes = [word for word in words if not is_palindrome(word)]
#     return palindromes, not_palindromes
# text = "kontolodon is gede."
# palindromes, not_palindromes = filter_palindrome(text)
# print("Palindromes:", palindromes)
# print("Not Palindromes:", not_palindromes)

# No.9.2 Mapping
# data = range(10)
# filterData = filter(lambda x : x%2==1, data)
# mapping = map(lambda y : y*2, filterData)
# filteredData = map(lambda x : x*2, filter(lambda x : x%2==1, range(10)))

# # No.13 Data Visualization
# import matplotlib.pyplot as plt
# data = [
#     ('Bus', 5, 200),
#     ('Trem', 8, 150),
#     ('Kereta', 12, 300),
#     ('Minibus', 6, 180),
#     ('Tram', 9, 220)
# ]
# jenis_kendaraan = [i[0] for i in data]
# penggunaan_energi = [i[1] for i in data]
# biaya_operasional = [i[2] for i in data]

# plt.figure(figsize=(10, 5))
# plt.subplot(1, 3, 1)
# plt.plot(penggunaan_energi)
# plt.title('Penggunaan Energi')
# plt.ylabel('Penggunaan Energi (Watt per KM)')

# plt.subplot(1, 3, 2)
# plt.plot(biaya_operasional)
# plt.title('Biaya Operasional')
# plt.ylabel('Biaya Operasional (Rupiah per KM)')

# plt.subplot(1, 3, 3)
# plt.scatter(penggunaan_energi, biaya_operasional)
# plt.title('Penggunaan Energi dan Biaya Operasional')
# plt.xlabel('Penggunaan Energi (Watt per KM)')
# plt.ylabel('Biaya Operasional (Rupiah per KM)')

# for i, txt in enumerate(jenis_kendaraan):
#     plt.annotate(txt, (penggunaan_energi[i], biaya_operasional[i]))

# plt.legend()
# plt.tight_layout()
# plt.show()

