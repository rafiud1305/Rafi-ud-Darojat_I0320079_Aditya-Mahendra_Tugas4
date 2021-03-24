print ("=============================================")
print ("Soal 6 Tugas 4")
print ("=============================================")

a = 4
b = 11

c = a | b
print('\n=========OR===========')
print('nilai :',a,' , binary : ',format(a,'08b'))
print('nilai :',b,' , binary : ',format(b,'08b'))
print('---------------------------------(|)')
print('nilai :',c,' , binary : ',format(c,'08b'))

c = a >> b
print('\n=========>>===========')
print('nilai :',a,' , binary : ',format(a,'08b'))
print('nilai :',b,' , binary : ',format(b,'08b'))
print('---------------------------------(>>)')
print('nilai :',c,' , binary : ',format(c,'08b'))

c = a ^ b
print('\n=========XOR===========')
print('nilai :',a,' , binary : ',format(a,'08b'))
print('nilai :',b,' , binary : ',format(b,'08b'))
print('---------------------------------(^)')
print('nilai :',c,' , binary : ',format(c,'08b'))

c = ~a
print('\n=========NOT===========')
print('nilai :',a,' , binary : ',format(a,'08b'))
print('---------------------------------(~)')
print('nilai :',c,' , binary : ',format(c,'08b'))

c = b & a
print('\n=========AND===========')
print('nilai :',b,' , binary : ',format(b,'08b'))
print('nilai :',a,' , binary : ',format(a,'08b'))
print('---------------------------------(&)')
print('nilai :',c,' , binary : ',format(c,'08b'))


