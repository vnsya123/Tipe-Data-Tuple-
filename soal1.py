# Dictionary yang diberikan
data = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# Header
print("key  value  item")

# Menampilkan setiap key, value, dan item
for k, v in data.items():
    print(f"{k:<5}{v:<7}({k}, {v})")
