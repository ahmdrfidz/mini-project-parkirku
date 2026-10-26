# ==============================================================
# ParkirKu - Pencatat Parkir Kampus Surabaya
# Tugas Individu #1 Algoritma dan Pemrograman 2026
#
# Program mencatat kendaraan yang keluar dari area parkir selama
# satu hari, menghitung biaya tiap kendaraan, lalu menampilkan
# rekap ketika petugas mengetik SELESAI.
#
# Hanya memakai materi pekan 1-6: variabel, tipe data, input(),
# operator, if/elif/else, and/or/not, while, for, dan range().
# ==============================================================


# ==============================================================
# TAHAP 1 - KONSTANTA & TABEL TARIF
# Semua angka aturan disimpan di sini agar mudah diubah dan
# tidak ada "angka ajaib" di tengah rumus.
# ==============================================================

# Tarif motor (rupiah)
TARIF_MOTOR_PERTAMA = 2000
TARIF_MOTOR_BERIKUTNYA = 1000
TARIF_MOTOR_MAKS = 8000

# Tarif mobil (rupiah)
TARIF_MOBIL_PERTAMA = 4000
TARIF_MOBIL_BERIKUTNYA = 2000
TARIF_MOBIL_MAKS = 16000

# Aturan tambahan
BATAS_GRATIS_MENIT = 15       # durasi <= 15 menit tarif dasarnya 0
PERSEN_DISKON = 20            # diskon kartu civitas 20%
PERSEN_PENUH = 100            # pembagi persen
DENDA_TIKET_HILANG = 10000    # denda tiket hilang

# Batas waktu dalam satu hari
JAM_TERKECIL = 0
JAM_TERBESAR = 23
MENIT_TERKECIL = 0
MENIT_TERBESAR = 59
MENIT_PER_JAM = 60

# Tabel tarif dicetak untuk 1 sampai 8 jam
JAM_TABEL_AWAL = 1
JAM_TABEL_AKHIR = 8

# Kata-kata yang dikenali program
PENANDA_SELESAI = "SELESAI"
JENIS_MOTOR = "motor"
JENIS_MOBIL = "mobil"
JAWAB_YA = "ya"
JAWAB_TIDAK = "tidak"
TANYA_PLAT = "Plat nomor (ketik SELESAI untuk berhenti): "

print("===== PARKIRKU KAMPUS SURABAYA =====")
print()
print("Tabel tarif parkir (sudah termasuk batas maksimum per hari)")
print("+-----+------------+------------+")
print("| Jam |   Motor    |   Mobil    |")
print("+-----+------------+------------+")
for jam in range(JAM_TABEL_AWAL, JAM_TABEL_AKHIR + 1):
    # Rumus yang sama persis dengan Tahap 3
    tarif_motor = TARIF_MOTOR_PERTAMA + (jam - 1) * TARIF_MOTOR_BERIKUTNYA
    if tarif_motor > TARIF_MOTOR_MAKS:
        tarif_motor = TARIF_MOTOR_MAKS
    tarif_mobil = TARIF_MOBIL_PERTAMA + (jam - 1) * TARIF_MOBIL_BERIKUTNYA
    if tarif_mobil > TARIF_MOBIL_MAKS:
        tarif_mobil = TARIF_MOBIL_MAKS
    print(f"| {jam:>3} | Rp {tarif_motor:>7} | Rp {tarif_mobil:>7} |")
print("+-----+------------+------------+")
print(f"* Parkir {BATAS_GRATIS_MENIT} menit atau kurang: gratis.")
print(f"* Diskon {PERSEN_DISKON}% untuk kartu civitas (tiket tidak hilang).")
print(f"* Denda tiket hilang: Rp {DENDA_TIKET_HILANG}.")
print()

# ----- Variabel rekap (diberi nilai awal sebelum perulangan) -----
jumlah_kendaraan = 0          # pencacah
jumlah_motor = 0              # pencacah
jumlah_mobil = 0              # pencacah
jumlah_gratis = 0             # penyaringan + pencacah
jumlah_diskon = 0             # penyaringan + pencacah
jumlah_denda = 0              # penyaringan + pencacah
total_pendapatan = 0          # akumulator
pendapatan_motor = 0          # akumulator (fitur tambahan)
pendapatan_mobil = 0          # akumulator (fitur tambahan)
total_diskon_diberikan = 0    # akumulator (fitur tambahan)
durasi_terlama = -1           # nilai ekstrem: -1 < durasi terkecil (0)
plat_terlama = ""
bayar_tertinggi = -1          # nilai ekstrem: -1 < total terkecil (0)
plat_tertinggi = ""


# ==============================================================
# TAHAP 4 - PERULANGAN BERPENANDA (SENTINEL)
# Plat dibaca SEKALI sebelum while (priming read), lalu dibaca
# lagi di akhir blok. Perulangan berhenti saat plat = SELESAI.
# ==============================================================
plat = input(TANYA_PLAT).strip().upper()
while plat == "":
    print("Plat nomor tidak boleh kosong.")
    plat = input(TANYA_PLAT).strip().upper()

