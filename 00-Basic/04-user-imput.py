##########################################################################
#user input digunakan untuk meminta user memasukan input kedalam program,#
#input yang dimasukan akan selalu berbentu string                        #
#(tetapi tetap bisa dikonversi menjadi tipe data lain, selagi memenuhi)  #
##########################################################################

hobi = input("apa hobi yang anda sukai kali ini?")

print(f"Hobi yang kamu sukai adalah {hobi}")
print(f"tipe data variabel hobi adalah {type(hobi)}")

#merubah user input ke integer
umur = input("masukan umur anda")
umur = int(umur) #konversi umur str menjadi int

print(f"umur anda adalah {umur}, dan tipedata umur adalah {type(umur)}")