print(20*'=')
print('KALKULATOR BMI')
print(20*'=')

berat_badan=float(input('masukan berat badan kamu:  '))
tinggi_badan=float(input('masukan tinggi badan kamu:  '))

print(20*'==')
hasil=berat_badan/(tinggi_badan/100)**2
print('HASIL BMI ADALAH: ',hasil)
print(20*'==')

print('KETERANGAN:')

if hasil < 18:
    print('berat badan kamu kurang')
elif hasil < 22.9:
    print('berat badan kamu normal')
elif hasil == 23:
    print('berat badan kamu berlebihan')
elif hasil <= 24:
    print('berat badan kamu terlalu berlebihan')
elif hasil <= 29.9:
    print('obesitas tahap 1')
else:
    print('obesitas tahap 2,bahaya!!!')