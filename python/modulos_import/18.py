import math
ang = int(input('angulo? '))
ang = (ang*math.pi)/180
print('seno: {:.2f}\ncosseno: {:.2f}\ntangente: {:.2f}'.format(math.sin(ang),math.cos(ang),math.tan(ang)))
