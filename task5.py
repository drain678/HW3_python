# списочное выражение для создания списка чисел
spisok = [i for i in input().split()]
# словарь для того чтобы удобно было считать пары чисел, если они разные
slovar = {}
for i in spisok:
    # распределим числа по ключам в словаре, при этом значения ключей будут храниться в списках,
    # чтобы они всегда были отдельными элементами
    # если нет такого числа в словаре и в списке оно встречается больше 1 раза,
    # то нужно создать ключ с таким числом и такими же значениями в нем
    if spisok.count(i) > 1 and i not in slovar:
        slovar[i] = [i]
    # иначе прибавить еще одно такое же число к существующему ключу, к которому оно подходит
    elif spisok.count(i) > 1 and i in slovar:
        slovar[i] += [i]
# эта переменная будет суммой количества пар
res = 0
# теперь цикл сначала по ключам словаря
for n in slovar:
    # затем по длине списка под этим ключом начиная с 1
    for i in range(1, len(slovar[n])+1):
        # из длины списка нужно вычесть текущую итерацию. таким образом, будут посчитаны все пары
        res += len(slovar[n]) - i
print(res)
