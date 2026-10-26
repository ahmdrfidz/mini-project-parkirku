# 01 — Tahap 1: Konstanta & Tabel Tarif

**Baris di program:** 14–70 · **Materi:** pekan 2 (variabel, tipe data, operator), pekan 6 (`for`, `range()`)

## Tujuan

1. Menyimpan **semua angka aturan** di satu tempat, di bagian atas program.
2. Mencetak tabel tarif 1–8 jam untuk motor dan mobil, yang **sudah memperhitungkan batas maksimum**.

## Bagian A — Konstanta (baris 21–53)

```python
TARIF_MOTOR_PERTAMA = 2000
TARIF_MOTOR_BERIKUTNYA = 1000
TARIF_MOTOR_MAKS = 8000
...
BATAS_GRATIS_MENIT = 15
PERSEN_DISKON = 20
PERSEN_PENUH = 100
DENDA_TIKET_HILANG = 10000
...
MENIT_PER_JAM = 60
PENANDA_SELESAI = "SELESAI"
```

**Penjelasan:**

- Python tidak punya "konstanta sungguhan". **Konvensinya**: variabel yang ditulis HURUF KAPITAL tidak boleh diubah nilainya setelah dibuat. Ini kesepakatan antarprogrammer.
- Alasan memakai konstanta (soal mewajibkan ini):
  - **Mudah diubah.** Bila tarif motor naik menjadi Rp 3000, cukup ubah satu baris. Tabel Tahap 1 dan perhitungan Tahap 3 ikut berubah otomatis.
  - **Mudah dibaca.** `tarif_dasar * PERSEN_DISKON // PERSEN_PENUH` lebih jelas daripada `tarif_dasar * 20 // 100`.
  - **Mencegah salah ketik.** Angka ajaib yang ditulis berulang rawan beda satu sama lain.
- Tipe data: semua tarif bertipe `int` (bilangan bulat) karena rupiah tidak memakai pecahan. `PENANDA_SELESAI`, `JENIS_MOTOR`, dll bertipe `str`.
- Konstanta `JAM_TERKECIL`, `JAM_TERBESAR`, `MENIT_TERBESAR`, `MENIT_PER_JAM` juga dibuat, sehingga bahkan teks pertanyaan `"Jam masuk (0-23)"` dibentuk dari konstanta.
- `TANYA_PLAT` menyimpan teks pertanyaan plat karena pertanyaan itu dipakai di 4 tempat.

## Bagian B — Tabel tarif dengan `for` (baris 61–69)

```python
for jam in range(JAM_TABEL_AWAL, JAM_TABEL_AKHIR + 1):
    tarif_motor = TARIF_MOTOR_PERTAMA + (jam - 1) * TARIF_MOTOR_BERIKUTNYA
    if tarif_motor > TARIF_MOTOR_MAKS:
        tarif_motor = TARIF_MOTOR_MAKS
    tarif_mobil = TARIF_MOBIL_PERTAMA + (jam - 1) * TARIF_MOBIL_BERIKUTNYA
    if tarif_mobil > TARIF_MOBIL_MAKS:
        tarif_mobil = TARIF_MOBIL_MAKS
    print(f"| {jam:>3} | Rp {tarif_motor:>7} | Rp {tarif_mobil:>7} |")
```

**Penjelasan baris demi baris:**

| Baris | Maksud |
|---|---|
| `range(1, 8 + 1)` | Menghasilkan 1, 2, ..., 8. Batas akhir `range` **tidak ikut**, maka ditulis `+ 1`. |
| `TARIF_PERTAMA + (jam - 1) * TARIF_BERIKUTNYA` | Jam pertama dihitung sekali; sisanya `(jam - 1)` jam dikali tarif per jam berikutnya. |
| `if tarif > MAKS: tarif = MAKS` | Pola **penjaga batas atas** (*capping*). Tarif tidak boleh melebihi maksimum per hari. |
| `f"{jam:>3}"` | f-string; `:>3` artinya rata kanan dengan lebar 3 karakter, agar kolom tabel lurus. |

**Kenapa `for`, bukan `while`?** Jumlah perulangan **sudah diketahui** sejak awal (tepat 8 kali). `for` + `range()` adalah pilihan yang tepat untuk perulangan terhitung. `while` dipakai bila jumlahnya belum diketahui (Tahap 2 dan 4).

## Hasil yang benar

| Jam | Motor | Mobil |
|---:|---:|---:|
| 1 | 2000 | 4000 |
| 2 | 3000 | 6000 |
| 3 | 4000 | 8000 |
| 4 | 5000 | 10000 |
| 5 | 6000 | 12000 |
| 6 | 7000 | 14000 |
| 7 | 8000 | 16000 |
| 8 | **8000** (rumus 9000, dipotong) | **16000** (rumus 18000, dipotong) |

Perhatikan jam 7: tarif **tepat sama** dengan maksimum, dan tidak terpotong karena kondisinya `>` bukan `>=`. Hasilnya sama saja di sini, tetapi kamu harus bisa menjelaskan alasannya.

## Kenapa rumusnya harus sama dengan Tahap 3?

Soal mensyaratkan ini. Tabel adalah "janji" kepada pengguna. Bila rumus tabel berbeda dari rumus penagihan, tabel bisa menunjukkan Rp 8000 padahal struk menagih Rp 9000. Karena kita belum boleh memakai `def` (fungsi), rumus ditulis dua kali dengan **bentuk yang persis sama**: hitung dulu, lalu potong ke maksimum.

## Kemungkinan pertanyaan dosen

- *"Kenapa `JAM_TABEL_AKHIR + 1`?"* → karena `range(a, b)` berhenti sebelum `b`.
- *"Apa jadinya kalau baris `if tarif_motor > TARIF_MOTOR_MAKS` dihapus?"* → jam 8 motor menjadi Rp 9000; tabel salah.
- *"Kalau tarif mobil berikutnya naik jadi 2500, apa yang kamu ubah?"* → cukup baris `TARIF_MOBIL_BERIKUTNYA = 2500`.
