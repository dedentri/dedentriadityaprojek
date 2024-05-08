import datetime
import os
import random
nama_kasir = [
    ('Syahrul'),
    ('Linda'),
    ('Akbar'),
    ('Deden'),
    ('Agan')
]
makanan = [
    ('Nasi Padang', 15000),
    ('Nasi Kebuli', 18000),
    ('Nasi Goreng', 23000),
    ('Ayam Goreng', 10000),
    ('Ayam Bakar', 13000),
    ('Ayam Gulai', 30000),
    ('Ketoprak', 15000)
]

minuman = [
    ('Es Teh', 3000),
    ('Es Jeruk', 5000),
    ('Teh Tarik', 15000),
    ('Lemon Tea', 20000),
    ('Milk Tea', 22000),
    ('Nutrisari', 5000)
]
kasir = ''
menu = ""
P_makanan = []
P_minuman = []
nama = ''
id_kasir = 1
while True:
    if kasir == "":
        print("-------------Anda Masuk Sebagai Kasri--------------")
        print("-----------------Pilih nama Anda-------------------")
        for x in nama_kasir:
            print(f"{id_kasir}. {x}")
            id_kasir+=1
        kasir_id = int(input("Pilih ID kasir : "))
        kasir = nama_kasir[kasir_id-1]
    if nama == "":
        print("-------------KEDAI NASI AYAM SEDERHANA-------------")
        print("-----------PROJEK SMKDEV KASIR SEDERHANA-----------")
        nama = input("\nMasukan Nama : ")
        os.system('cls')
        print("SELAMAT DATANG DI KEDAI KAMI SELAMAT MENIKMATI")
        print("-------MAU PESAN APA HARI INI?-------")
        print("BELANJA LEBIH DARI Rp 100.000 DAN DAPATKAN DISKON")
    print(" 1. Pesan Makan")
    print(" 2. Pesan Minum")
    print(" 3. Lihat Pesanan")
    print(" 4. Lihat Tagihan")
    menu = input("Silahkan pilih menu di atas : ")

    if menu == '1':
        os.system('cls')
        lagi = "y"
        while lagi == "Y" or lagi == 'y':
           print("-------------KEDAI NASI AYAM SEDERHANA-------------")
           print("-----------PROJEK SMKDEV KASIR SEDERHANA-----------") 
           print("------------------MENU MAKANAN---------------------")
           no = 1
           for x in makanan:
               print(f"{no}. {x[0]} \t|\t {x[1]}")
               no += 1
           no_makan = int(input("Masukan pesanan Anda : "))

           print(f"\nAnda memilih {makanan[no_makan-1][0]}")
           porsi = int(input(f"Berapa porsi yang Anda inginkan : "))
           pesanan = (makanan[no_makan-1][0], makanan[no_makan-1][1], porsi)
           P_makanan.append(pesanan)
           print(f"{porsi} porsi {makanan[no_makan-1][0]} berhasil dicatat!!!")

           lagi = input("\nApakah Anda ingin memesan makan lagi ? (y/n): ")
           os.system('cls')

    if menu == '2':
        os.system('cls')
        lagi = "y"
        while lagi == "Y" or lagi == 'y':
           print("-------------KEDAI NASI AYAM SEDERHANA-------------")
           print("-----------PROJEK SMKDEV KASIR SEDERHANA-----------") 
           print("------------------MENU MAKANAN---------------------")
           no = 1
           for x in minuman:
               print(f"{no}. {x[0]} \t|\t {x[1]}")
               no += 1
           no_minum = int(input("Masukan pesanan Anda : "))

           print(f"\nAnda memilih {minuman[no_minum-1][0]}")
           porsi = int(input(f"Berapa porsi yang Anda inginkan : "))
           pesanan = (minuman[no_minum-1][0], minuman[no_minum-1][1], porsi)
           P_minuman.append(pesanan)
           print(f"{porsi} porsi {minuman[no_minum-1][0]} berhasil dicatat!!!")

           lagi = input("\nApakah Anda ingin memesan minum lagi ? (y/n): ")
           os.system('cls')

    if menu == '3':
        os.system('cls')
        lagi = "y"
        print("-------------KEDAI NASI AYAM SEDERHANA-------------")
        print("-----------PROJEK SMKDEV KASIR SEDERHANA-----------")
        if P_makanan: 
            print("\n---------- Daftar Makanan Yang Anda Pesan ---------")
            for x in P_makanan:
                print(f"{x[2]} porsi {x[0]}")
            
        else:
            pass
        if P_minuman:
            print("\n---------- Daftar Minuman Yang Anda Pesan ---------")
            for x in P_minuman:
                print(f"{x[2]} porsi {x[0]}")
        else:
            pass
        input("\nTekan Enter Untuk Kembali.....")
        os.system('cls')
    
    if menu == '4':
        os.system('cls')
        harga1 = []
        jmlh_mkn = []
        if P_makanan:
            for i in P_makanan:
                hitung = i[1] * i[2]
                harga1.append(hitung)
                hrga_mkn = sum(harga1)
                jmlh_mkn.append(hrga_mkn)
        else:
            hrga_mkn = 0
            jmlh_mkn.append(hrga_mkn)

        harga2 = []
        jmlh_mnum = []
        if P_minuman:
            for i in P_minuman:
                hitung = i[1] * i[2]
                harga2.append(hitung)
                hrga_mnum = sum(harga2)
                jmlh_mnum.append(hrga_mnum)
        else:
            hrga_mnum = 0
            jmlh_mnum.append(hrga_mnum)

        mkn = (jmlh_mkn[len(jmlh_mkn)-1])
        mnum = (jmlh_mnum[len(jmlh_mnum)-1])
        total = mkn+mnum
        waktu = datetime.datetime.today()

        if total < 100000:
            print("="*50)
            print("-----------------BUKTI PEMBAYARAN-----------------")
            print("-----------KEDAI NASI AYAM SEDERHANA--------------")
            print("="*50)
            print(f"\nWaktu : {waktu}")
            print(f"Kasir : {kasir}")
            print(f"Pelanggan : {nama}")
            print("="*50)

            for item in P_makanan:
                print(f"\n{item[2]} porsi {item[0]} \t Rp.{mkn}")
            for item in P_minuman:
                print(f"{item[2]} porsi {item[0]} \t Rp.{mnum}")
            
            print("="*50)
            print(f"\nSubtotal : \t\t Rp.{total}")
            print(f"Total    : \t\t Rp.{total}")
            bayar = int(input("Cash     : \t\t Rp. "))
            print(f"Kembalian  : \t\t Rp.{bayar-total}\n")
            print("\n-----------TERIMAKASIH TELAH DATANG-----------")
            print("---------------HAVE A NICE DAY----------------")
            print("="*50)
        else:
            diskon = total*(20/100)
            harga_diskon = total-diskon
            print("="*50)
            print("-----------------BUKTI PEMBAYARAN-----------------")
            print("-----------KEDAI NASI AYAM SEDERHANA--------------")
            print("="*50)
            print(f"Waktu     : {waktu}")
            print(f"Kasir     : {kasir}")
            print(f"Pelanggan : {nama}")
            print("="*50)

            for item in P_makanan:
                print(f"\n{item[2]} porsi {item[0]} \t Rp.{mkn}")
            for item in P_minuman:
                print(f"{item[2]} porsi {item[0]} \t Rp.{mnum}\n")
            
            print("="*50)
            print(f"\nSubtotal   : \t\t Rp.{total}")
            print(f"Diskon 20% : \t\t Rp.{diskon}")
            print(f"Total      : \t\t Rp.{harga_diskon}")
            bayar = int(input("Cash       : \t\t Rp. "))
            print(f"Kembalian  : \t\t Rp.{bayar-harga_diskon}\n")
            print("\n-----------TERIMAKASIH TELAH DATANG-----------")
            print("---------------HAVE A NICE DAY----------------")
            print("="*50)

        break