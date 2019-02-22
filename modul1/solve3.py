import math
jumlah = 485; 
tahun = 365;
bulan = 30;
minggu = 7;

hitung_tahun = math.floor(jumlah/tahun)
hitung_bulan = math.floor(jumlah/bulan)
hitung_minggu = math.floor(jumlah/minggu)
hitung_hari = math.floor(hitung_minggu/minggu)

print(str(hitung_tahun) + ' ' + 'tahun')
print(str(hitung_bulan) + ' ' + 'bulan')
print(str(hitung_minggu) + ' ' + 'minggu')
print(str(hitung_hari) +  ' ' + 'hari')