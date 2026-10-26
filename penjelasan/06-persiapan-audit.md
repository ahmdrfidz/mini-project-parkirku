# 06 — Persiapan Audit (Tanya Jawab & Debugging Langsung)

Saat audit, dosen akan (1) meminta kamu menjelaskan kode, dan (2) **menyisipkan satu galat** lalu memintamu menemukan dan memperbaikinya. Bobot debugging 10% (sintaks 4%, logika 3%, runtime 3%), kemampuan menjelaskan 10%. Kode yang tidak bisa kamu jelaskan bisa bernilai 0, jadi bagian ini penting.

---

## Bagian A — Latihan menjawab (tutup jawabannya, coba jawab sendiri dulu)

<details><summary><b>1. Apa beda galat sintaks, runtime, dan logika?</b></summary>

- **Sintaks**: aturan penulisan Python dilanggar (titik dua hilang, kurung tidak tertutup, indentasi salah). Program **tidak jalan sama sekali**.
- **Runtime**: penulisan benar, tetapi saat dijalankan ada operasi yang tidak mungkin (bagi nol, nama variabel tidak ada, `int("abc")`). Program **berhenti di tengah** dengan *traceback*.
- **Logika**: program jalan sampai selesai tanpa pesan galat, tetapi **hasilnya salah**. Hanya bisa ditemukan dengan membandingkan hasil terhadap perhitungan tangan.
</details>

<details><summary><b>2. Kenapa <code>durasi_terlama</code> mulai dari −1?</b></summary>

Durasi sah terkecil adalah 0 menit. Dengan nilai awal 0, kendaraan pertama berdurasi 0 tidak lolos `0 > 0`, sehingga plat terlama kosong. −1 lebih kecil dari semua durasi sah, jadi kendaraan pertama pasti menjadi "juara sementara".
</details>

<details><summary><b>3. Kenapa jam ditagih memakai <code>(durasi + 59) // 60</code>?</b></summary>

`//` membulatkan ke bawah, padahal tarif dibulatkan ke **atas**. Menambah 59 sebelum dibagi membuat sisa menit berapa pun (1–59) "naik" ke jam berikutnya, sedangkan kelipatan 60 yang pas tidak ikut naik. 60 menit → 119 // 60 = 1; 61 menit → 120 // 60 = 2.
</details>

<details><summary><b>4. Kenapa validasi jenis memakai <code>and</code>, bukan <code>or</code>?</b></summary>

Yang kita ulang adalah "bukan motor **dan** bukan mobil". Dengan `or`, kata `motor` tetap memenuhi `!= "mobil"`, sehingga kondisinya selalu benar dan program bertanya tanpa henti.
</details>

<details><summary><b>5. Bagaimana kamu menjamin setiap <code>while</code> pasti berhenti?</b></summary>

Setiap `while` punya variabel kondisi yang **diubah di dalam bloknya**: plat dibaca ulang di akhir blok (sentinel), `jenis`/`jawab_*` dibaca ulang, dan `waktu_*_sah` diberi `True` begitu masukan benar. Begitu pengguna mengetik masukan yang benar, kondisinya menjadi salah dan perulangan berhenti.
</details>

<details><summary><b>6. Kenapa memakai <code>isdigit()</code>? Soal bilang pengguna selalu mengetik angka.</b></summary>

Itu fitur tambahan untuk kasus tidak lazim. Tanpa `isdigit()`, mengetik `8a` membuat `int()` gagal (`ValueError`) dan program berhenti. `try/except` dilarang, jadi diperiksa dulu sebelum dikonversi (pola penjaga).
</details>

<details><summary><b>7. Kenapa tidak ada <code>def</code>? Bukankah rumus tarif jadi ditulis dua kali?</b></summary>

`def` dilarang di tugas ini (baru dipakai di tugas berikutnya). Rumus tarif memang muncul di Tahap 1 dan Tahap 3, tetapi bentuknya dibuat **persis sama** (hitung, lalu potong ke maksimum) dan semua angkanya konstanta, sehingga tabel dan tagihan pasti cocok.
</details>

<details><summary><b>8. Kenapa <code>for</code> di tabel dan grafik, tetapi <code>while</code> di tempat lain?</b></summary>

`for` + `range()` untuk perulangan yang jumlahnya diketahui (8 baris tabel, n tanda `#`). `while` untuk perulangan yang berhenti karena kondisi (masukan valid, plat `SELESAI`).
</details>

<details><summary><b>9. Jelaskan urutan operasi pada <code>tarif_dasar * PERSEN_DISKON // PERSEN_PENUH</code>.</b></summary>

