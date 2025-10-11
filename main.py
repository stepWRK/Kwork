#1ое задание
n = int(input())
for i in range(n):
    Sk = []
    for j in range(n):
        if i + j == n - 1:
            Sk.append(1)
        elif i + j > n - 1:
            Sk.append(2)
        else:
            Sk.append(0)
    print(" ".join(map(str, Sk)))

#2ое задание
X = int(input())
Mat = [[abs(i - j) for j in range(X)] for i in range(X)]
for row in Mat:
    print(" ".join(map(str, row)))

#3е задание
print("пиши: X N <-- через пробел 2 цфр")
x, m = map(int, input().split())
Board = [["." if (x + j) % 2 == 0 else "*" for j in range(m)] for x in range(x)]
for row in Board:
    print(" ".join(row))

#4ое задание
A = int(input())
arr = [["." for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j or i + j == A - 1 or i == A // 2 or j == A // 2:
            arr[i][j] = "*"
for row in arr:
    print(" ".join(row))
#5 задание не по силам

#6 ультре сложное делюкс задание
def print_triangle(siz, chavo):
    """треугольник печать"""
    for i in range(1, siz + 1):
        print(" " * (siz - i) + chavo * (2 * i - 1))
def print_square(siz, chavo):
    """квадрат печать"""
    for i in range(siz):
        print(chavo * siz)
def print_rhombus(siz, chavo):
    """Написание тяжолай хрень кт вы написать"""
    for i in range(1, siz + 1):
        print(" " * (siz - i) + chavo * (2 * i - 1))
    for i in range(siz - 1, 0, -1):
        print(" " * (siz - i) + chavo * (2 * i - 1))
def print_star(siz, chavo):
    """печать зевёздочка"""
    idk = [[" " for _ in range(siz)] for _ in range(siz)]
    for i in range(siz):
        for j in range(siz):
            if i == j or i + j == siz - 1 or i == siz // 2 or j == siz // 2:
                idk[i][j] = chavo
    for row in idk:
        print(" ".join(row))

print("""Доступные фигуры: 
———————————————————
треугольник (1), ▲ |
квадрат     (2), ■ |
ромб        (3), ◆ |
звездочка   (4), ∗ |
———————————————————
(другого не дано)""")
fig = input("""Напиши номер фигуры ----------------------------------------------------------------------------|
--->""").strip().lower()
siz = int(input("""Напиши размер фигуры -------------------------------------------------------------------------|
--->"""))
chavo = input("""Напиши символ кт ты хочешь заполнить фигуру --------------------------------------------------|
--->""").strip()
if not chavo:
    char = "*"
print(f"\nФигура: {fig}, размер: {siz}, символ: {chavo}\n")
if fig == "1":
    print_triangle(siz, chavo)
elif fig == "2":
    print_square(siz, chavo)
elif fig == "3":
    print_rhombus(siz, chavo)
elif fig == "4":
    if siz % 2 == 0:
        print("советую нечётный размер, он касивее")
        siz += 1
    print_star(siz, chavo)
else:
    print("Шайтан где ты видил в перечне такую фигуру, иди учись читать в 1ый класс?!")
