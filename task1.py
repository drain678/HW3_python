# создаем функцию
def can_eat(horse, figure):
    # присвоим переменным координаты из кортежей
    rowH, colH = horse
    rowF, colF = figure
    # сравниваем координаты фигур и проверяем может ли конь съесть её
    # первое условие для вертикальной буквы г
    if abs(colH - colF) == 1 and abs(rowH - rowF) == 2:
        # если координаты подходят, то возвращаем True
        return True
    # второе условие для горизонтальной буквы г
    if abs(rowH - rowF) == 1 and abs(colH - colF) == 2:
        return True
    # иначе возвращаем False
    return False


result = can_eat(input(), input())
print(result)
