"""
Lists

Sebuah daftar menyimpan serangkaian item dalam urutan tertentu. Anda mengakses item menggunakan indeks, atau dalam sebuah perulangan. menggunakan [item1,item2,...,item n] 
bersifat mutable atau isi data bisa dirubah dirubah
"""

#cara membuat list
buah = ["apple", "grape", "durian"]

#mendapatkan item pertama apel
buah_1 = buah[0] #apple

#mendapatkan item terakhir menggunakan indeks negatif
buah_terakhir = buah[-1] #durian

#meloop didalam list
for b in buah:
    print(b)
    # apple
    # grape
    # durian
    
#menambahkan item kedalam sebuah list
nama = []
nama.append("Remote")
nama.append("Worker")
nama.append("Indonesia") 
print(nama)  #['Remote', 'Worker', 'Indonesia']

#slicing, mengambil item dari indeks x sampai SEBELUM indeks y / y-1
nama = ["Anisa", "Budi", "Citra", "Dewi", "Edo"]
print(nama[0:3]) #['Anisa', 'Budi', 'Citra'], BUKAN #['Anisa', 'Budi', 'Citra', "Edo"]
print(nama[2:4]) #['Citra', 'Dewi']
print(nama[:3]) #['Anisa', 'Budi', 'Citra']
print(nama[2:]) #['Citra', 'Dewi', 'Edo']

"""
Tuple

Tuple, mirip seperti list, perbedaannya hanya bahwa sifatnya immutable (isi data tidak bisa dirubah)

Note : Lists lebih sering dipakai dibanding Tuple
"""

buah = ("Apel", "Semangka", "Durian")

print(buah) #('Apel', 'Semangka', 'Durian')
print(buah[1]) #Semangka