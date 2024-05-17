array = input('Введите целые числа через пробел: ').strip().split()
array_result = []
for num in array:
    num = int(num)
    if num % 3 == 0 and num != 0:
        array_result.append(num)
print('Ваш массив:\n', array)
print('\nЧисла, которые делятся на 3:\n', array_result)
