# 00 — Baca Dulu: Peta Proyek ParkirKu

Folder ini berisi penjelasan **per proses (per tahap)** dari `parkir.py`, ditulis supaya kamu bisa menjelaskan setiap baris saat sesi audit. Baca berurutan.

| Berkas | Isi |
|---|---|
| `01-tahap1-konstanta-tabel.md` | Konstanta, tabel tarif dengan `for` + `range()` |
| `02-tahap2-masukan-validasi.md` | Validasi masukan dengan `while`, variabel penanda `sah`, `isdigit()` |
| `03-tahap3-hitung-biaya.md` | Durasi, jam ditagih, tarif dasar, diskon, denda, struk |
| `04-tahap4-perulangan-berpenanda.md` | Sentinel `SELESAI`, *priming read*, kenapa tanpa `while True`/`break` |
| `05-tahap5-rekap-akhir.md` | Pencacah, akumulator, penyaringan, nilai ekstrem, grafik |
| `06-persiapan-audit.md` | Daftar pertanyaan dosen + jawaban, latihan mencari galat sisipan |
| `data-uji/` | Berkas masukan siap pakai: contoh soal, penelusuran 5.1, data kosong, kasus batas, kasus seri |
| `latihan-galat/` | 6 salinan program yang masing-masing berisi satu galat, untuk latihan audit (+ kunci jawaban) |

## Struktur folder proyek

```
mini-project-parkir/
├── parkir.py              <- program (WAJIB dikumpulkan)
├── README-NIM.pdf         <- dokumentasi (WAJIB, ganti NIM di nama berkas)
├── flowchart.drawio       <- flowchart 6 halaman (buka di app.diagrams.net / draw.io desktop)
└── penjelasan/            <- folder ini, untuk belajar (TIDAK perlu dikumpulkan)
```

## Cara menjalankan

- **Thonny / VS Code**: buka `parkir.py`, tekan Run (F5), ketik masukan satu per satu.
- **Uji cepat dengan berkas** (dari folder proyek):
  - Command Prompt: `python parkir.py < penjelasan\data-uji\uji_contoh.txt`
  - PowerShell: `Get-Content penjelasan\data-uji\uji_contoh.txt | python parkir.py`

  Hasil yang benar: total Rp 30400, rata-rata Rp 6080, terlama S 9012 EF, tertinggi L 3456 GH.

## Cara membuka flowchart

Buka <https://app.diagrams.net>, pilih *Open Existing Diagram*, lalu pilih `flowchart.drawio`. Ada 6 tab halaman di bawah: Program Utama, Tahap 1–5. Semua kotak dan panah bisa digeser dan diedit.

## Yang WAJIB kamu lakukan sebelum mengumpulkan

1. **Isi identitas** di README (nama, NIM, kelas, dosen). Kirim datanya ke Claude untuk dibuatkan ulang PDF-nya, lalu ganti nama berkas menjadi `README-<NIM>.pdf`.
2. **Tulis ulang bagian Refleksi dengan kata-katamu sendiri.** Isinya harus jujur tentang pengalamanmu.
3. **Periksa bagian Pengungkapan AI.** Sudah ditulis bahwa kamu memakai Claude. Sesuaikan bila ada yang kamu ubah sendiri. Menyembunyikan penggunaan AI = nilai 0.
4. **Pelajari semua berkas di folder ini** dan coba jawab pertanyaan di `06-persiapan-audit.md` tanpa melihat jawaban. Kode yang tidak bisa kamu jelaskan = nilai 0.
5. Jalankan `parkir.py` sekali di Thonny/VS Code kamu sendiri dengan data uji soal.
6. Buat folder `NIM_NamaLengkap/` berisi **hanya** `parkir.py` dan `README-NIM.pdf`, kompres jadi `NIM_NamaLengkap.zip`, unggah ke CeLOE.

## Gambaran alur besar

```
Mulai
 └─ Tahap 1: konstanta + cetak tabel tarif
 └─ siapkan variabel rekap (0 dan -1)
 └─ baca plat ──────────────────────────────┐
     while plat != "SELESAI":               │  Tahap 4 (sentinel)
        Tahap 2: baca & validasi masukan    │
        Tahap 3: hitung biaya & cetak struk │
        perbarui variabel rekap             │
        baca plat berikutnya ───────────────┘
 └─ Tahap 5: rekap akhir (atau "Belum ada kendaraan")
Selesai
```

Catatan nomor baris: nomor baris yang disebut di folder ini dan di README merujuk ke `parkir.py` versi asli (284 baris). Bila kamu menambah atau menghapus baris, nomornya ikut bergeser.
