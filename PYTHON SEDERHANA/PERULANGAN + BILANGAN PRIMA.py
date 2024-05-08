jalan = True
while (jalan==True):
    print('=='*20)
    print('MASUKAN NILAI AWAL DAN AKHIR')
    print('=='*20)
    nilaiawal=int(input('masukan nilai awal: '))
    nilaiakhir=int(input('masukan nilai akhir: '))
    print('1.ganjil')
    print('2.genap')
    masukanopsi= input ('opsi (1,2,AND 3): ')

#ganjil
    if masukanopsi == '1':
        for i in range (nilaiawal,nilaiakhir):
            if i %2 == 1:
                print(i)

#genap  
    elif masukanopsi == '2':
        for i in range (nilaiawal,nilaiakhir):
            if i %2 == 0:
                print(i)

#BILANGAN PRIMA
    elif masukanopsi == '3':
        list_angka = [i for i in range(nilaiawal, nilaiakhir +1 )]
        bilangan_prima = [i for i in list_angka if (i==2 or i==3 or i==5 or i==7) or (i%2 != 0 and i%3 != 0 and i%5 != 0 and i%7 != 0)]
 
        print(bilangan_prima)
        
        
l=input('lagi (y/n): ')
if (l=='n'):
    jalan=False