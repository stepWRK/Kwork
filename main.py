import random

# задача C (сложное)
#


print("""

задание Ⅰ (1)
треугольник △
———————————————————————————————————————————————————————————————————————————————————————————————————————————————""")
print("введите размер треугольника")
SizTriangle = int(input())                   #triangle - треугольник, гений

for i in range(SizTriangle):
    if i == 0:
        print(" " * (SizTriangle - 1) + "*")
    elif i == SizTriangle - 1:               #заполнение низней части треугольника
        print("*" * (2 * SizTriangle -1))
    else:
        SpaceBef = SizTriangle - i - 1
        SpaceBetw = 2 * i - 1
        print(" " * SpaceBef + "*" + " " * SpaceBetw + "*")
print("""


задача Ⅱ (2)
поля случайных чисел
———————————————————————————————————————————————————————————————————————————————————————————————————————————————""")
print("""
введите число для проверки""")
num = int(input())
Anum = 10
Bnum = 50
if Anum <= num <=Bnum:
    print("число принадлежит промежутку")
else:
    print("число не принадлежит промежутку")

print("""

задача Ⅲ (3)
поля случайных чисел
———————————————————————————————————————————————————————————————————————————————————————————————————————————————""")
SizInp = int(input())
SideX = SizInp
UpX = SizInp
Matrix = []

print("исходная матрица")
for i in range(SideX):
    UpGlob = [random.randint(1, 99) for _ in range(SideX)]
    Matrix.append(UpGlob)
    print(" ".join(f"{num:2}" for num in UpGlob))

while True:
    print("Команды: влево (1) и выход (2)")
    Command = input("""
Введите команду:""").lower()

    if Command == "2":
        print("Goodbye world! *deleting folder system_32*")
        break
    elif Command == "1":
        shifted_matrix = []
        for row in Matrix:
            shifted_row = row[1:] + [row[0]]
            shifted_matrix.append(shifted_row)
        Matrix = shifted_matrix
    else:
        print("поздравляю, ваш средний IQ чуть больше чем у Чихуахуа")
        continue
    for row in Matrix:
        print(" ".join(f"{num:2}" for num in row))