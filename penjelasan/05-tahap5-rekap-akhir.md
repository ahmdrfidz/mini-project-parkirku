# 05 — Tahap 5: Rekap Akhir

**Baris di program:** 76–90 (nilai awal), 218–239 (pembaruan tiap kendaraan), 248–282 (cetak rekap) · **Materi:** pekan 6 (plan akumulator, pencacah, penyaringan, nilai ekstrem; `for` dan `range()`)

Rekap bekerja dalam **tiga bagian** yang letaknya berbeda:

1. **Nilai awal** — sebelum perulangan (sekali saja).
2. **Pembaruan** — di dalam perulangan, setelah struk tiap kendaraan.
3. **Pencetakan** — setelah perulangan selesai.

Kalau nilai awal ditaruh di dalam perulangan, rekap akan "ter-reset" setiap kendaraan baru. Ini galat logika yang sering muncul.

---

## Plan 1 — Pencacah (counter)

```python
jumlah_kendaraan = 0                          # nilai awal
...
jumlah_kendaraan = jumlah_kendaraan + 1       # tiap kendaraan
```

Menghitung **berapa kali** sesuatu terjadi. Selalu mulai dari 0, bertambah 1.

## Plan 2 — Penyaringan + pencacah (filter)

```python
if tarif_dasar == 0:
    jumlah_gratis = jumlah_gratis + 1
if diskon > 0:
    jumlah_diskon = jumlah_diskon + 1
if denda > 0:
    jumlah_denda = jumlah_denda + 1
```

Pencacah yang hanya bertambah bila **syaratnya terpenuhi**. Perhatikan: ini **tiga `if` terpisah**, bukan `if/elif`. Satu kendaraan bisa memenuhi lebih dari satu syarat (contoh: gratis **dan** kena denda), jadi semua syarat harus diperiksa.

**Definisi "gratis":** dipakai `tarif_dasar == 0` sesuai aturan 3.0 ("tarif dasarnya Rp 0"). Kendaraan 0 menit yang tiketnya hilang tetap dihitung gratis (parkirnya gratis), walaupun total bayarnya Rp 10000 karena denda.

## Plan 3 — Akumulator

```python
total_pendapatan = 0                              # nilai awal
...
total_pendapatan = total_pendapatan + total       # tiap kendaraan
```

Seperti pencacah, tetapi yang dijumlahkan adalah **nilainya**, bukan angka 1. Fitur tambahan `pendapatan_motor`, `pendapatan_mobil`, dan `total_diskon_diberikan` memakai pola yang sama.

## Plan 4 — Akumulator ÷ pencacah (rata-rata) + penjaga pembagian nol

```python
if jumlah_kendaraan == 0:
    print("Belum ada kendaraan yang tercatat.")
else:
    rata_rata = total_pendapatan // jumlah_kendaraan
    ...
```

Bila petugas langsung mengetik `SELESAI`, `jumlah_kendaraan = 0`. Pembagian `// 0` menghasilkan **`ZeroDivisionError`** (galat runtime) dan program berhenti dengan pesan galat. Karena itu rata-rata **hanya dihitung di cabang `else`**. Soal juga meminta nilai ekstrem tidak ditampilkan saat data kosong, sehingga seluruh rekap ditaruh di cabang `else`.

## Plan 5 — Nilai ekstrem (terbesar)

```python
durasi_terlama = -1          # nilai awal
plat_terlama = ""
...
if durasi > durasi_terlama:
    durasi_terlama = durasi
    plat_terlama = plat
```

Bayangkan "juara sementara". Setiap kendaraan baru dibandingkan dengan juara. Bila lebih besar, ia menjadi juara baru, dan **platnya ikut disimpan**.

### Kenapa nilai awalnya −1, bukan 0? (pasti ditanya!)

Nilai awal harus **lebih kecil dari semua nilai yang mungkin**, agar kendaraan pertama pasti menjadi juara.

- Durasi terkecil yang sah adalah **0 menit** (masuk 23:59, keluar 23:59).
- Bila nilai awal 0 dan kendaraan pertama berdurasi 0: `0 > 0` → **False**. `plat_terlama` tetap `""`, sehingga rekap mencetak plat kosong.
- Dengan nilai awal −1: `0 > -1` → **True**. Kendaraan pertama tercatat.

`bayar_tertinggi = -1` dengan alasan yang sama: total bayar bisa Rp 0.

### Kenapa `>`, bukan `>=`?

Soal: "Bila seri, ambil yang **lebih dulu** tercatat". Dengan `>`, kendaraan berikutnya yang nilainya **sama** tidak menggantikan juara, sehingga yang pertama tetap dipertahankan. Dengan `>=`, yang **terakhir** yang menang.

Kenapa tidak memakai list lalu `max()`? List dilarang, dan memang tidak perlu: nilai ekstrem bisa diperbarui langsung saat data datang, tanpa menyimpan semua data.

## Plan 6 — Grafik batang dengan `for` dan `range()`

```python
print("Motor | ", end="")
for i in range(jumlah_motor):
    print("#", end="")
print(f" ({jumlah_motor})")
```

- `range(3)` menghasilkan 0, 1, 2 → badan diulang **3 kali** → `###`.
- `end=""` membuat `print` **tidak pindah baris**, sehingga semua `#` tersusun dalam satu baris.
- `print(f" ({jumlah_motor})")` menutup baris (pindah baris) sambil menampilkan angkanya.
- Bila `jumlah_motor = 0`, `range(0)` kosong → badan tidak dijalankan → tidak ada `#`. Tidak galat.

## Penelusuran data 5.1 (hafalkan cara menghitungnya)

| Kendaraan ke- | durasi | jam_tagih | tarif_dasar | diskon | total | jumlah | total_pendapatan | durasi_terlama |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Awal | - | - | - | - | - | 0 | 0 | -1 |
| 1 (A 1111 AA) | 40 | 1 | 2000 | 0 | 2000 | 1 | 2000 | 40 |
| 2 (B 2222 BB) | 140 | 3 | 8000 | 1600 | 6400 | 2 | 8400 | 140 |
| 3 (C 3333 CC) | 15 | 1 | 0 | 0 | 0 | 3 | 8400 | 140 |

Rekap: rata-rata `8400 // 3 = 2800`, terlama B 2222 BB (2 jam 20 menit), tertinggi B 2222 BB (Rp 6400). Data uji siap pakai: `data-uji/uji_penelusuran.txt`.

## Kemungkinan pertanyaan dosen

- *"Kenapa memakai `//` untuk rata-rata, bukan `/`?"* → soal meminta pembagian bulat; `/` menghasilkan `float` seperti `6080.0`.
- *"Pindahkan `jumlah_kendaraan = 0` ke dalam `while`, apa yang terjadi?"* → setiap kendaraan me-reset hitungan; rekap selalu menunjukkan 1 kendaraan.
- *"Kenapa `if` untuk gratis/diskon/denda tidak memakai `elif`?"* → karena syaratnya tidak saling meniadakan.
