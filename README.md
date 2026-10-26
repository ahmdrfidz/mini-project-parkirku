# ParkirKu — Aplikasi CLI Pencatat Parkir Kampus

> Mini project **Tugas Individu #1 — Algoritma dan Pemrograman (BBK1AAB4)** dari **Asisten Praktikum (Asprak) Telkom University Surabaya**, Semester 1, tahun 2026.

ParkirKu adalah aplikasi berbasis teks (*command line interface*) untuk membantu petugas gerbang parkir kampus. Program mencatat setiap kendaraan yang keluar selama satu hari, menghitung biaya parkirnya secara otomatis, mencetak struk, lalu menampilkan rekap harian saat petugas selesai bertugas.

Proyek ini mengikuti skenario dari soal: petugas parkir yang selama ini mencatat di buku dan menghitung tarif dengan kalkulator sering salah hitung. Unit Sarana dan Prasarana membutuhkan prototipe program yang menghitung tarif dan membuat rekap sendiri.

---

## Fitur

- **Tabel tarif** 1–8 jam untuk motor dan mobil, dicetak saat program dimulai.
- **Validasi masukan**: setiap isian diulang sampai benar (jenis kendaraan, jam 0–23, menit 0–59, waktu keluar tidak boleh sebelum waktu masuk, jawaban ya/tidak).
- **Perhitungan biaya otomatis**: durasi, jam ditagih (dibulatkan ke atas), gratis ≤ 15 menit, batas maksimum per hari, diskon 20% kartu civitas, denda tiket hilang.
- **Struk** untuk setiap kendaraan.
- **Pencatatan berulang** sampai petugas mengetik `SELESAI`.
- **Rekap harian**: jumlah kendaraan (motor/mobil), parkir gratis, berdiskon, kena denda, total dan rata-rata pendapatan, parkir terlama, bayar tertinggi, serta grafik batang teks.

Fitur tambahan di luar soal:

- Isian jam/menit berisi huruf (mis. `8a`) ditolak tanpa membuat program galat.
- Plat kosong ditolak; plat dan kata `SELESAI` tidak membedakan huruf besar/kecil.
- Rekap pendapatan per jenis kendaraan dan total diskon yang diberikan.

## Aturan Tarif

| Jenis | Jam pertama | Tiap jam berikutnya | Maksimum per hari |
|---|---:|---:|---:|
| Motor | Rp 2.000 | Rp 1.000 | Rp 8.000 |
| Mobil | Rp 4.000 | Rp 2.000 | Rp 16.000 |

- Durasi ≤ 15 menit: tarif dasar Rp 0 (gratis).
- Diskon 20% bila punya kartu civitas, tiket tidak hilang, dan tarif dasar > 0.
- Denda tiket hilang Rp 10.000, tetap berlaku walau durasinya gratis.
- `Total = tarif dasar − diskon + denda`

## Cara Menjalankan

Membutuhkan **Python 3.12** (atau lebih baru). Tidak ada pustaka tambahan.

```bash
python parkir.py
```

Bisa juga dijalankan langsung dari **Thonny** atau **VS Code** (tekan Run / F5).

Untuk menguji dengan data contoh dari soal sekaligus:

```bash
# Command Prompt
python parkir.py < penjelasan\data-uji\uji_contoh.txt

# PowerShell
Get-Content penjelasan\data-uji\uji_contoh.txt | python parkir.py
```

## Contoh Penggunaan

```
===== PARKIRKU KAMPUS SURABAYA =====

Plat nomor (ketik SELESAI untuk berhenti): L 1234 AB
Jenis kendaraan (motor/mobil): motor
Jam masuk (0-23): 8
Menit masuk (0-59): 0
Jam keluar (0-23): 11
Menit keluar (0-59): 20
Punya kartu civitas? (ya/tidak): ya
Tiket hilang? (ya/tidak): tidak

--- STRUK L 1234 AB ---
Jenis       : motor
Durasi      : 3 jam 20 menit
Jam ditagih : 4
Tarif dasar : Rp 5000
Diskon      : Rp 1000
Denda       : Rp 0
TOTAL       : Rp 4000
```

Rekap setelah kelima data uji soal dimasukkan:

