# 02 — Tahap 2: Masukan & Validasi

**Baris di program:** 105–165 · **Materi:** pekan 2 (`input()`, konversi `int()`), pekan 3 (`if/elif/else`, plan penjaga), pekan 4 (`and`, `or`, `not`), pekan 5 (`while` validasi)

## Prinsip: "jangan percaya masukan"

Pesan Kak Dito: petugas sering salah ketik. Setiap pertanyaan **diulang dengan `while` sampai jawabannya valid**. Program tidak boleh lanjut menghitung dengan data yang salah.

Ada dua pola validasi yang dipakai.

---

## Pola 1 — Baca, lalu ulang selama tidak valid (jenis, kartu, tiket)

```python
jenis = input("Jenis kendaraan (motor/mobil): ").strip().lower()
while jenis != JENIS_MOTOR and jenis != JENIS_MOBIL:
    print("Jenis harus motor atau mobil.")
    jenis = input("Jenis kendaraan (motor/mobil): ").strip().lower()
```

**Penjelasan:**

1. Baca sekali **sebelum** `while`.
2. Kondisi `while` = "masukan **tidak** valid". Selama tidak valid: cetak pesan, baca ulang.
3. Begitu valid, kondisi bernilai `False` dan perulangan berhenti dengan sendirinya.

**`.strip().lower()`**: `.strip()` membuang spasi di depan/belakang, `.lower()` mengubah ke huruf kecil. Jadi `" MOTOR "` diterima sebagai `"motor"`.

### Kenapa `and`, bukan `or`? (pertanyaan favorit dosen)

Kita ingin mengulang bila jenis **bukan motor DAN bukan mobil**.

| jenis | `!= "motor"` | `!= "mobil"` | `and` (benar) | `or` (SALAH) |
|---|---|---|---|---|
| `"motor"` | False | True | **False → berhenti** ✓ | True → ulang terus ✗ |
| `"mobil"` | True | False | **False → berhenti** ✓ | True → ulang terus ✗ |
| `"sepeda"` | True | True | **True → ulang** ✓ | True → ulang ✓ |

Dengan `or`, kondisinya **selalu** True, sehingga terjadi **perulangan tak berujung**. Ini juga hukum De Morgan: `not (a == x or a == y)` sama dengan `a != x and a != y`.

### Mengubah jawaban ya/tidak menjadi boolean

```python
punya_kartu = jawab_kartu == JAWAB_YA
```

Ekspresi `jawab_kartu == "ya"` menghasilkan `True` atau `False`, lalu disimpan. Selanjutnya cukup menulis `if punya_kartu` (tidak perlu `if punya_kartu == True`).

---

## Pola 2 — Variabel penanda `sah` (waktu masuk & keluar)

Waktu terdiri dari **dua masukan** (jam dan menit) yang diperiksa bersama, dengan **beberapa pemeriksaan** dan pesan berbeda. Soal menyarankan variabel penanda.

```python
waktu_masuk_sah = False
while not waktu_masuk_sah:
    jam_masuk_teks = input(f"Jam masuk ({JAM_TERKECIL}-{JAM_TERBESAR}): ").strip()
    menit_masuk_teks = input(f"Menit masuk ({MENIT_TERKECIL}-{MENIT_TERBESAR}): ").strip()
    if not (jam_masuk_teks.isdigit() and menit_masuk_teks.isdigit()):
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
```

**Penjelasan:**

| Bagian | Maksud |
|---|---|
| `waktu_masuk_sah = False` | Anggap belum sah, supaya `while` pasti dijalankan minimal sekali. |
| `while not waktu_masuk_sah` | Ulangi selama belum sah. **Variabel kondisi berubah di dalam blok** (`= True`), jadi perulangan pasti berhenti begitu masukan benar. |
| `.isdigit()` | `True` bila teks hanya berisi angka 0–9. `"8a"`, `"abc"`, `""`, `"-1"` menghasilkan `False`. |
| `if not (... and ...)` | Bila salah satu bukan angka, tolak. `int()` **tidak pernah** dipanggil pada teks yang bukan angka, sehingga tidak ada `ValueError`. |
| Kondisi rentang dengan `or` | Waktu **tidak valid** bila **salah satu saja** keluar rentang, sehingga dipakai `or`. |
| Tanda kurung `( ... )` | Agar kondisi panjang boleh dipecah ke dua baris. |

