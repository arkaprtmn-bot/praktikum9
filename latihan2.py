nilai = [80, 90, 'A', 70, 100, 'B']

total = 0
jumlah_data = 0

for n in nilai:
    try:
        total += n      # akan error jika n bukan angka
        jumlah_data += 1
    except TypeError:
        # melewati data yang bukan angka
        continue

if jumlah_data > 0:
    rata_rata = total / jumlah_data
    print(f"Rata-rata nilai valid: {rata_rata}")
else:
    print("Tidak ada data nilai yang valid.")
