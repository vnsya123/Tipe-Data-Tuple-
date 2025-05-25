def semua_sama(t):
    return all(x == t[0] for x in t)

# Contoh penggunaan
tA = (90, 90, 90, 90)
print(semua_sama(tA))  # Output: True

tB = (90, 80, 90, 90)
print(semua_sama(tB))  # Output: False