while plat != PENANDA_SELESAI:

    # ==========================================================
    # TAHAP 2 - MASUKAN & VALIDASI
    # Setiap pertanyaan diulang dengan while sampai valid.
    # ==========================================================

    # --- Jenis kendaraan: hanya motor atau mobil ---
    jenis = input("Jenis kendaraan (motor/mobil): ").strip().lower()
    while jenis != JENIS_MOTOR and jenis != JENIS_MOBIL:
        print("Jenis harus motor atau mobil.")
        jenis = input("Jenis kendaraan (motor/mobil): ").strip().lower()

    # --- Waktu masuk: jam 0-23, menit 0-59 ---
    waktu_masuk_sah = False
    while not waktu_masuk_sah:
        jam_masuk_teks = input(f"Jam masuk ({JAM_TERKECIL}-{JAM_TERBESAR}): ").strip()
        menit_masuk_teks = input(f"Menit masuk ({MENIT_TERKECIL}-{MENIT_TERBESAR}): ").strip()
        if not (jam_masuk_teks.isdigit() and menit_masuk_teks.isdigit()):
            # Penjaga tambahan: cegah int() galat bila petugas salah ketik huruf
            print("Jam dan menit harus berupa angka bulat.")
        else:
            jam_masuk = int(jam_masuk_teks)
            menit_masuk = int(menit_masuk_teks)
            if (jam_masuk < JAM_TERKECIL or jam_masuk > JAM_TERBESAR
                    or menit_masuk < MENIT_TERKECIL or menit_masuk > MENIT_TERBESAR):
                print("Waktu tidak valid.")
            else:
                waktu_masuk_sah = True
    total_menit_masuk = jam_masuk * MENIT_PER_JAM + menit_masuk

    # --- Waktu keluar: rentang sama, dan tidak sebelum waktu masuk ---
    waktu_keluar_sah = False
    while not waktu_keluar_sah:
        jam_keluar_teks = input(f"Jam keluar ({JAM_TERKECIL}-{JAM_TERBESAR}): ").strip()
        menit_keluar_teks = input(f"Menit keluar ({MENIT_TERKECIL}-{MENIT_TERBESAR}): ").strip()
        if not (jam_keluar_teks.isdigit() and menit_keluar_teks.isdigit()):
            print("Jam dan menit harus berupa angka bulat.")
        else:
            jam_keluar = int(jam_keluar_teks)
            menit_keluar = int(menit_keluar_teks)
            total_menit_keluar = jam_keluar * MENIT_PER_JAM + menit_keluar
            if (jam_keluar < JAM_TERKECIL or jam_keluar > JAM_TERBESAR
                    or menit_keluar < MENIT_TERKECIL or menit_keluar > MENIT_TERBESAR):
                print("Waktu tidak valid.")
            elif total_menit_keluar < total_menit_masuk:
                print("Waktu keluar tidak boleh sebelum waktu masuk.")
            else:
                waktu_keluar_sah = True

    # --- Kartu civitas: hanya ya atau tidak ---
    jawab_kartu = input("Punya kartu civitas? (ya/tidak): ").strip().lower()
    while jawab_kartu != JAWAB_YA and jawab_kartu != JAWAB_TIDAK:
        print("Jawaban harus ya atau tidak.")
        jawab_kartu = input("Punya kartu civitas? (ya/tidak): ").strip().lower()
    punya_kartu = jawab_kartu == JAWAB_YA

    # --- Tiket hilang: hanya ya atau tidak ---
    jawab_tiket = input("Tiket hilang? (ya/tidak): ").strip().lower()
    while jawab_tiket != JAWAB_YA and jawab_tiket != JAWAB_TIDAK:
        print("Jawaban harus ya atau tidak.")
        jawab_tiket = input("Tiket hilang? (ya/tidak): ").strip().lower()
    tiket_hilang = jawab_tiket == JAWAB_YA

    # ==========================================================
    # TAHAP 3 - HITUNG BIAYA & STRUK
    # ==========================================================
    durasi = total_menit_keluar - total_menit_masuk
    jam_tagih = (durasi + MENIT_PER_JAM - 1) // MENIT_PER_JAM   # bulat ke atas

    # Pilih tarif sesuai jenis kendaraan
    if jenis == JENIS_MOTOR:
        tarif_pertama = TARIF_MOTOR_PERTAMA
        tarif_berikutnya = TARIF_MOTOR_BERIKUTNYA
        tarif_maks = TARIF_MOTOR_MAKS
    else:
        tarif_pertama = TARIF_MOBIL_PERTAMA
        tarif_berikutnya = TARIF_MOBIL_BERIKUTNYA
        tarif_maks = TARIF_MOBIL_MAKS

    # Tarif dasar: gratis bila <= 15 menit; selain itu rumus jam,
    # lalu dipotong ke batas maksimum (rumus sama dengan tabel Tahap 1)
    if durasi <= BATAS_GRATIS_MENIT:
        tarif_dasar = 0
    else:
        tarif_dasar = tarif_pertama + (jam_tagih - 1) * tarif_berikutnya
        if tarif_dasar > tarif_maks:
            tarif_dasar = tarif_maks

    # Diskon: punya kartu DAN tiket tidak hilang DAN tarif dasar > 0
    if punya_kartu and not tiket_hilang and tarif_dasar > 0:
        diskon = tarif_dasar * PERSEN_DISKON // PERSEN_PENUH
    else:
        diskon = 0

    # Denda: tetap dikenakan walaupun durasinya gratis
    if tiket_hilang:
        denda = DENDA_TIKET_HILANG
    else:
        denda = 0

    total = tarif_dasar - diskon + denda

    # Cetak struk
    print()
    print(f"--- STRUK {plat} ---")
    print(f"Jenis       : {jenis}")
    print(f"Durasi      : {durasi // MENIT_PER_JAM} jam {durasi % MENIT_PER_JAM} menit")
    print(f"Jam ditagih : {jam_tagih}")
    print(f"Tarif dasar : Rp {tarif_dasar}")
    print(f"Diskon      : Rp {diskon}")
    print(f"Denda       : Rp {denda}")
    print(f"TOTAL       : Rp {total}")
    print()

    # ----- Perbarui variabel rekap (bagian dari Tahap 5) -----
    jumlah_kendaraan = jumlah_kendaraan + 1
    total_pendapatan = total_pendapatn + total
    if jenis == JENIS_MOTOR:
        jumlah_motor = jumlah_motor + 1
        pendapatan_motor = pendapatan_motor + total
    else:
        jumlah_mobil = jumlah_mobil + 1
        pendapatan_mobil = pendapatan_mobil + total
    if tarif_dasar == 0:
        jumlah_gratis = jumlah_gratis + 1
    if diskon > 0:
        jumlah_diskon = jumlah_diskon + 1
        total_diskon_diberikan = total_diskon_diberikan + diskon
    if denda > 0:
        jumlah_denda = jumlah_denda + 1
    if durasi > durasi_terlama:          # ">" agar bila seri, yang lebih dulu tetap
        durasi_terlama = durasi
        plat_terlama = plat
    if total > bayar_tertinggi:          # ">" agar bila seri, yang lebih dulu tetap
        bayar_tertinggi = total
        plat_tertinggi = plat

    # Baca plat berikutnya (variabel kondisi while berubah di sini)
    plat = input(TANYA_PLAT).strip().upper()
    while plat == "":
        print("Plat nomor tidak boleh kosong.")
        plat = input(TANYA_PLAT).strip().upper()


