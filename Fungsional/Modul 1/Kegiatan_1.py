# KEGIATAN 1
# # fungsi pengurangan
# def minus(a, b):
#     return a - b

# # fungsi perkalian
# def mult(a, b):
#     return a * b

# # fungsi pembagian
# def div(a, b):
#     if b != 0:
#         return a / b
#     else:
#         return "Error: Division by zero is not allowed"

# # fungsi penjumlahan
# def add(a, b):
#     return a + b

# # fungsi untuk evaluasi pohon ekspresi
# def tree(angka):
#     if type(angka) is tuple:
#         if angka[1] == '+':
#             return add(tree(angka[0]), tree(angka[2]))
#         elif angka[1] == '-':
#             return minus(tree(angka[0]), tree(angka[2]))
#         elif angka[1] == '*':
#             return mult(tree(angka[0]), tree(angka[2]))
#         elif angka[1] == '/':
#             return div(tree(angka[0]), tree(angka[2]))
#     else:
#         return angka

# # Contoh pohon: (2 + 3) * (5 - 1)
# angka_tree = ((2, '+', 3), '*', (5, '-', 2))

# # Evaluasi pohon ekspresi dengan fungsi pada paradigma fungsional
# result = tree(angka_tree)

# print("Hasil tree:", result)


