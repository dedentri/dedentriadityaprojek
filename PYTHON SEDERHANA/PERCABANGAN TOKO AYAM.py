print(35*"=")
print("SELAMAT DATANG DI LOBI PEMESANAN")
print("SILAHKAN DI PILIH MENUNYA:")
print(35*"=")
print("1.Ayam Geprek = 15.000")
print("2.Ayam goreng = 12.000")
print("3.ayam goreng mentega = 18.000")
print("4.Ayam bakar = 10.000")
print("5.ayam Panggang = 22.000")
print("promo spesial akhir tahun beli di atas nominal 50.000 dan dapatikan diskon 20%")
print(35*"-")

opsi = input("pilih menunya: ")
if opsi == "1":
    jumlah=int(input("masukan jumlah pesanan anda:  "))
    uang_kamu=int(input("masukan uang kamu:  "))
    print("jadi total pembelian anda adalah: ",jumlah*15000)
    total_pembelian=(jumlah*15000)
    if total_pembelian >= 50000:
        print('DISKON KAMU ADALAH:  ',total_pembelian*20/100)
        hasil_diskon=(total_pembelian*20/100)
        print('JADI KEMBALIAN KAMU ADALAH: ',uang_kamu-(total_pembelian-hasil_diskon))
    elif total_pembelian < 50000:
        print('kembalian kamu adalah: ',uang_kamu-total_pembelian)
        
if opsi == "2":
    jumlah=int(input("masukan jumlah pesanan anda:  "))
    uang_kamu=int(input("masukan uang kamu:  "))
    print("jadi total pembelian anda adalah: ",jumlah*12000)
    total_pembelian=(jumlah*12000)
    if total_pembelian >= 50000:
        print('DISKON KAMU ADALAH:  ',total_pembelian*20/100)
        hasil_diskon=(total_pembelian*20/100)
        print('JADI KEMBALIAN KAMU ADALAH: ',uang_kamu-(total_pembelian-hasil_diskon))
    elif total_pembelian < 50000:
        print('kembalian kamu adalah: ',uang_kamu-total_pembelian)
        
if opsi == "3":
    jumlah=int(input("masukan jumlah pesanan anda:  "))
    uang_kamu=int(input("masukan uang kamu:  "))
    print("jadi total pembelian anda adalah: ",jumlah*18000)
    total_pembelian=(jumlah*18000)
    if total_pembelian >= 50000:
        print('DISKON KAMU ADALAH:  ',total_pembelian*20/100)
        hasil_diskon=(total_pembelian*20/100)
        print('JADI KEMBALIAN KAMU ADALAH: ',uang_kamu-(total_pembelian-hasil_diskon))
    elif total_pembelian < 50000:
        print('kembalian kamu adalah: ',uang_kamu-total_pembelian)
        
if opsi == "4":
    jumlah=int(input("masukan jumlah pesanan anda:  "))
    uang_kamu=int(input("masukan uang kamu:  "))
    print("jadi total pembelian anda adalah: ",jumlah*10000)
    total_pembelian=(jumlah*10000)
    if total_pembelian >= 50000:
        print('DISKON KAMU ADALAH:  ',total_pembelian*20/100)
        hasil_diskon=(total_pembelian*20/100)
        print('JADI KEMBALIAN KAMU ADALAH: ',uang_kamu-(total_pembelian-hasil_diskon))
    elif total_pembelian < 50000:
        print('kembalian kamu adalah: ',uang_kamu-total_pembelian)
        
if opsi == "5":
    jumlah=int(input("masukan jumlah pesanan anda:  "))
    uang_kamu=int(input("masukan uang kamu:  "))
    print("jadi total pembelian anda adalah: ",jumlah*22000)
    total_pembelian=(jumlah*22000)
    if total_pembelian >= 50000:
        print('DISKON KAMU ADALAH:  ',total_pembelian*20/100)
        hasil_diskon=(total_pembelian*20/100)
        print('JADI KEMBALIAN KAMU ADALAH: ',uang_kamu-(total_pembelian-hasil_diskon))
    elif total_pembelian < 50000:
        print('kembalian kamu adalah: ',uang_kamu-total_pembelian)