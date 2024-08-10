print()
print('Latihan Komparasi')
print('-'*50)
#membuat gabungan area rentang dari angka 
#++++++3---------10++++++++

inputuser = float(input('masukan angka yang bernilai\nkurang dari 3 atau(or)\nlebih dari 10\n:'))

#++++3------
#mamariksa angka kurang dai 3
iskurangdari = (inputuser < 3)
print('kurang dari 3 = ',iskurangdari)#output boolean

#----10++++++++++
#mamariksa angka kurang dai 3
islebihdari = (inputuser > 10)
print('lebih dari 10 = ',islebihdari)#output boolean

#++++++3---------10++++++++
iscorrect = iskurangdari or islebihdari
print('angka yang anda masukkan: ',iscorrect)


print()
#----3++++++10-------
#kasus irisan (antara angka 3 sampe 10, jadi pakai and)
inputuser = float(input('masukan angka yang bernilai\nlebih dari 3 dan(and)\nkurang dari 10\n:'))

#-----3++++++++++
#lebih dari 3
islebihdari = (inputuser > 3)
print('lebih dari 3 = ',islebihdari)
#+++++10---------
#kurang dari 10
iskurangdari = (inputuser < 10)
print('kurang dari 10 = ',iskurangdari)

#------3++++++10------
iscorrect = islebihdari and iskurangdari
print('angka yang anda masukkan: ',iscorrect)
