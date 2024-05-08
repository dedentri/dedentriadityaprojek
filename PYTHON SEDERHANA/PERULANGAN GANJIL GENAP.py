jalan = True
while (jalan==True):
    print('=='*20)
    print('MASUKAN NILAI AWAL DAN AKHIR')
    print('=='*20)
    nilaiawal=int(input('masukan nilai awal: '))
    nilaiakhir=int(input('masukan nilai akhir: '))
    print('1.ganjil')
    print('2.genap')
    masukanopsi= input ('opsi (1 or 2): ')

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



l=input('lagi (y/n): ')
if (l=='n'):
    jalan=False