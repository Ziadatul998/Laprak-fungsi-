#fungsi dan modularasi
#f(x)=5x-10
def fungsiku (x):
    return (5*x)-10
a=int(input("masukkan nilai a:"))

#hasil fx jika nilai x = 10
hasil_fx = fungsiku (a)
print(hasil_fx)
#fungsi mencari nilai faktorial 
def faktorial (n):
    if n==0 or n==1:
        return 1
    else:
        return n*(faktorial(n-1))
    
#mencari nilai faktorial!
a = int(input("masukkan nilai yang akan dicari: "))    
cari_faktorial = faktorial(a)   
print ("nilai dari ", a,"! adalah ", cari_faktorial)

#fungsi dan mudularasi
#fungsi mencari luas persegi panjang
def luaspersegipanjang (panjang, lebar):
    return panjang*lebar

#funngsi mencari keliling persegi panjang
def kelilingpersegipanjang(panjang,lebar):
    return 2*(panjang+lebar)

t=float(input("masukkan panjang :"))
i=float(input("masukkan lebar :"))

hasil_luas = luaspersegipanjang(t,i)
hasil_keliling = kelilingpersegipanjang(t,i)
print("luasnya adalah ", hasil_luas)
print("keliling adalah ", hasil_keliling)

#fungsi mencari nilai maximal
def max (angka1, angka2, angka3):
    if ((angka1>angka2) and  (angka1>angka2)):
        return angka1
    elif ((angka2>angka1) and (angka2>angka3)):
        return angka2
    else:
        return angka3
    
a= int(input("masukkan angka1: "))
b= int(input("masukkan angka2: "))
c= int(input("masukkan angka3: "))

cek_max = max(a,b,c)
print("nilai maximal dari ", a,"dan",b,"dan",c,"adalah",cek_max)
