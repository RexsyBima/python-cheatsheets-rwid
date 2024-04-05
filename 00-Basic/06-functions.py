#Fungsi adalah blok kode yang dapat dipanggil untuk melakukan tugas tertentu dengan input dan output yang bisa diatur

#definisi/membuat fungsi, wajib dengan rumus syntax
#def nama_fungsi():
#   blok kode (dan yes ada indentasi)
def salam_perkenalan():
    print("halo, saya Joko")
    
#pemanggilan fungsi/cara pakai
salam_perkenalan() #halo, saya joko

#menambahkan argumen/parameter (saya menggunakan 2 istilah tersebut bersinambungan)
def salam(nama):
    print(f"halo, saya {nama}")
    
salam("Budi") #halo, saya Budi

#mensetting default value dari arg/par...

def makan(nama="rendang"):
    print(f"saya makan {nama}")
    
makan()      # saya makan rendang
makan("soto")# saya makan soto



#return sebuah nilai
def penjumlahan(x,y):
    hasil = x+y 
    return hasil

x=10
y=15
hasil_jumlah = penjumlahan(x,y)
print(hasil_jumlah) #25

hasil_jumlah = penjumlahan(x,y) - 10
print(hasil_jumlah) #15

""" 
kode dibaris 38 bisa dilakukan karena hasil return value dari fungsi penjumlahan adalah 25,
mirip seperti MTK, python memiliki order of execution sebuah kode
"""

# kode baris 38, itu sama saja seperti
hasil_jumlah = (x+y) - 10