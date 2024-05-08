#LATIHAN 1

print(20*"=")
print("KALKULATOR SEDERHANA")
print(20*"=")

angka1=float(input("masukan angka1= "))
operator = input ("operator (+,-,x,/) : ")
angka2=float(input("masukan angka2 = "))

#PERCABANGAN 

if operator == "+":
    hasil = angka1 + angka2
    print(f"hasilnya adalah {hasil}")
elif operator == "-":
    hasil = angka1 - angka2
    print(f"hasilnya adalah {hasil}")
elif operator == "x":
    hasil = angka1 * angka2
    print(f"hasilnya adalah {hasil}")
elif operator == "/":
    hasil = angka1 / angka2
    print(f"hasilnya adalah {hasil}")