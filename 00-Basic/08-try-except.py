# rumus/syntax/istilah try and except digunakan untuk menghandle sebuah error, jadi jika error tersebut terjadi, maka lakukanlah kode y
# selain untuk menghandle error biasanyya digunakan untuk memberikan tampilan error yang mudah dimengerti seorang user

#contoh
# umur = int(input("berapa umur anda?"))
# print(umur)

#di contoh diatas, jika kita memasukan nilai bukan integer, maka diterminal akan muncul error
#ValueError: invalid literal for int() with base 10: 'asd'

#untuk memasukkan errornya tinggal cek diterminal

try:
    umur = int(input("berapa umur anda?"))
except ValueError:
    print("silahkan masukan input umur dengan benar")
    
#kode diatas akan mengeluarkan periintah print jika user memasukan input bukan integer 