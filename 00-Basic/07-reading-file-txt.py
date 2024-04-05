#python bisa membuka file berbagai jenis text, contoh, txt dan json.

#membaca file txt
#rumus = with open("nama file.txt", "modebaca") as f:
#ada banyak jenis mode baca, tapi yang sering dipakai adalah "r" dan "w", berdiri sebagai mode read dan write 
with open("halo.txt", "r") as file:
    text = file.read()
    
print(text) #teks ini berasal dari halo.txt

with open("tes.txt", "w") as file:
    file.writelines("text ini muncul karena python")