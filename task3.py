# с помощью списочного выражения создадим список из введенных значений
sp = [int(i) for i in input().split()]
sp.insert(0, sp.pop()) # с помощью метода insert вставляем на 0 индекс значение аргумента sp.pop() (pop без параметра будет удалять последний элемент),
# который одновеменно удалится со своего изначального места
print(sp)