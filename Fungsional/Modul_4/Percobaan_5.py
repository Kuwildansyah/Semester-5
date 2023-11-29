import math

def point(x, y):
    return x, y

def translasi(p, tx, ty):
    return (p[0] + tx, p[1] + ty)

def rotasi(p, sudut):
    rad = math.radians(sudut)
    return (p[0]*math.cos(rad) - p[1]*math.sin(rad), p[0]*math.sin(rad) + p[1]*math.cos(rad))

def dilatasi(p, sx, sy):
    return (p[0] * sx, p[1] * sy)

# Titik awal berdasarkan NIM
A = point(1, 1)
B = point(9, 4)

# Translasi
A_translasi = translasi(A, 9, 4)
B_translasi = translasi(B, 9, 4)

# Rotasi
A_rotasi = rotasi(A_translasi, 60)
B_rotasi = rotasi(B_translasi, 60)

# Dilatasi
A_dilatasi = dilatasi(A_rotasi, 1.5, 2)
B_dilatasi = dilatasi(B_rotasi, 1.5, 2)

print("Koordinat A setelah transformasi:", A_dilatasi)
print("Koordinat B setelah transformasi:", B_dilatasi)
