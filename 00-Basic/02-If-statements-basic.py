""" 
If statements

kode didalam if statement hanya akan berjalan jika sifat if statement bersifat True

"""
#Ekspresi Kondisional


number = 69

print(number == 69) # == -> samadengan            / equal | out -> True
print(number >  69) # >  -> lebihdari             / greater than | out -> False
print(number <  69) # <  -> kurangdari            / lesser than | out -> False
print(number >= 69) # >= -> lebihdari samadengan  / greater than or equal to | out -> True
print(number <= 69) # <= -> kurangdari samadengan / lesser than or equal to | out -> True
print(number != 69) # != -> tidak samadengan      / not equal to | out -> False

# rumus if kondisi

if True:
    """ 
    akan mengeksekusi kode dibawah
    """
    print("Hello, this code is executed because if condition is True")
    

umur = 21

if umur >= 18:
    print("Pengguna berhak mendapatkan sim")
    
#if-elif-else statements
if umur < 4:
    print("anda seorang bayi")
elif 4 < umur < 18:
    print("anda seorang remaja")
else:
    print("anda seorang dewasa")

