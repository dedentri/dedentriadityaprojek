print (20*'=')
print('TOKO PERCETAKAN')
print (20*'=')

print('PILIH OPSI DI BAWAH INI:')
print('1.CETAK FOTO + EDIT BACKGROUND')
print('2.FOTO FORMAL PAKET')
print('3.CETAK FOTO BIASA')

#DAFTAR HARGA
harga_perlembar = 2500
harga_paket_foto= 25000
harga_edit = 5000
#HARGA PER PAKET
print('1.4x6 5 lembar = 25000')
print('2.3x4 6 lembar = 25000')
print('3.2x3 6 lembar = 25000')
HARGA_FOTO_PAKET=25000
opsi1 = input('PILIH PILIHAN ANDA:')
if opsi1 == '1':
    ukuran=str(input('masukan ukuran yang anda pilih: '))
    jumlah=int(input('masukan jumlah fotoan: '))
    harga=(jumlah*harga_perlembar+harga_edit)
    print('jadi harga yang harus di bayar adalah Rp: ',harga)
elif opsi1 == '2':
    ukuran=str(input('masukan paket yang anda pilih: '))
    harga=(HARGA_FOTO_PAKET)
    print('jadi harga yang harus di bayar adalah Rp: ',harga)

elif opsi1 == '3':
    ukuran=str(input('masukan ukuran yang anda pilih: '))
    jumlah=int(input('masukan jumlah fotoan: '))
    harga3=(jumlah*harga_perlembar)
    print('jadi harga yang harus di bayar adalah Rp: ',harga3)

