# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

n = int(input('Введите натуральное число: '))
tmp = ''
while n > 0:
    tmp += str(n % 10)
    n = n // 10
result = int(tmp)
print(result)
