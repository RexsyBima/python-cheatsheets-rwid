"""
Variabel dan String

Variabel digunakan untuk memberi label pada nilai-nilai. Sebuah string adalah
serangkaian karakter, dikelilingi oleh tanda kutip tunggal atau ganda.
F-string pada Python memungkinkan Anda untuk menggunakan variabel di dalam string untuk
membangun pesan-pesan dinamis.
"""


#Hello world sederhana
print("Hello World!") #"Hello World"

#Helloworld tapi dengan variabel
pesan = "Hello World!"
print(pesan) #"Hello World!"

#f-strings (lempar variabel ke dalam string)
nama_depan = "Remote W."
nama_belakang = "Indonesia"
nama_lengkap = f"{nama_depan} {nama_belakang}"

print(nama_lengkap) #"Remote W. Indonesia"

umur = 18
nama = "Eko"
intro = f"saya {nama}, berumur {umur}"
print(intro, type(intro))  #saya Eko, berumur 18 <class 'str'>