# ulangi = 10
# for _ in range(11): #x =0, x=1
#     print(f'ini perulangan ke berapa ?')

#i = 0, i=1
# simpan = [1, 'Dapupu', 4.00, True] #06
# for i in simpan:
#     print(i)


# for i in range (0,10,2):
#     print(i)

# for i in range(1, 4):# Mengontrol baris dalam tabel perkalian
#     for j in range(1, 7):# Mengontrol kolom dalam tabel perkalian
#         print(f'{i} x {j} = {i * j}')
#     print('') #biar ada jarak tiap iterasi

# jawab = 'ya'
# hitung = 0
# while(jawab == 'ya'): 
#     hitung += 1
#     # 07
#     jawab = input("Ulang lagi? ")
#     print(f"Total perulangan: {hitung}")


# tinggi = 6
# for i in range(tinggi):
#     print("*"*i)

# for i in range(6):
#     for j in range(i):
#         print("*", end="")
#     print("")


# print("-"*50)

# loop, 11

# angka = [2, 5, 8, 9, 15, 7, 20] #7, #19
# print("Mencari angka pertama yang lebih besar dari 10...")
# for i in angka:
#     print(f"Sekarang memeriksa angka: {i}")
#     if i > 10:
#         print(f"Angka {i} lebih besar dari 10, Perulangan berhenti.")
#         break
# print("Program selesai.")


for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(f"Angka ditemukan: {i}")
print("\nProgram selesai.")