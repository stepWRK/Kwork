print("напишите число")
zov = int(input())
for i in range(1, zov + 1):
    print(i)

#———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
print("""
================
——— Задача 2 ———

введите число от кт""")
Atw = int(input())
print("введите число до кт")
Btw = int(input())
print("Числа от", Atw, "до", Btw)
if Atw < Btw:
    for i in range(Atw, Btw + 1):
        print(i)
else:
    for i in range(Atw, Btw - 1, -1):
        print(i)

#———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
print("""
================
——— Задача 3 ———

введите натуральное число:""")
N = int(input())
isQadTwo = True
InterP = N

if InterP <= 0:
    isQadTwo = False
else:
    while InterP > 1:
        if InterP % 2 != 0:
            isQadTwo = False
            break
        InterP //= 2
print("YES" if isQadTwo else "NO") # my english is bulocka s coriciu

#———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
print("""
================
——— Задача 4 ———
""")
def FBInachi(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return FBInachi(n - 1) + FBInachi(n - 2)

fbiN = int(input("Введите номер числа Фибоначчи: "))
print(f"F({fbiN}) = {FBInachi(fbiN)}")
print("Первые 10 чисел фибаначи ↓")
for i in range(1, 11):
    print(f"F({i}) = {FBInachi(i)}")