filename = input("Masukkan nama file: ")
try:
    with open(filename, 'r') as file:
        domain_count = {}
        for line in file:
            if line.startswith('From '):
                words = line.split()
                if len(words) >= 2:
                    email = words[1]
                    domain = email.split('@')[1]
                    domain_count[domain] = domain_count.get(domain, 0) + 1
        print("\nHasil Histogram Domain:")
        print(domain_count)

except FileNotFoundError:
    print("File tidak ditemukan. Pastikan nama file benar dan berada di folder yang sama.")
