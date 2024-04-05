#Dictionary menyimpan data berupa key:value pair/pasangan

contoh = {"nama" : "Eko"}
        #  KEY     VALUE
        
#akses sebuah value
print(contoh["nama"]) # Eko
nama = contoh["nama"]
print(nama) # Eko

#menambahkan sebuah key:value baru
contoh["umur"] = 18
print(contoh) #{'nama': 'Eko', 'umur': 18}
data = {"nama" : "Budi", "umur" : 35}
#mengubah key:value pair menjadi set like data
for i in data.items():
    print(i)
    #('nama', 'Budi')
    #('umur', 35)
    
#meloop key saja dalam dictionary
for key in data:
    print(key)
    # nama
    # umur
    

#meloop value saja dalam dictionary
#cara 1
for key in data:
    print(data[key])
    #budi
    #35
    
#cara 2
for value in data.values():
    print(value)
    #budi
    #35