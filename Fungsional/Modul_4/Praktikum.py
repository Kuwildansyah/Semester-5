import math
def print_message(func):
    def wrapper(*args, **kwargs):
        print("Calling function...")
        result = func(*args, **kwargs)
        print("Function call complete.")
        return result
    return wrapper

# Titik awal
A = (3, 4)
B = (5, 6)

# Fungsi untuk translasi
@print_message
def translate(tx, ty):
    def inner(point):
        x, y = point
        return (x + tx, y + ty)
    return inner

# Fungsi untuk rotasi
@print_message
def rotate(degree):
    rad = math.radians(degree)
    def inner(point):
        x, y = point
        return (x * math.cos(rad) - y * math.sin(rad), x * math.sin(rad) + y * math.cos(rad))
    return inner

# Fungsi untuk perbesaran skala
@print_message
def scale(sx, sy):
    def inner(point):
        x, y = point
        return (x * sx, y * sy)
    return inner

# Mengambil input dari user
tx = float(input("Masukkan nilai tx untuk translasi: "))
ty = float(input("Masukkan nilai ty untuk translasi: "))
degree = float(input("Masukkan derajat rotasi: "))
sx = float(input("Masukkan faktor skala untuk sumbu x: "))
sy = float(input("Masukkan faktor skala untuk sumbu y: "))

# Menerapkan transformasi
transform = lambda point: scale(sx, sy)(rotate(degree)(translate(tx, ty)(point)))

# Hasil transformasi
A_transformed = transform(A)
B_transformed = transform(B)

# Mencetak hasil
print(f"Titik A setelah transformasi: {A_transformed}")
print(f"Titik B setelah transformasi: {B_transformed}")
