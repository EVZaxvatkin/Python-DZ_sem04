#1. Напишите функцию для транспонирования матрицы

def transporation(table):
    table2 = []

    for i in range(len(table[0])):
        table2.append(list())
        for j in range(len(table)):
            table2[i].append(table[j][i])
    return table2

matrix = [[7, 6, 5], [9, 8, 1]]
print(matrix)
matrix2 = transporation(matrix)
print(matrix2)

#2.Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
#где ключ - значение переданного аргумента, а значение - имя аргумента.
#Если ключ не хешируем, используйте его строковое представление.

def dictunary(a=4, b=6):
    dictun = {
        f'{a}': id(a),
        f'{b}': id(b)
    }

    return dictun
a = 4
b = 6
temp = dictunary(a, b)
print(temp)