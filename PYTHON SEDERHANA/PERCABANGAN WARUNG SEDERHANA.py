print (15*"=")
print("TOKO SAYA")
print (15*"=")
print("PILIH MENU TOKO : ")
print("1.Es teh -> Rp 3000")
print("2.mie goreng -> Rp 8000")
print("beli 2 dapat diaskon 15%")
opsi = input("pilih menunya : ")
if opsi == "1" :
    jumlah = int(input("jumlah : "))
    uang_kamu=int(input("uang_kamu : "))
    harga=3000
    diskon=20/100
    if jumlah == 1:
        print("kamu akan membeli es teh berjumlah : ",jumlah , "dengan harga: ",harga)
    elif jumlah == 2:
        print("kamu membeli Es teh berjumlah: ",jumlah, "dengan harga: ",harga, "dan mendapatkan diskon sebesar 20%")
        print ("total diskon :",harga*jumlah*20/100)
        
        
if opsi == "2" :
    jumlah = int(input("jumlah : "))
    uang_kamu=int(input("uang_kamu : "))
    harga=8000
    diskon=20/100
    if jumlah == 1:
        print("kamu akan membeli mie goreng berjumlah : ",jumlah , "dengan harga: ",harga)
    elif jumlah == 2:
        print("kamu membeli mie goreng berjumlah: ",jumlah, "dengan harga: ",harga, "dan mendapatkan diskon sebesar 20%")
        print ("total diskon :",harga*jumlah*20/100)