# 03 — Tahap 3: Hitung Biaya & Struk

**Baris di program:** 167–216 · **Materi:** pekan 2 (operator `//`, `%`, urutan operasi), pekan 3 (`if/elif/else`), pekan 4 (`and`/`not`, kondisi batas)

Flowchart lengkapnya ada di halaman **"Tahap 3 - Hitung Biaya"** pada `flowchart.drawio` dan di README bagian 4.

## Langkah 1 — Durasi dan jam ditagih

```python
durasi = total_menit_keluar - total_menit_masuk
jam_tagih = (durasi + MENIT_PER_JAM - 1) // MENIT_PER_JAM   # = (durasi + 59) // 60
```

- `//` adalah **pembagian bulat ke bawah** (`200 // 60 = 3`).
- Kita butuh **bulat ke atas**: 3 jam 20 menit harus ditagih 4 jam. Triknya: tambahkan 59 dulu.

| durasi | durasi + 59 | // 60 | Keterangan |
|---:|---:|---:|---|
| 0 | 59 | **0** | tidak ada jam yang ditagih |
| 15 | 74 | **1** | |
| 60 | 119 | **1** | tepat 1 jam, tidak dibulatkan |
| 61 | 120 | **2** | lewat 1 menit → 2 jam |
| 200 | 259 | **4** | 3 jam 20 menit → 4 jam |

Kenapa 59, bukan 60? Bila +60, durasi 60 menit menjadi `120 // 60 = 2` (salah, harusnya 1).

## Langkah 2 — Pilih tarif sesuai jenis

```python
if jenis == JENIS_MOTOR:
    tarif_pertama = TARIF_MOTOR_PERTAMA
    tarif_berikutnya = TARIF_MOTOR_BERIKUTNYA
    tarif_maks = TARIF_MOTOR_MAKS
else:
    tarif_pertama = TARIF_MOBIL_PERTAMA
    ...
```

Cukup `if/else` karena Tahap 2 sudah menjamin jenis hanya `motor` atau `mobil`. Variabel umum (`tarif_pertama`, dst.) membuat rumus di bawahnya **ditulis sekali** untuk kedua jenis.

## Langkah 3 — Tarif dasar

```python
if durasi <= BATAS_GRATIS_MENIT:
    tarif_dasar = 0
else:
    tarif_dasar = tarif_pertama + (jam_tagih - 1) * tarif_berikutnya
    if tarif_dasar > tarif_maks:
        tarif_dasar = tarif_maks
```

- **Gratis** diperiksa lebih dulu dengan `<=`: tepat 15 menit **masih gratis**, 16 menit sudah bayar.
- Urutan operasi: `(jam_tagih - 1)` dihitung dulu karena kurung, lalu `*`, lalu `+`.
- Potong ke maksimum dengan `>`: tarif yang **tepat sama** dengan maksimum tidak berubah.
- Pada cabang `else` dijamin `durasi >= 16`, sehingga `jam_tagih >= 1` dan `(jam_tagih - 1)` tidak pernah negatif.

## Langkah 4 — Diskon (kondisi majemuk)

```python
if punya_kartu and not tiket_hilang and tarif_dasar > 0:
    diskon = tarif_dasar * PERSEN_DISKON // PERSEN_PENUH
else:
    diskon = 0
```

Tiga syarat **harus benar semua**, maka dipakai `and`:

| Syarat | Contoh yang gagal |
|---|---|
| `punya_kartu` | W 5678 CD tidak punya kartu |
| `not tiket_hilang` | L 3456 GH punya kartu, tetapi tiket hilang → **tanpa diskon** |
| `tarif_dasar > 0` | gratis → tidak ada yang bisa didiskon |

`tarif_dasar * 20 // 100` → kalikan dulu, baru bagi bulat (operator `*` dan `//` setara, dikerjakan dari kiri). Untuk 5000: `5000 * 20 = 100000`, `// 100 = 1000`.

**Kenapa tidak `tarif_dasar * 0.2`?** Hasilnya `float` (mis. `1000.0`) dan bisa memunculkan angka seperti `1599.9999`. Soal meminta `* 20 // 100` agar tetap bilangan bulat.

## Langkah 5 — Denda dan total

```python
if tiket_hilang:
    denda = DENDA_TIKET_HILANG
else:
    denda = 0

total = tarif_dasar - diskon + denda
```

- Denda **dicek terpisah** dari gratis, sehingga tetap dikenakan walau durasinya gratis (contoh: 0 menit + tiket hilang = Rp 10000).
- Denda ditambahkan **setelah** diskon; diskon tidak pernah memotong denda.

## Langkah 6 — Struk

```python
print(f"Durasi      : {durasi // MENIT_PER_JAM} jam {durasi % MENIT_PER_JAM} menit")
```

`//` memberi jam penuh, `%` (modulo, sisa bagi) memberi sisa menit. 200 menit → `200 // 60 = 3` jam, `200 % 60 = 20` menit.

## Tabel uji tahap ini (sesuai data soal 3.7)

| Plat | durasi | jam | tarif dasar | diskon | denda | total |
|---|---:|---:|---:|---:|---:|---:|
| L 1234 AB | 200 | 4 | 5000 | 1000 | 0 | **4000** |
| W 5678 CD | 15 | 1 | 0 | 0 | 0 | **0** |
| S 9012 EF | 735 | 13 | 14000 → **8000** | 1600 | 0 | **6400** |
| L 3456 GH | 16 | 1 | 2000 | 0 | 10000 | **12000** |
| N 7788 IJ | 130 | 3 | 8000 | 0 | 0 | **8000** |

## Kemungkinan pertanyaan dosen

- *"Kenapa gratis dicek sebelum rumus?"* → durasi 0 menghasilkan `jam_tagih = 0`, sehingga rumus memberi `2000 + (0-1)*1000 = 1000` (salah). Pemeriksaan gratis lebih dulu mencegah hal ini.
- *"Kalau baris `and tarif_dasar > 0` dihapus, apa bedanya?"* → hasilnya tetap sama (20% dari 0 = 0), tetapi pencacah `jumlah_diskon` tidak terpengaruh karena pencacah memeriksa `diskon > 0`. Syarat ini tetap ditulis karena diminta soal dan membuat maksudnya jelas.
- *"Ubah `<=` menjadi `<` pada batas gratis, apa yang terjadi?"* → W 5678 CD (tepat 15 menit) jadi membayar Rp 4000. Ini galat logika klasik di kasus batas.
