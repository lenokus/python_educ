# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

x = input('Please, enter time (sec): ')

h = int(x)//3600
m = int(x) // 60 % 60
s = int(x) % 60

if h < 10:
    h = '0' + str(h)

if m < 10:
    m = '0' + str(m)

if s < 10:
    s = '0' + str(s)

result = str(h) + ':' + str(m) + ':' + str(s)
print('hh:mm:cc => ', result)