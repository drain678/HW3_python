# ввод строки
n = input()
# проверка на наличе буквы в строке
if 'f' in n:
    # если первый индекс вхождения равен последнему, то это значит что буква одна
    # и можно вывести любой из этих двух индексов
    if n.find('f') == n.rfind('f'):
        print(n.find('f'))
    # иначе букв уже несколько и выведется начальный и конечный индекс
    else:
        print(n.find('f'), n.rfind('f'))

