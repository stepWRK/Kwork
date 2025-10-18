import random

print("""напишите 2 значения выс и шир (мин 6)
пустоты рядом с берегами являются лужами
рекоммендованные размеры: 90 x 90
——————————————————————————————————————————————""")
width = int(input("Ширина области: "))
height = int(input("Высота области: "))
Isl = [["ㅤ" for _ in range(width)] for _ in range(height)]
tudaX = width // 2
tudaY = height // 2
Isl[tudaY][tudaX] = "▨"
KudaSuda = [(-1, 0), (1, 0), (0, -1), (0, 1)]
XEd = random.randint(width * height // 4, width * height // 2)
Used = 0

# справочник по переменным
# Isl - острове
# tudaX/Y - ширина и выс терр для ген
# KudaSuda - направления для ген
# XEd - еденицы
# Used - использованно
while Used < XEd:
    y = random.randint(1, height - 2)
    x = random.randint(1, width - 2)
    if Isl[y][x] == "▨":
        dx, dy = random.choice(KudaSuda)
        tudaX, tudaY = x + dx, y + dy
        if 1 <= tudaX < width - 1 and 1 <= tudaY < height - 1:
            if Isl[tudaY][tudaX] == "ㅤ":
                Isl[tudaY][tudaX] = "▨"
                Used += 1

print("\nСлучайный остров:")
for StR in Isl:
    print("".join(StR))

#Генерация озёр —————————————————————————————————————————————————————

# Генерация клада ————————————————————————————————————————————————————
KladGen = False
Attem = 0
MAttem = 1000
while not KladGen and Attem < MAttem:
    y = random.randint(1, height - 2)
    x = random.randint(1, width - 2)
    if Isl[y][x] == "▨" and (y != height // 2 or x != width // 2):
        is_safe = True
        for dx, dy in KudaSuda:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height:
                if Isl[ny][nx] == "ㅤ":
                    is_safe = False
                    break
        if is_safe:
            Isl[y][x] = "▣"
            KladGen = True
    Attem += 1

print("\nостров с озером и кладом:")
for StR in Isl:
    print("".join(StR))

if OzerGen:
    print("\nОзеро ~ размещено")
else:
    print("\nОзеро не размещено, попробуй ещё раз")

if KladGen:
    print("Клад ▣ размещён")
else:
    print("Клад не размещён, попробуй ещё раз")