import matplotlib.pyplot as plt
from functools import reduce

# Data nilai-nilai ujian mahasiswa
nilai_mahasiswa = [75, 80, 90, 65, 70, 85, 95, 78, 88, 92]

# Menghitung rata-rata menggunakan fungsi reduce
total = reduce(lambda a, b: a + b, nilai_mahasiswa)
rata_rata = total / len(nilai_mahasiswa)

print("Rata-rata nilai ujian mahasiswa: ", rata_rata)

# Membuat label mahasiswa (sumbu x) dalam bentuk fungsional dinamis (list-map-lamda)
mahasiswa = list(map(lambda x: 'Mahasiswa ' + str(x+1), range(len(nilai_mahasiswa))))

# Visualisasi data dalam bentuk diagram batang
plt.bar(mahasiswa, nilai_mahasiswa)

# Menambahkan garis rata-rata
plt.axhline(y=rata_rata, color='r', linestyle='--')
plt.text(0.5, rata_rata, f"Rata-rata = {rata_rata:.2f}", color = 'r')

plt.xlabel('Mahasiswa')
plt.ylabel('Nilai Ujian')
plt.title('Diagram Batang Nilai Ujian Mahasiswa')
plt.show()
