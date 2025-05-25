lista = ['red', 'green', 'blue']
listb = ['#FF0000', '#008000', '#0000FF']

hasil = dict(zip(lista, listb))

urutan = ['green', 'blue', 'red']
hasil_urut_custom = {key: hasil[key] for key in urutan}

print("Output:")
print(hasil_urut_custom)