**Soal bilang "asumsikan pengguna selalu mengetik angka"**, jadi `isdigit()` adalah **fitur tambahan** untuk kasus tidak lazim (rubrik skor 4: "termasuk kasus tidak lazim"). Kita tidak boleh memakai `try/except`, sehingga dipakai pemeriksaan sebelum konversi. Ini disebut pola **penjaga** (*guard*).

### Kenapa waktu diubah menjadi total menit?

```python
total_menit_masuk = jam_masuk * 60 + menit_masuk     # 08:00 -> 480
```

Membandingkan dua waktu jadi cukup satu perbandingan angka. Tanpa ini, kamu harus menulis kondisi rumit seperti `jam_keluar < jam_masuk or (jam_keluar == jam_masuk and menit_keluar < menit_masuk)`. Kasus 10:30 → 10:29 (jam sama, menit lebih kecil) otomatis tertangkap: 629 < 630.

### Waktu keluar: tiga pemeriksaan dengan `if / elif / else`

```python
if (jam/menit di luar rentang):
    print("Waktu tidak valid.")
elif total_menit_keluar < total_menit_masuk:
    print("Waktu keluar tidak boleh sebelum waktu masuk.")
else:
    waktu_keluar_sah = True
```

- `elif` hanya diperiksa bila rentangnya sudah benar. Urutan ini penting agar pesan yang muncul tepat.
- Memakai `<` (bukan `<=`) sehingga **waktu keluar = waktu masuk tetap sah** (durasi 0 menit). Soal menyebut durasi 0 menit sebagai kasus batas yang harus benar.
- Bila keluar lebih awal, **hanya jam & menit keluar** yang ditanya ulang (sesuai tabel soal), karena loop waktu masuk sudah selesai.

## Kasus uji untuk tahap ini

| Masukan | Hasil |
|---|---|
| jenis `sepeda` | "Jenis harus motor atau mobil." lalu ditanya ulang |
| jenis `MOTOR` | diterima sebagai `motor` |
| jam 25, menit 0 | "Waktu tidak valid." lalu jam **dan** menit ditanya ulang |
| jam `abc` | "Jam dan menit harus berupa angka bulat." (tidak galat) |
| jam `-1` | ditolak (`"-1".isdigit()` = False) |
| menit 60 | "Waktu tidak valid." |
| masuk 08:00, keluar 07:00 | "Waktu keluar tidak boleh sebelum waktu masuk." |
| masuk 23:59, keluar 23:59 | sah, durasi 0 |
| kartu `mungkin` | "Jawaban harus ya atau tidak." |

## Kemungkinan pertanyaan dosen

- *"Bisakah validasi waktu ditulis tanpa variabel `sah`?"* → bisa, tetapi kondisi `while` jadi sangat panjang, dan pesan galat yang berbeda-beda sulit dibuat. Variabel penanda membuat tiap pemeriksaan punya pesannya sendiri.
- *"Apakah `while` ini pasti berhenti?"* → ya. Satu-satunya cara keluar adalah `waktu_masuk_sah = True`, dan baris itu tercapai begitu pengguna mengetik waktu yang benar. Kalau pengguna terus salah, program memang terus bertanya; itu perilaku yang diinginkan, bukan perulangan tak berujung karena galat.
- *"Kenapa variabel `jam_masuk` bisa dipakai di luar `while`?"* → di Python, variabel yang dibuat di dalam `while`/`if` tetap ada setelah bloknya selesai. Dan `jam_masuk` pasti sudah terisi karena loop hanya berhenti setelah melewati cabang yang mengisinya.
