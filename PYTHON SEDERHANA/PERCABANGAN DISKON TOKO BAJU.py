print("1.PRIA ")
print("2.WANITA")
print (40*"==")
print("SELAMAT HARI IBU,KHUSUS PELANGGAN WANITA JIKA BERBELANJA DI ATAS 100.000 DAPAT DISKON 10%,JIKA DI BAWAH 100.000 MAKA 5%,MARI SEGERA DAPATKAN!!!")
print (40*"==")
opsi = input("pilih gendermu : ")
if opsi == "1" :
    jumlah = int(input("NOMINAL BELANJA : "))
    uang_kamu=int(input("uang_kamu : "))
    print("KEMBALIAN ANDA:  ",uang_kamu-jumlah)
    
        
if opsi == "2" :
    jumlah = int(input("NOMINAL BELANJA : "))
    uang_kamu=int(input("uang_kamu : "))
    if jumlah < 100000:
        print("HASIL DISKON ANDA: ",jumlah*5/100)
        hasil_diskon=(jumlah*5/100)
        print("KEMBALIAN KAMU: ",uang_kamu-(jumlah-hasil_diskon))
       
    elif jumlah >= 100000:
        print("HASIL DISKON ANDA: ",jumlah*10/100)
        hasil_diskon=(jumlah*10/100)
        print("KEMBALIAN KAMU: ",uang_kamu-(jumlah-hasil_diskon))