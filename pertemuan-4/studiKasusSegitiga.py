tinggi = int(input('Masukkan tinggi segitiga : '))


print('--- Segitiga Sama Kaki ---')
for i in range(1, tinggi + 1):
    spasi = ' ' * (tinggi - i)
    bintang = '*' * (2 * i - 1) 
    print(spasi + bintang)

print('\n') 

print('--- Segitiga Sama Kaki Terbalik ---')
for i in range(tinggi, 0, -1):
    spasi = ' ' * (tinggi - i)
    bintang = '*' * (2 * i - 1)
    print(spasi + bintang)