# ==============================================================
# TAHAP 5 - REKAP AKHIR
# ==============================================================
print()
print("===== REKAP PARKIR HARI INI =====")
if jumlah_kendaraan == 0:
    # Penjaga data kosong: tidak ada rata-rata maupun nilai ekstrem
    print("Belum ada kendaraan yang tercatat.")
else:
    rata_rata = total_pendapatan // jumlah_kendaraan   # aman: jumlah > 0
    print(f"Jumlah kendaraan    : {jumlah_kendaraan}")
    print(f"  Motor             : {jumlah_motor}")
    print(f"  Mobil             : {jumlah_mobil}")
    print(f"Parkir gratis       : {jumlah_gratis}")
    print(f"Mendapat diskon     : {jumlah_diskon}")
    print(f"Kena denda tiket    : {jumlah_denda}")
    print(f"Total pendapatan    : Rp {total_pendapatan}")
    print(f"  dari motor        : Rp {pendapatan_motor}")
    print(f"  dari mobil        : Rp {pendapatan_mobil}")
    print(f"Total diskon diberi : Rp {total_diskon_diberikan}")
    print(f"Rata-rata/kendaraan : Rp {rata_rata}")
    print(f"Parkir terlama      : {plat_terlama} "
          f"( {durasi_terlama // MENIT_PER_JAM} jam {durasi_terlama % MENIT_PER_JAM} menit )")
    print(f"Bayar tertinggi     : {plat_tertinggi} ( Rp {bayar_tertinggi} )")

    # Grafik batang teks: satu tanda # untuk satu kendaraan
    print("Grafik jumlah kendaraan:")
    print("Motor | ", end="")
    for i in range(jumlah_motor):
        print("#", end="")
    print(f" ({jumlah_motor})")
    print("Mobil | ", end="")
    for i in range(jumlah_mobil):
        print("#", end="")
    print(f" ({jumlah_mobil})")

print("Terima kasih telah memakai ParkirKu.")
