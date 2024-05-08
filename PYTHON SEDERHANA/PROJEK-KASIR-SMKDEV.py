print("-------------KEDAI NASI AYAM SEDERHANA-------------")
print("-----------PROJEK SMKDEV KASIR SEDERHANA-----------")
print(50*"=")
print("SELAMAT DATANG DI KEDAI KAMI SELAMAT MENIKMATI")
print("-------MAU PESAN APA HARI INI?-------")
print("BELANJA LEBIH DARI Rp 100.000 DAN DAPATKAN DISKON")
print(50*"=")
print("PILIH MENU DI BAWAH INI")      
print("1. Nasi Padang          | Rp 15.000 |")
print("2. Ayam Bakar           | Rp 13.000 |")
print("3. Ayam Goreng          | Rp 10.000 |")
print("4. Nasi Kebuli          | Rp 18.000 |")
print("5. Nasi Goreng Spesial  | Rp 23.000 |")
print("6. Ayam Panggang        | Rp 30.000 |")
print("7. Ketoprak             | Rp 15.000 |")
print(50*"=")


pesanan = input("masukan pesanan anda: ")
if pesanan == "1":
    jumlah_pesanan = int(input("Mau pesan berapa?: "))
    uang_kamu = float(input("masukan uang kamu disini ya Rp: "))
    print(50*"-")
    print("Jadi total pembelian anda adalah Rp", jumlah_pesanan*15000)
    total = (jumlah_pesanan*15000)
    if total >= 100000:
        print("Selamat anda mendapatkan diskon sebesar 20% Rp", total*20/100)
        total_harga = (total*20/100)
        print(50*"-")
        print("Total pembayaran anda adalah: Rp",total - total_harga )
        print("Sisa uang kamu adalah: Rp",uang_kamu - (total - total_harga))
    else:
        print("Sisa uang kamu adalah: Rp",uang_kamu - total) 
        
if pesanan == "2":
    jumlah_pesanan = int(input("Mau pesan berapa?: "))
    uang_kamu = float(input("masukan uang kamu disini ya Rp: "))
    print(50*"-")
    print("Jadi total pembelian anda adalah Rp", jumlah_pesanan*13000)
    total = (jumlah_pesanan*13000)
    if total >= 100000:
        print("Selamat anda mendapatkan diskon sebesar 15% Rp", total*15/100)
        total_harga = (total*15/100)
        print(50*"-")
        print("Total pembayaran anda adalah: Rp",total - total_harga )
        print("Sisa uang kamu adalah: Rp",uang_kamu - (total - total_harga))
    else:
        print("Sisa uang kamu adalah: Rp",uang_kamu - total)
        
if pesanan == "3":
    jumlah_pesanan = int(input("Mau pesan berapa?: "))
    uang_kamu = float(input("masukan uang kamu disini ya Rp: "))
    print(50*"-")
    print("Jadi total pembelian anda adalah Rp", jumlah_pesanan*10000)
    total = (jumlah_pesanan*10000)
    if total >= 100000:
        print("Selamat anda mendapatkan diskon sebesar 10% Rp", total*10/100)
        total_harga = (total*10/100)
        print(50*"-")
        print("Total pembayaran anda adalah: Rp",total - total_harga )
        print("Sisa uang kamu adalah: Rp",uang_kamu - (total - total_harga))
    else:
        print("Sisa uang kamu adalah: Rp",uang_kamu - total)
        
if pesanan == "4":
    jumlah_pesanan = int(input("Mau pesan berapa?: "))
    uang_kamu = float(input("masukan uang kamu disini ya Rp: "))
    print(50*"-")
    print("Jadi total pembelian anda adalah Rp", jumlah_pesanan*18000)
    total = (jumlah_pesanan*18000)
    if total >= 100000:
        print("Selamat anda mendapatkan diskon sebesar 10% Rp", total*10/100)
        total_harga = (total*10/100)
        print(50*"-")
        print("Total pembayaran anda adalah: Rp",total - total_harga )
        print("Sisa uang kamu adalah: Rp",uang_kamu - (total - total_harga))
    else:
        print("Sisa uang kamu adalah: Rp",uang_kamu - total)
        
if pesanan == "5":
    jumlah_pesanan = int(input("Mau pesan berapa?: "))
    uang_kamu = float(input("masukan uang kamu disini ya Rp: "))
    print(50*"-")
    print("Jadi total pembelian anda adalah Rp", jumlah_pesanan*23000)
    total = (jumlah_pesanan*23000)
    if total >= 100000:
        print("Selamat anda mendapatkan diskon sebesar 15% Rp", total*15/100)
        total_harga = (total*15/100)
        print(50*"-")
        print("Total pembayaran anda adalah: Rp",total - total_harga )
        print("Sisa uang kamu adalah: Rp",uang_kamu - (total - total_harga))
    else:
        print("Sisa uang kamu adalah: Rp",uang_kamu - total)
        
if pesanan == "6":
    jumlah_pesanan = int(input("Mau pesan berapa?: "))
    uang_kamu = float(input("masukan uang kamu disini ya Rp: "))
    print(50*"-")
    print("Jadi total pembelian anda adalah Rp", jumlah_pesanan*30000)
    total = (jumlah_pesanan*30000)
    if total >= 100000:
        print("Selamat anda mendapatkan diskon sebesar 15% Rp", total*15/100)
        total_harga = (total*15/100)
        print(50*"-")
        print("Total pembayaran anda adalah: Rp",total - total_harga )
        print("Sisa uang kamu adalah: Rp",uang_kamu - (total - total_harga))
    else:
        print("Sisa uang kamu adalah: Rp",uang_kamu - total)
        
if pesanan == "7":
    jumlah_pesanan = int(input("Mau pesan berapa?: "))
    uang_kamu = float(input("masukan uang kamu disini ya Rp: "))
    print(50*"-")
    print("Jadi total pembelian anda adalah Rp", jumlah_pesanan*15000)
    total = (jumlah_pesanan*15000)
    if total >= 100000:
        print("Selamat anda mendapatkan diskon sebesar 10% Rp", total*10/100)
        total_harga = (total*10/100)
        print(50*"-")
        print("Total pembayaran anda adalah: Rp",total - total_harga )
        print("Sisa uang kamu adalah: Rp",uang_kamu - (total - total_harga))
    else:
        print("Sisa uang kamu adalah: Rp",uang_kamu - total)
        
