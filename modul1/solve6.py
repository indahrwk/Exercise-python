import math

jamawal = 9;
jarak = 120;
kecepatantotal = 100/3600;
detiktotal = jarak/kecepatantotal;

lamajam = math.floor(detiktotal/3600);
lamamenit = math.floor((detiktotal%3600)/60);
lamajam = math.floor((detiktotal%3600)%60);

print('lama jam = '  + str(lamajam) + ' ' + 'lama menit = ' + str(lamamenit))
print('tabraknya pukul = ' + str(jamawal + lamajam) + ' dan menit ke ' + str(lamamenit))