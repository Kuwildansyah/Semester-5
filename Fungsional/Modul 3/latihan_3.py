random_list = [105, 3.1, 'Hello', 737, 412, 2.7, 'Python', 'world', 5.5, 'AI']

# Filter untuk memisahkan nilai float, int, dan string
floats = list(filter(lambda x: isinstance(x, float), random_list))
ints = list(filter(lambda x: isinstance(x, int), random_list))
strings = list(filter(lambda x: isinstance(x, str), random_list))

# Map untuk memetakan nilai int menjadi satuan, puluhan, dan ratusan
def map_to_digits(n):
    return {'ratusan': n // 100, 'puluhan': (n % 100) // 10, 'satuan': n % 10}

mapped_ints = list(map(map_to_digits, ints))

# Output
print("Data Float :")
print(tuple(floats))
print("Data Int :")
for item in mapped_ints:
    print(item)
print("Data String :")
print(strings)
