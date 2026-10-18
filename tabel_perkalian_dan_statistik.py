# tabel_perkalian_dan_statistik.py

print("=== Program Tabel Perkalian dan Analisis Statistik (Nested Loop) ===")

# Penerimaan Input ukuran tabel
baris_maks = int(input("Masukkan jumlah baris (maksimum): "))
kolom_maks = int(input("Masukkan jumlah kolom (maksimum): "))

# Inisialisasi variabel untuk akumulasi dan pencacahan
total_nilai = 0
jumlah_data = 0

print(f"\n--- Tabel Perkalian {baris_maks} x {kolom_maks} ---")

# Memanfaatkan nested loop dengan dua variabel kontrol (i dan j)
for i in range(1, baris_maks + 1):
    baris_teks = ""
    for j in range(1, kolom_maks + 1):
        # Menghitung hasil perkalian sebagai pasangan data
        hasil = i * j
        
        # Akumulasi nilai dan pencacahan jumlah data
        total_nilai += hasil
        jumlah_data += 1
        
        # Menyusun format tampilan tabel
        baris_teks += f"{hasil:4d} "
        
    # Menampilkan baris hasil perulangan bersarang
    print(f"Baris {i} -> {baris_teks}")

# Menghitung rata-rata dari akumulasi data
rata_rata = total_nilai / jumlah_data if jumlah_data > 0 else 0

# Penampilan Output Statistik
print("\n--- HASIL ANALISIS STATISTIK ---")
print(f"Total Keseluruhan Nilai : {total_nilai}")
print(f"Jumlah Pasangan Data    : {jumlah_data}")
print(f"Rata-rata Nilai         : {rata_rata:.2f}")