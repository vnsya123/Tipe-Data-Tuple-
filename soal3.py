
filename = input("Masukkan nama file : ")

try:
    with open(filename, 'r') as file:
        counts = {} 

        for line in file:
            if line.startswith('From '): 
                words = line.split()
                if len(words) >= 2:
                    email = words[1]  
                    counts[email] = counts.get(email, 0) + 1  

        
        print("\nHasil Histogram Email:")
        print(counts)

except FileNotFoundError:
    print("File tidak ditemukan. Pastikan nama file benar dan ada di folder yang sama.")
