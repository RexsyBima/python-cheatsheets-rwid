# Dalam blok kode whileloops, sebuah kode akan terus berjalan selagi sifat dari while loops merupakan True

""" Contoh whileloops akan terus berjalan tanpa berhenti 

while True:
    print("hello world!")

untuk mengetes silahkan copy kode baris 5-6 keluar komentar ini
"""

#Rumus simplified
# while |kondisi itu True|:
#    eksekusi kode dibawah ini

umur = 0

while umur < 18:
    print(umur)
    umur+=1
    #0,1,2,3,....,17
    
#cara lain untuk memberhentikan while Loops adalah menggunakan kombinasi if statement lalu break

while True:
    kode = input("silahkan ketik quit untuk keluar dari sini : ")
    if kode == "quit":
        print("kode ini berhenti karena memenuhi sifat if statement, dan diberhentikan melalui break statement")
        break