`*` dan `//` setara, dikerjakan dari kiri: `(tarif_dasar * 20) // 100`. Bila dibalik (`tarif_dasar * (20 // 100)`), hasilnya `tarif_dasar * 0 = 0`. Itu galat logika.
</details>

<details><summary><b>10. Apa yang terjadi bila nilai awal rekap ditaruh di dalam <code>while</code>?</b></summary>

Setiap kendaraan baru me-reset rekap ke 0, sehingga rekap hanya mencerminkan kendaraan terakhir.
</details>

<details><summary><b>11. Kenapa <code>SELESAI</code> tidak ikut terhitung?</b></summary>

Plat dibaca di akhir blok, lalu langsung diperiksa oleh kondisi `while` sebelum sempat diproses. Pencacah ada di dalam badan, jadi tidak pernah dijalankan untuk `SELESAI`.
</details>

<details><summary><b>12. Bagaimana jika petugas langsung mengetik SELESAI?</b></summary>

Badan `while` tidak pernah dijalankan, `jumlah_kendaraan` tetap 0, cabang `if jumlah_kendaraan == 0` mencetak "Belum ada kendaraan yang tercatat." Rata-rata (pembagian) dan nilai ekstrem tidak disentuh, sehingga tidak ada `ZeroDivisionError`.
</details>

---

## Bagian B — Latihan debugging (folder `latihan-galat/`)

Folder `latihan-galat/` berisi 6 salinan `parkir.py`. **Masing-masing punya tepat satu galat.** Jalankan, temukan, dan perbaiki seperti saat audit. Kunci ada di `latihan-galat/KUNCI-JAWABAN.md`. Jangan dibuka sebelum mencoba.

| Berkas | Petunjuk gejala | Data uji |
|---|---|---|
| `latihan1.py` | program tidak mau jalan sama sekali | apa saja |
| `latihan2.py` | struk pertama tercetak, lalu program berhenti dengan pesan galat | `uji_contoh.txt` |
| `latihan3.py` | program berhenti setelah jam & menit masuk diketik | `uji_contoh.txt` |
| `latihan4.py` | total pendapatan Rp 34400, bukan Rp 30400 | `uji_contoh.txt` |
| `latihan5.py` | hasil data uji soal benar semua, tetapi ada yang salah pada kasus seri | `uji_seri.txt` |
| `latihan6.py` | "Mendapat diskon" 4, total pendapatan Rp 28400 | `uji_contoh.txt` |

Cara menjalankan dengan data uji (Command Prompt, dari folder `penjelasan`):

```
python latihan-galat\latihan4.py < data-uji\uji_contoh.txt
```

## Bagian C — Strategi mencari galat saat audit

1. **Baca pesan galatnya dari bawah.** Baris terakhir menyebut jenis galat (`SyntaxError`, `NameError`, `TypeError`, `ZeroDivisionError`, `ValueError`). Baris di atasnya menyebut nomor baris.
2. **`SyntaxError`**: periksa baris yang ditunjuk **dan baris sebelumnya** (kurung atau tanda kutip yang belum ditutup sering terdeteksi di baris berikutnya). Cek titik dua pada `if/elif/else/while/for`, indentasi 4 spasi.
3. **`NameError`**: cari salah ketik nama variabel atau variabel yang belum diberi nilai awal.
4. **`TypeError` antara `str` dan `int`**: ada `input()` yang lupa diubah dengan `int()`.
5. **Galat logika** (tidak ada pesan):
   - Jalankan `uji_contoh.txt` dan bandingkan **total per struk** dengan tabel 3.7 soal. Struk mana yang pertama kali salah?
   - Lihat struknya: jam ditagih, tarif dasar, diskon, atau denda yang salah? Itu menunjuk langsung ke langkah Tahap 3 yang rusak.
   - Periksa **operator pembanding** di kondisi batas (`<` vs `<=`, `>` vs `>=`), **`and` vs `or`**, **nilai awal**, dan **letak** baris (di dalam atau di luar `while`).
   - Bila perlu, tambahkan `print()` sementara untuk melihat nilai variabel (lalu hapus lagi).
6. **Program bertanya terus tanpa henti** → periksa kondisi `while` validasi (`and`/`or` terbalik) atau variabel kondisi yang tidak pernah berubah.

## Bagian D — Checklist sebelum audit

- [ ] Bisa menggambar ulang alur program utama tanpa melihat (lihat `00-BACA-DULU.md`).
- [ ] Bisa menghitung tangan data penelusuran 5.1 dalam 5 menit.
- [ ] Bisa menjelaskan 6 plan: penjaga, validasi `while`, sentinel, pencacah, akumulator, nilai ekstrem.
- [ ] Sudah menyelesaikan keenam latihan galat.
- [ ] Sudah menulis ulang Refleksi di README dengan kata-kata sendiri.
