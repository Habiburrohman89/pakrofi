print('\t \t \t PROGRAM DAFTAR NAMA\n')
print('########################################################################')
print('\t \t \tPILIH NAMA DI BAWAH INI\n')
print('########################################################################')
Daftar = ['\t•Ulfa','\t•Anis','\t•Dewi','\t•Ayu','\t•Rahma','\t•Reni'
]
#perulangan for
for i in Daftar:
	print(i)



#logika if ,elif,else
nama = input('masukan nama yang kamu sukai :')


if nama == 'ulfa':
        print('cantik,imut,baik')
elif nama == 'anis':
        print('manyun,baik')
elif nama == 'dewi':
        print('cantik, kalem')
elif nama == 'ayu':
        print('tinggi,manis')
elif nama == 'rahma':
	    print('bulet,hitam manis')
elif nama == 'reni':
        print('tinggi,baik')
else :
	print('maaf nama tidak termasuk kategori ')