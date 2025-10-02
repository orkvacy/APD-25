tempA = int(input('Masukkan angka pertama\t: '))
tempB = int(input('Masukkan angka kedua\t: '))

if tempA > tempB:
    angkaBesar = tempA
    angkaKecil = tempB
else:
    angkaBesar = tempB
    angkaKecil = tempA

tempKPK = angkaBesar

while True:
    if tempKPK % angkaKecil == 0 and tempKPK % angkaBesar == 0:
        print(f'KPK dari {tempA} dan {tempB} yaitu : {tempKPK}')
        break
    tempKPK = tempKPK + angkaBesar
