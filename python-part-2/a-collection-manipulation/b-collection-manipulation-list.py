# Penggabungan dua list
print(">>> Fitur penggabungan dua list")
list_makanan = ['Gado-gado', 'Ayam Goreng', 'Rendang']
list_minuman = ['Es Teh', 'Es Jeruk', 'Es Campur']
list_menu = list_makanan + list_minuman
print(list_menu)

print("--------------------")

# Mengambil data dengan index negatif
print(">>> Fitur mengambil data index negatif")
harga = [1000, 2500, 5000, 15000, 25000]
print(harga[:-3])

print("--------------------")

# Append: Untuk menambah data di dalam list
print(">>> Fitur append data")
list_makanan = ['Gado-gado', 'Ayam Goreng', 'Rendang']
list_makanan.append('Ketoprak')
print(list_makanan)

print("--------------------")

# Clear: untuk menghapus seluruh data di dalam list
print(">>> Fitur hapus list data")
list_makanan = ['Gado-gado', 'Ayam Goreng', 'Rendang']
list_makanan.clear()
print(list_makanan)

print("--------------------")

# Copy: untuk mengembalikan copy dari setiap elemen dalam list
print(">>> Fitur copy list")
list_makanan1 = ['Gado-gado', 'Ayam Goreng', 'Rendang']
list_makanan2 = list_makanan1.copy()
list_makanan3 = list_makanan1
list_makanan2.append('Opor')
list_makanan2.append('Sei Sapi')
list_makanan3.append('Ketoprak')
list_makanan3.append('Sate Taichan')
list_makanan1.append('Sate Klatak')
list_makanan1.append('Burger')
print(list_makanan1)
print(list_makanan2)
print(list_makanan3)

print("--------------------")

#count: menampilkan jumlah kemunculan elemen pada suatu list
print(">>> Fitur count list")
list_score = ['Budi', 'Sud', 'Budi', 'Budi', 'Budi', 'Sud', 'Sud']
score_budi = list_score.count('Budi')
score_sud = list_score.count('Sud')
print(score_budi)
print(score_sud)

print("--------------------")

#Extend: menambahkan suatu list ke dalam list lain
print(">>> Fitur extend list")
list_menu = ['Gado-gado', 'Ayam Goreng', 'Rendang']
list_minuman = ['Es Teh', 'Es Jeruk', 'Es Campur']
list_menu.extend(list_minuman)
print(list_menu)

print("--------------------")

# Fitur .index()
print(">>> Fitur .index()")
list_score = ['Budi','Sud','Budi','Budi','Budi','Sud','Sud']
score_pertama_sud = list_score.index('Sud') + 1
print(score_pertama_sud)

print("--------------------")

# Fitur .insert()
print(">>> Fitur .insert()")
list_score = ['Budi','Sud','Budi','Budi','Sud']
list_score.insert(3, 'Sud')
print(list_score)

print("--------------------")

# Fitur .pop()
print(">>> Fitur .pop()")
list_menu = ['Gado-gado', 'Ayam Goreng', 'Rendang']
list_menu.pop(1)
print(list_menu)

print("--------------------")

# Fitur .remove()
print(">>> Fitur .remove()")
list_menu = ['Gado-gado', 'Ayam Goreng', 'Rendang', 'Ketoprak']
list_menu.remove('Rendang')
print(list_menu)

print("--------------------")

# Fitur .reverse()
print(">>> Fitur .reverse()")
list_menu = ['Gado-gado', 'Ayam Goreng', 'Rendang', 'Ketoprak']
list_menu.reverse()
print(list_menu)

print("--------------------")

# Fitur .sort()
print(">>> Fitur .sort()")
list_menu = ['Gado-gado', 'Ayam Goreng', 'Rendang', 'Ketoprak']
list_menu.sort() # Default: Ascending
print(list_menu) 
list_menu.sort(reverse=True)# Descending
print(list_menu) 

print("--------------------")