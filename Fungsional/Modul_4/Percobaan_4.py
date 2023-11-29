import math

def translasi(p, tx, ty):
    return (p[0] + tx, p[1] + ty)

def dilatasi(p, sx, sy):
    return (p[0] * sx, p[1] * sy)

def rotasi(p, sudut):
    rad = math.radians(sudut)
    return (p[0]*math.cos(rad) - p[1]*math.sin(rad), p[0]*math.sin(rad) + p[1]*math.cos(rad))

# Titik awal
P = (3, 5)

# Translasi
P_translasi = translasi(P, 2, -1)
print(f'Koordinat setelah translasi: {P_translasi}')

# Dilatasi
P_dilatasi = dilatasi(P, 2, -1)
print(f'Koordinat setelah dilatasi: {P_dilatasi}')

# Rotasi
P_rotasi = rotasi(P, 30)
print(f'Koordinat setelah rotasi: {P_rotasi}')
