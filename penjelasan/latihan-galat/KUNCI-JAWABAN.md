# Kunci Jawaban Latihan Galat

Coba dulu semua latihan sebelum membaca ini.

---

### latihan1.py — Galat SINTAKS

- **Pesan:** `SyntaxError: expected ':'`
- **Letak:** baris 103, `while plat != PENANDA_SELESAI`
- **Penyebab:** titik dua di akhir baris `while` hilang.
- **Perbaikan:** `while plat != PENANDA_SELESAI:`
- **Pelajaran:** galat sintaks dideteksi sebelum program berjalan, karena itu tabel tarif pun tidak tercetak.

### latihan2.py — Galat RUNTIME (`NameError`)

- **Pesan:** `NameError: name 'total_pendapatn' is not defined. Did you mean: 'total_pendapatan'?`
- **Letak:** baris 220
- **Penyebab:** salah ketik nama variabel di sisi kanan `=`.
- **Perbaikan:** `total_pendapatan = total_pendapatan + total`
- **Pelajaran:** galat runtime muncul hanya saat baris itu dijalankan. Struk pertama sempat tercetak karena baris 220 baru dijalankan setelah struk.

### latihan3.py — Galat RUNTIME (`TypeError`)

- **Pesan:** `TypeError: '<' not supported between instances of 'str' and 'int'`
- **Letak:** baris 125 (`jam_masuk = jam_masuk_teks`); galat muncul di baris 127 saat dibandingkan.
- **Penyebab:** konversi `int()` dihapus, sehingga `jam_masuk` masih bertipe `str` dan tidak bisa dibandingkan dengan angka `0`.
- **Perbaikan:** `jam_masuk = int(jam_masuk_teks)`
- **Pelajaran:** `input()` **selalu** menghasilkan `str`. Baris yang dilaporkan traceback belum tentu baris penyebabnya; telusuri dari mana nilainya berasal.

### latihan4.py — Galat LOGIKA (kondisi batas)

- **Gejala:** "Parkir gratis: 0", total Rp 34400. Struk W 5678 CD (tepat 15 menit) menjadi Rp 4000, seharusnya Rp 0.
- **Letak:** baris 185, `if durasi < BATAS_GRATIS_MENIT:`
- **Penyebab:** `<` membuat tepat 15 menit tidak lagi gratis. Aturan soal: "15 menit **atau kurang**".
- **Perbaikan:** `if durasi <= BATAS_GRATIS_MENIT:`
- **Pelajaran:** selalu uji **tepat di batas** (15 menit) dan satu langkah setelahnya (16 menit).

### latihan5.py — Galat LOGIKA (nilai ekstrem saat seri)

- **Gejala:** dengan `uji_seri.txt`, parkir terlama menjadi **P2**, padahal P1 dan P2 sama-sama 1 jam dan P1 lebih dulu tercatat.
- **Letak:** baris 234, `if durasi >= durasi_terlama:`
- **Penyebab:** `>=` membuat data seri yang datang belakangan menggantikan juara.
- **Perbaikan:** `if durasi > durasi_terlama:`
- **Pelajaran:** data uji soal tidak selalu mengungkap semua galat. Kasus seri harus diuji tersendiri.

### latihan6.py — Galat LOGIKA (kondisi majemuk)

- **Gejala:** "Mendapat diskon: 4", total Rp 28400. L 3456 GH (tiket hilang) dan N 7788 IJ (tanpa kartu) ikut mendapat diskon.
- **Letak:** baris 193, `if punya_kartu or not tiket_hilang and tarif_dasar > 0:`
- **Penyebab:** `or` seharusnya `and`. Ditambah lagi, `and` lebih kuat daripada `or`, sehingga Python membacanya sebagai `punya_kartu or (not tiket_hilang and tarif_dasar > 0)`.
- **Perbaikan:** `if punya_kartu and not tiket_hilang and tarif_dasar > 0:`
- **Pelajaran:** urutan prioritas operator logika adalah `not` → `and` → `or`. Bila ragu, beri tanda kurung.
