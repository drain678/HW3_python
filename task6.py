def issymmetric(n, spisok):
    for i in range(n):
        for j in range(n):
            # слева от неравно: перебор сначала по строкам, затем по столбцам
            # справа от неравно: перебор сначала по столбцам, затем по строкам
            # и если значения получаются разные, то возвращается "NO",
            # а если каждый цикл прошел - "YES"
            if spisok[i][j] != spisok[j][i]:
                return "NO"
    return "YES"


# ввод значений
n = int(input())
# списочное выражение
spisok = [[int(i) for i in input().split()] for i in range(n)]
print(issymmetric(n, spisok))

