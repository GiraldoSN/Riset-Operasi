import math


def hitung_probabilitas(lamda, miu, s, waktu):
    p = [1 / (lamda / miu)]  # P0
    for i in range(1, waktu + 1):
        if i <= s:
            p.append(((lamda / miu) ** i) * (1 / math.factorial(i)) * p[0])
        else:
            p.append(
                ((lamda / miu) ** s)
                * (1 / math.factorial(s))
                * ((lamda / miu) ** (i - s))
                * p[0]
            )
    return p


def hitung_metrics(probabilitas, lamda, miu, s):
    banyaknya_mesin_macet = sum((i * probabilitas[i]) for i in range(s + 1))
    banyak_antri = sum(
        ((i - s) * probabilitas[i]) for i in range(s + 1, len(probabilitas))
    )
    lama_antri = banyak_antri / lamda
    lama_macet = lama_antri + 1 / miu
    waktu_mesin_beroprasi = s - banyaknya_mesin_macet
    return (
        banyaknya_mesin_macet,
        banyak_antri,
        lama_antri,
        lama_macet,
        waktu_mesin_beroprasi,
    )


# Meminta input dari pengguna
lamda = float(input("Masukkan nilai lamda: "))
miu = float(input("Masukkan nilai miu: "))
s = int(input("Masukkan nilai s: "))
waktu = int(input("Masukkan jumlah waktu atau Probalitas: "))

# Hitung probabilitas
probabilitas = hitung_probabilitas(lamda, miu, s, waktu)

# Tampilkan hasil probabilitas
for i, p in enumerate(probabilitas):
    print(f"P{i} =", round(p, 4))

# Hitung dan tampilkan metrik
(
    banyaknya_mesin_macet,
    banyak_antri,
    lama_antri,
    lama_macet,
    waktu_mesin_beroprasi,
) = hitung_metrics(probabilitas, lamda, miu, s)
print("\nMetrics:")
print(f"Banyaknya mesin yang rusak = {round(banyaknya_mesin_macet, 2)}")
print(f"Banyaknya yang antri = {round(banyak_antri, 2)}")
print(f"Rata-rata lama antri = {round(lama_antri, 2)}")
print(f"Rata-rata lama macet = {round(lama_macet, 2)}")
print(f"Rata-rata waktu mesin beroperasi = {round(waktu_mesin_beroprasi, 2)}")
