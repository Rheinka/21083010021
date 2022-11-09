from os import getpid, system
from time import time, sleep
from multiprocessing import cpu_count, Pool, Process

def cetak(i):
    if i%2 == 0:
       print(i+1, "Ganjil - ID proses", getpid())
    else:
       print(i+1, "Genap - ID proses", getpid())
    sleep(1)

banyak =int(input("Input :"))

print("\nSekuensial")
sekuensial_awal = time()

for i in range(banyak):
    cetak(i)

sekuensial_akhir = time()

print("\nmultiprocessing.Process")
kumpulan_proses = []

process_awal = time()

for i in range(banyak):
    p = Process(target=cetak, args=(i,))
    kumpulan_proses.append(p)
    p.start()

for i in kumpulan_proses:
    p.join()

process_akhir = time()

print("\nmultiprocessing.Pool")

pool_awal = time()

pool = Pool()
pool.map(cetak, range(0, banyak))
pool.close()

pool_akhir = time()

print("\nWaktu Eksekusi Sekuensial: ", sekuensial_akhir - sekuensial_awal, "detik")
print("Waktu Eksekusi Multiprocessing.Process: ", process_akhir - process_awal, "detik")
print("Waktu Eksekusi Multiprocessing.Pool: ", pool_akhir - pool_awal, "detik")
