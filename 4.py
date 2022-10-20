# Разбор домашки
Из десятичной в двоичную
a = 14
st = ''
while a > 0:
    ost = a % 2
    st = str(ost) + st
    a = a // 2
print(st)    