```
===== REKAP PARKIR HARI INI =====
Jumlah kendaraan    : 5
  Motor             : 3
  Mobil             : 2
Parkir gratis       : 1
Mendapat diskon     : 2
Kena denda tiket    : 1
Total pendapatan    : Rp 30400
Rata-rata/kendaraan : Rp 6080
Parkir terlama      : S 9012 EF ( 12 jam 15 menit )
Bayar tertinggi     : L 3456 GH ( Rp 12000 )
Grafik jumlah kendaraan:
Motor | ### (3)
Mobil | ## (2)
```

## Struktur Program

Program ditulis dalam satu berkas `parkir.py` dan dibagi menjadi lima tahap:

| Tahap | Nama | Konsep yang dipakai |
|---|---|---|
| 1 | Konstanta & Tabel Tarif | konstanta, `for` + `range()` |
| 2 | Masukan & Validasi | `input()`, `int()`, `while`, `and`/`or`/`not` |
| 3 | Hitung Biaya & Struk | `if`/`elif`/`else`, operator `//` dan `%` |
| 4 | Perulangan Berpenanda | `while` dengan sentinel `SELESAI` |
| 5 | Rekap Akhir | pencacah, akumulator, penyaringan, nilai ekstrem |

Sesuai ketentuan tugas, program **hanya** memakai materi pekan 1–6. Tidak ada `def`, list, tuple, dictionary, `import`, `try/except`, `break`, `continue`, maupun `while True`. Semua angka aturan disimpan sebagai konstanta di bagian atas program.

## Isi Repositori

```
mini-project-parkir/
├── parkir.py                     # program utama
├── README.md                     # berkas ini
├── README-NIM.pdf                # dokumentasi tugas (dekomposisi, penelusuran, kasus uji, dll.)
├── flowchart.drawio              # flowchart 6 halaman (buka di app.diagrams.net)
├── buka-flowchart-di-drawio.html # pintasan untuk membuka flowchart di draw.io
└── penjelasan/                   # materi belajar per tahap
    ├── 00-BACA-DULU.md
    ├── 01-tahap1-konstanta-tabel.md
    ├── 02-tahap2-masukan-validasi.md
    ├── 03-tahap3-hitung-biaya.md
    ├── 04-tahap4-perulangan-berpenanda.md
    ├── 05-tahap5-rekap-akhir.md
    ├── 06-persiapan-audit.md
    ├── data-uji/                 # berkas masukan untuk pengujian
    ├── gambar-flowchart/         # flowchart dalam bentuk gambar PNG
    └── latihan-galat/            # 6 latihan mencari galat + kunci jawaban
```

Yang dikumpulkan ke LMS CeLOE hanya `parkir.py` dan `README-<NIM>.pdf`, dikompres menjadi `NIM_NamaLengkap.zip`.

## Pengujian

Program sudah diuji dengan:

- Lima data uji contoh dari soal: semua total dan rekap sesuai (Rp 30.400, rata-rata Rp 6.080).
- Data penelusuran: total pendapatan Rp 8.400, rata-rata Rp 2.800.
- Kasus batas: tepat 15 menit, 16 menit, tepat 60 dan 61 menit, durasi 0 menit, tarif tepat di batas maksimum, parkir seharian (00:00–23:59), data kosong, dan kasus seri.
- Masukan tidak valid: jenis salah, jam/menit di luar rentang, waktu keluar lebih awal, huruf pada isian angka, plat kosong.

Rincian lengkap ada di `README-NIM.pdf` bagian *Tabel Kasus Uji*.

## Informasi Tugas

| | |
|---|---|
| Mata kuliah | Algoritma dan Pemrograman (BBK1AAB4), 4 SKS |
| Penyusun soal | Asisten Praktikum, Telkom University Surabaya |
| Jenis | Tugas Individu #1 — Mini Project |
| Batas pengumpulan | Sebelum pekan ke-9 (lihat LMS CeLOE) |
| Bahasa | Python 3.12 |

## Penulis

- **Nama:** Ahmad Rafid Zaidan
- **NIM:** 108052630010
- **Kelas:** SS1SI-50-REG-05

## Pengungkapan Penggunaan AI

Sesuai ketentuan integritas akademik pada soal, pengerjaan proyek ini dibantu asisten AI **Claude (Anthropic)** untuk penyusunan kode, dokumentasi, dan flowchart. Seluruh kode telah dijalankan, diuji, dan dipelajari agar dapat dijelaskan saat sesi audit. Rincian lengkap ada di `README-NIM.pdf` bagian *Pengungkapan Penggunaan AI*.
