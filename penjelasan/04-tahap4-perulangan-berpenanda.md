# 04 — Tahap 4: Perulangan Berpenanda (Sentinel)

**Baris di program:** 93–103 dan 241–245 · **Materi:** pekan 5 (`while` dengan masukan berpenanda)

## Masalahnya

Petugas tidak tahu berapa kendaraan yang akan keluar hari ini. Karena jumlahnya **tidak diketahui di awal**, kita tidak bisa memakai `for ... in range(n)`. Solusinya: petugas mengetik kata khusus **`SELESAI`** sebagai tanda berhenti. Kata khusus ini disebut **penanda** atau **sentinel**.

## Struktur yang dipakai (pola *priming read*)

```python
plat = input(TANYA_PLAT).strip().upper()        # (1) baca SEBELUM while
while plat == "":
    print("Plat nomor tidak boleh kosong.")
    plat = input(TANYA_PLAT).strip().upper()

while plat != PENANDA_SELESAI:                   # (2) kondisi = kapan berhenti
    ... Tahap 2: masukan & validasi ...
    ... Tahap 3: hitung & struk ...
    ... perbarui rekap ...

    plat = input(TANYA_PLAT).strip().upper()    # (3) baca lagi di AKHIR blok
    while plat == "":
        print("Plat nomor tidak boleh kosong.")
        plat = input(TANYA_PLAT).strip().upper()
```

**Kenapa harus begini:**

1. **Baca sebelum `while`** — agar kondisi `plat != "SELESAI"` punya nilai untuk diperiksa pertama kali. Bila petugas langsung mengetik `SELESAI`, badan perulangan **tidak dijalankan sama sekali** (data kosong).
2. **Kondisi `while` menjelaskan kapan berhenti** — siapa pun yang membaca baris itu langsung paham. Ini alasan soal melarang `while True` + `break`.
3. **Baca lagi di akhir blok** — inilah yang **mengubah variabel kondisi**. Tanpa baris ini, `plat` tidak pernah berubah, sehingga terjadi **perulangan tak berujung**.

### Kenapa `SELESAI` tidak ikut terhitung di rekap?

Karena `SELESAI` dibaca di akhir blok, lalu **langsung diperiksa oleh kondisi `while`** sebelum sempat diproses. Pencacah `jumlah_kendaraan = jumlah_kendaraan + 1` ada di dalam badan, jadi tidak pernah dijalankan untuk `SELESAI`.

Bandingkan dengan versi yang **salah**:

```python
plat = ""
while plat != "SELESAI":
    plat = input("Plat: ")
    jumlah_kendaraan = jumlah_kendaraan + 1   # SELESAI ikut terhitung! (galat logika)
    ...
```

Di versi salah ini, `SELESAI` sudah dihitung sebagai kendaraan dan program juga menanyakan jenisnya.

### `.strip().upper()`

Plat dinormalisasi ke huruf besar. Akibatnya:
- `selesai`, `Selesai`, `SELESAI` semuanya menghentikan program (lebih ramah petugas).
- Plat `l 1234 ab` tersimpan sebagai `L 1234 AB`, sehingga struk dan rekap seragam.

### Validasi plat kosong (fitur tambahan)

Soal membolehkan "teks apa saja", tetapi plat kosong jelas salah ketik (Enter tertekan). Pola validasinya sama dengan Tahap 2. Karena kita tidak boleh memakai `def`, blok 3 baris ini muncul dua kali (sebelum `while` dan di akhir blok). Teks pertanyaannya disimpan di konstanta `TANYA_PLAT` supaya tetap konsisten.

## Kenapa `while`, bukan `for`?

| | `for` + `range()` | `while` |
|---|---|---|
| Kapan dipakai | jumlah perulangan **diketahui** | berhenti karena **suatu kondisi** |
| Di ParkirKu | tabel tarif 8 baris, grafik `#` | sentinel `SELESAI`, validasi masukan |

## Kemungkinan pertanyaan dosen

- *"Apa yang terjadi jika baris baca plat di akhir blok dihapus?"* → plat tidak pernah berubah. Bila plat pertama bukan `SELESAI`, perulangan berjalan selamanya dan kendaraan yang sama diproses berulang kali.
- *"Kenapa tidak `while True` lalu `if plat == 'SELESAI': break`?"* → dilarang soal; selain itu kondisi berhentinya tersembunyi di tengah badan perulangan, sehingga lebih sulit dibaca dan dibuktikan pasti berhenti.
- *"Bagaimana kalau ada kendaraan yang platnya benar-benar `SELESAI`?"* → tidak mungkin; plat kendaraan Indonesia berformat huruf-angka-huruf. Bila perlu, penanda bisa diganti hanya dengan mengubah konstanta `PENANDA_SELESAI`.
