class myAtm:   
    print('nama     : Iis Dayanti')
    print('npm      :2021020200068')

    print('prodi    :sistem informasi')
    print('angkatan :21')
    print('kelas    :B')
    print('')
    print('==== SELAMAT DATANG DI ATM SEDERHANA ====')
    print('')
    def __init__(
              self):
        self.nama = eval(input ("masukan no rekening:"))
        self.pasword=eval(input("masukan pasword:"))
        
    def kartu(self):
        print(self.kartu,self.pasword)
    def pasword(self):
        print (self.pasword,self.kartu)
opsi1 =(input("masukan nama:"))
obj=myAtm  ()
print('1.tarik tunai')
print('2.cek saldo')
opsi2=int(input("masukan opsi:"))
uang_kamu = 700.00000
if opsi2==1:
      print('uang kamu berjumlah 700.00000 mau di ambil berapa')
      print('1.Rp.300.00000')
      print('2.Rp.300.00000')
      opsi1=int(input('masukan opsi:'))
if opsi1==1:
      hasil1=uang_kamu-300.00000
      print('uang kamu sekarang:',hasil1)
elif opsi2==1:
      hasil2=uang_kamu-300.00000
      print('uang kamu sekarang:',hasil2)
elif opsi2==2:
    print("saldo anda saat ini 500.000000")
else:
    print('no konik')
