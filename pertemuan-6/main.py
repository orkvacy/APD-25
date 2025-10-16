# # Membuat set
# buah = {"apel", "jeruk", "mangga", "apel"}
# # print(buah)
# for i in buah:
#     print(i, end=' ')


# angka = [1,1,2,5,2,3,6] #017

# unik = set(angka)
# print(unik)

# Daftar_buku = {
# "Novel" : "Bumi Manusia",
# "Buku2" : "Laut Bercerita"
# }

# print(Daftar_buku["Novel"]) #038 , 15


Biodata = {
"Nama" : "Ananda Daffa Harahap",
"NIM" : 2409106050,
"KRS" : ["Pemrograman Web", "Struktur Data", "Basis Data"],
"Mahasiswa_Aktif" : True,
"Social Media" : {"Instagram" : "daffahrhap"}
}

# print (Biodata) # 035 # 004
# for i, j in Biodata.items():
#     print(i)
#     print(j)

# print(f"nama saya adalah {Biodata['Nama']}")
# print(f"Instagram : {Biodata['Social Media']['Instagram']}")
# print(f"nama saya adalah {Biodata.get("nama")}")
# print(Biodata.get("Nama"))

# Film = {
# "Avenger Endgame" : "Action",
# "Sherlock Holmes" : "Mystery",
# "The Conjuring" : "Horror"}
# print(Film)
# Film.clear()
# print(Film)


# print(Film)

# Film["ZombieLand"] = "Comedy"
# Film.update({"Upin ipin" : "Comedy"})
# #Setelah Ditambah
# print(Film)



# Musik = {
#     "The Chainsmoker": ["All we Know", "The Paris"],
#     "Alan Walker": ["Alone", "Lily"],
#     "Neffex": ["Best of Me",['tes','halo'], "Memories"],
#     'Paramore' : ["Misery Business", "Ain't It Fun", 
#                 ['All We Know Is Falling',['Here We Go Again', 'My Heart']],'This Is Why' ]
# }

# print(Musik['Paramore'][2][1][0]) #007 , #021, #031




# a = {10,11,12}
# b = {11,13,14}

# c = a | b # 013 002

# print(c)



# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81
# }

# print("Nilai : ", Nilai.setdefault("Kimia", 70))
# print(Nilai)



# 024
mahasiswa = [["Daffa", "Dante", "Santoso"], ["Pernanda", "Triya", "Ahnaf"]]
# perulangan for untuk mendapatkan semua elemen
for i in mahasiswa:
    for j in i :
        print (j)   

