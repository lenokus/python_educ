# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

n = input('Please, enter any number = ')

print('n + nn + nnn = ', int(str(n))+int(str(n*2))+int(str(n*3)))