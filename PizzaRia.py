import os, re
USERS_FILE = "анапа_2007.txt"

def IsValidPh(phone):
    if not phone:
        return False
    ClPhon = re.sub(r"\D", "", phone)
    return len(ClPhon) >= 10 and len(ClPhon) <= 15

def is_valid_email(email):
    if not email:
        return False
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None 

def LoadUs():
    users = {}
    if os.path.exists(USERS_FILE):
        try:
            with open(USERS_FILE, "r", encoding="utf-8") as f:
                CurrUser = {}
                for line in f:
                    line = line.strip()
                    if line.startswith("name - "):
                        CurrUser["name"] = line.replace("name - ", "")
                    elif line.startswith("numphone - "):
                        CurrUser["phone"] = line.replace("numphone - ", "")
                    elif line.startswith("email - "):
                        CurrUser["email"] = line.replace("email - ", "")
                    elif line == "" and CurrUser:
                        if "phone" in CurrUser:
                            users[CurrUser["phone"]] = CurrUser.copy()
                        CurrUser = {}
                if CurrUser and "phone" in CurrUser:
                    users[CurrUser["phone"]] = CurrUser
            print(f"Загружено {len(users)} аккаунтов")
        except Exception as e:
            print(f"ошибка чтения файла: {e}")
    else:
        try:
            with open(USERS_FILE, "w", encoding="utf-8") as f:
                f.write("""
na# - Admin
nu+ - 4242424242
em@ - admin42@gmail.com

""")
            print("файл пользователей создан")
        except Exception as e:
            print(f"ошибка создания файла {e}")
    return users

def save_user(name, phone, email):
    try:
        with open(USERS_FILE, "a", encoding="utf-8") as f:
            f.write(f"""na# - {name}
nu+ - {phone}
em@ - {email}

""")
        return True
    except Exception as e:
        print(f"ошибка сохранения: {e}")
        return False

def AuthSyst():
    users = LoadUs()
    print("""
─────────────────────────────────────────────────────
ДОБРО ПОЖАЛОВАТЬ В TWO PIZZA
─────────────────────────────────────────────────────""")

    while True:     # ввод и проверка телефона
        phone = input("введите номер телефона").strip()
        if not phone:
            print("телефон пустой, такого быть не может!")
            continue

        if not IsValidPh(phone):
            print("неверный формат телефона, пишите 8 xxx xxx xx xx (10-15 цифр)")
            continue

        ClPhon = re.sub(r"\D", "", phone)
        break

    if ClPhon in users:
        UsData = users[ClPhon]
        print(f"""
Найден аккаунт
Имя: {UsData["name"]}
Телефон: {UsData["phone"]}
Email: {UsData["email"]}""")
        choice = input("Это ваш аккаунт? (да / нет): ").lower()
        if choice in ["да", "д", "y", "yes"]:
            print(f"Добро пожаловать, {UsData['name']}!")
            return ClPhon, UsData["email"], UsData["name"]

    print("""
Создание нового аккаунта:""")

    while True:  # ввод и проверка имени
        name = input("Введите ваше имя: ").strip()
        if not name:
            print("Имя не может быть пустым!")
            continue
        if len(name) < 2:
            print("Имя должно содержать минимум 2 символа!")
            continue
        break

    while True:  # ввод и проверка email
        email = input("Введите ваш email: ").strip()
        if not email:
            print("Email не может быть пустым!")
            continue

        if not is_valid_email(email):
            print("Неверный формат email! Пример: example@mail.com")
            continue
        break
    if save_user(name, ClPhon, email):
        print(f"""
Аккаунт успешно создан!
Имя: {name}
Телефон: {ClPhon}
Email: {email}""")
    else:
        print("Ошибка сохранения аккаунта")
    return ClPhon, email, name

import time  # главное меню + время
TimeHourAndMin = time.strftime("%H:%M")
print("""
——————————————————————————————— Добро пожаловать в TwoPizza ————————————————————————
Самый большой выбор только у нас, мы лучшая пиццирия в городе (и единственная)
(ВНИМАНИЕ МЫ НЕ РАБОТАЕМ И НЕ ОБСЛУЖИВАЕМ ПОСЛЕ 22:00 из за бомжов под окнами)
время сейчас:""", TimeHourAndMin, """
Внимание, ТОЛЬКО самовывоз!
————————————————————————————————————————————————————————————————————————————————————""")

import sys  # проверка времени
TimeHour = int(time.strftime("%H"))
if TimeHour >= 24:  # стандарт время 22 но если проверивать то 24
    print("МЫ ЗАКРЫТЫ!!!")
    sys.exit()
elif 21 >= TimeHour:
    print("""
Мы открыты, заходи братюня, только вчера продукты превезли свежии как для тебя!""")
else:
    print("чё за время у тебя")

TimePutinZOV = int(time.strftime("%j"))  # проверка дня рождения Путина
DenPutina = 0  # а если вы спросите зачем скидка в день путина то GOYDA Z V ZOV SVO
if TimePutinZOV == 279:
    print("Сегодня день рождения путина, ПРАЗДНИК и скидки!!!!")
    DenPutina = 1
else:
    print("сегодня нет никакого праздника, скидок не положено!")
    DenPutina = 0

print("""
Здравствуйте! Сколько вам лет?""")  # проверка на вруна (по возрасту)
DostMenu = "(Недоступно)"
OldOrNo = 0
while True:
    try:
        YearBryth = int(input())

        if YearBryth < 0:
            print("Возраст не может быть отрицательным! Введите реальный возраст")
            continue
        elif YearBryth == 0:
            print("Вы только что родились? Введите реальный возраст")
            continue
        elif YearBryth < 5:
            print("Вам слишком мало лет для заказа пиццы! Приходите с родителями)))")
            sys.exit()
        elif YearBryth > 120:
            print("Поздравляем с долголетием! Но такой возраст кажется нереалистичным. Введите реальный возраст")
            continue
        elif YearBryth > 150:
            print("Вы реинкарнация? Введите реальный возраст!")
            continue

        break
    except ValueError:
        print("Пожалуйста, введите число! Какие зернадцать?! Сколько вам лет?")

if YearBryth >= 18:
    OldOrNo = 1
    DostMenu = "(Доступно)"
    print("а вам ТОЧНО есть 18?")
elif 18 >= YearBryth >= 5:
    OldOrNo = 0
    DostMenu = "(Недоступно)"
    print("Вам доступно базовое меню")

if OldOrNo == 1:
    print("""
поздравляю, вам доступно расширенное меню, а также доп налог!""")

print("""
─────────────────────────────────────────────────────
РЕГИСРАЦИЯ и ВХОД В СИСТЕМУ
─────────────────────────────────────────────────────""")
CustInfo = {}
phone, email, name = AuthSyst()
CustInfo = {
    "phone": phone,
    "email": email,
    "name": name,
    "age": YearBryth  # возраст для чека
}

print(f"Успешная авторизация! Добро пожаловать, {name}!")# а какие клавиши за что отвечают ?
print("""

─────────────────────────────────────────────────────
УПРАВЛЕНИЕ ЗАКАЗОМ:
─────────────────────────────────────────────────────
N — переключение между меню
1-3 — выбор позиции в текущем меню

ВЫБОР РАЗМЕРА (после выбора позиции):
Q-15г  W-20г  E-25г  R-30г
A-100г S-250г D-500г Z-5г
C — стандартный размер для закусок

C (без выбора) — просмотр чека
ESC — выход
─────────────────────────────────────────────────────
Начните с нажатия N для просмотра меню
─────────────────────────────────────────────────────

есть фетыре меню:
1е - стандартное с пиццами
2е - расширенное """, DostMenu, """
3е - меню с напитками
4е - закуски
что вы выбрали надо нажать: допустим у вас меню 1, 
─────────────────────────────────────────────────────
""")

# Менюшки
OneMenu = """ 



|——————————————————————————————————————————————————————————————————————————————————|
|                                                                                  |
|1) Пицца четыре сира                                                              |
|Четыре сыра, на 0.5% больше чем в стандартной!                                    |
|варианты: (20см, 30см) - цены: 20см=300р, 30см=450р                               |
|                                                                                  |
|2) Пицца состоящяя на 80% из свинины                                              |
|100% халяль                                                                       |
|варианты: (5см, 15см) - цены: 5см=100р, 15см=200р                                 |
|                                                                                  |
|3) Пицца пипирони                                                                 |
|Обычная пицца, с колбасками пипирони                                              |
|варианты: (20см, 30см) - цены: 20см=350р, 30см=500р                               |
|                                                                                  |
|——————————————————————————————————————————————————————————————————————————————————|
"""

DrinkMenu = """ 



|——————————————————————————————————————————————————————————————————————————————————|
|                                                                                  |
|1) <<мохито>>                                                                     |
|обычная газировка                                              (на 25% дороже!)   |
|варианты: (100мл, 250мл) - цены: 100мл=150р, 250мл=300р                           |
|                                                                                  |
|2) Кока-кола                                                                      |
|классическая газировка                                                            |
|варианты: (250мл, 500мл) - цены: 250мл=120р, 500мл=200р                           |
|                                                                                  |
|3) Вода                                                                           |
|простая вода без газа                                                             |
|варианты: (500мл) - цена: 500мл=80р                                               |
|                                                                                  |
|——————————————————————————————————————————————————————————————————————————————————|
"""

OldMenu = """ 



|——————————————————————————————————————————————————————————————————————————————————|
|                                                                                  |
|1) Пицца с Жёлто-синим тестом, со свининой                                        |
|Отдаётся по 100% скидке в день Путина!                                            |
|описание: ZOV GOYDA SVO + экста порция ХОХЛОВ                                     |
|варианты: (25см) - цена: 600р                                                     |
|                                                                                  |
|2) Пицца с острым перцем                                                          |
|Для настоящих мужчин!                                                             |
|варианты: (30см) - цена: 550р                                                     |
|                                                                                  |
|3) Пицца с грибами и луком                                                        |
|Вегетарианский вариант                                                            |
|варианты: (20см) - цена: 400р                                                     |
|                                                                                  |
|——————————————————————————————————————————————————————————————————————————————————|
"""

SacksMenu = """ 



|——————————————————————————————————————————————————————————————————————————————————|
|                                                                                  |
|1) Картофель фри                                                                  |
|Хрустящая картошечка                                                              |
|варианты: (стандарт) - цена: 150р                                                 |
|                                                                                  |
|2) Наггетсы                                                                       |
|Куриные наггетсы, 6шт                                                             |
|варианты: (6шт) - цена: 180р                                                      |
|                                                                                  |
|3) Сырные палочки                                                                 |
|С хрустящей корочкой                                                              |
|варианты: (5шт) - цена: 200р                                                      |
|                                                                                  |
|——————————————————————————————————————————————————————————————————————————————————|
"""

prices = {  # цены
    1: {"name": "Пицца четыре сира", "sizes": {20: 600, 30: 990}, "category": "pizza"},  # пиццы
    2: {"name": "Пицца состоящяя на 80% из свинины", "sizes": {5: 200, 15: 500}, "category": "pizza"},
    3: {"name": "Пицца пипирони", "sizes": {20: 500, 30: 909}, "category": "pizza"},

    4: {"name": "Мохито", "sizes": {100: 300, 250: 600}, "category": "drink"},  # напитки
    5: {"name": "Кока-кола", "sizes": {250: 120, 500: 400}, "category": "drink"},
    6: {"name": "Вода", "sizes": {500: 8}, "category": "drink"},

    7: {"name": "Пицца с Жёлто-синим тестом", "sizes": {25: 150}, "category": "adult"}, # расширенное меню (для налого плательшиков)
    8: {"name": "Пицца с острым перцем", "sizes": {30: 550}, "category": "adult"},
    9: {"name": "Пицца с грибами и луком", "sizes": {20: 400}, "category": "adult"},

    10: {"name": "Картофель фри", "sizes": {"стандарт": 150}, "category": "snack"},  # закуски
    11: {"name": "Наггетсы", "sizes": {"6шт": 299}, "category": "snack"},
    12: {"name": "Сырные палочки", "sizes": {"3шт": 185}, "category": "snack"}
}
CurrentMenu = 0  # переменные заказоф
SelectedItem = 0
OrderItems = []

def ShowMenu():
    global CurrentMenu
    if CurrentMenu == 1:
        print(f"первое меню: {OneMenu}")
        print("Выберите пиццу (1-3) или нажмите N для следующего меню")
    elif CurrentMenu == 2:
        print(f"меню с напитками: {DrinkMenu}")
        print("Выберите напиток (4-6) или нажмите N для следующего меню")
    elif CurrentMenu == 3 and OldOrNo == 1:
        print(f"меню для старых: {OldMenu}")
        print("Выберите пиццу (7-9) или нажмите N для следующего меню")
    elif CurrentMenu == 3 and OldOrNo == 0:
        print(f"внимание, вам: {DostMenu}")
        print("Нажмите N для следующего меню")
    elif CurrentMenu == 4:
        print(f"меню закусок: {SacksMenu}")
        print("Выберите закуску (10-12) или нажмите C для чека")

def SelectItem(ItemNum):
    global SelectedItem
    if ItemNum in prices:
        if prices[ItemNum]["category"] == "adult" and OldOrNo == 0: # доступ к взрослому меню (проверка)
            print("Вам нет 18 лет! Это меню НЕдоступно")
            return False

        SelectedItem = ItemNum
        ItemName = prices[ItemNum]["name"]
        AvailSiz = list(prices[ItemNum]["sizes"].keys())
        print(f"Выбрано: {ItemName}")
        print(f"Доступные размеры: {AvailSiz}")

        SizMapp = {  # подсказки
            20: "W", 30: "R", 5: "Z", 15: "Q", 25: "E",
            100: "A", 250: "S", 500: "D", "стандарт": "C",
            "6шт": "C", "5шт": "C", "3шт": "C"
        }

        print("Клавиши для размеров:")
        for size in AvailSiz:
            key = SizMapp.get(size, "?")
            print(f"  {key} - {size}")

        return True
    return False

import keyboard

def SelectSize(SizChoice):
    global SelectedItem, OrderItems
    if SelectedItem:
        ItemDat = prices[SelectedItem]

        if isinstance(SizChoice, str) and SizChoice.isdigit():
            SizChoice = int(SizChoice)

        if SizChoice in ItemDat["sizes"]:
            price = ItemDat["sizes"][SizChoice]

            if DenPutina == 1:  # скидка в день путина
                discount = price * 0.99  # 99% скидка
                price = int(price - discount)
                print(f"СКИДКА 99% В ДЕНЬ ПУТИНА! -{discount} руб.")

            OrderItems.append({
                "name": ItemDat["name"],
                "size": SizChoice,
                "price": price,
                "category": ItemDat["category"]
            })

            print(f"Добавлено: {ItemDat['name']} {SizChoice} - {price} руб.")
            print("Нажмите 'С' для просмотра чека или продолжайте выбирать")
            SelectedItem = 0
            return True
        else:
            print("Неверный размер! Доступные размеры:", list(ItemDat["sizes"].keys()))
    return False

def ShowReceipt():
    global OrderItems, CustInfo
    if not OrderItems:
        print("Заказ пуст!")
        return

    total = 0
    print("""
           ВАШ ЧЕК TwoPizza:
    =================================
    Самовывоз,
    Телефон + почта:""", CustInfo["phone"], CustInfo["email"], """
    Возраст:""", CustInfo["age"]
          )

    for i, item in enumerate(OrderItems, 1):
        print(f"{i}. {item['name']} {item['size']} - {item['price']} руб.")
        total += item["price"]

    if OldOrNo == 1:  # налог для hjcks[ [hzrjd
        TaxAm = total * 0.1  # 10% налог
        print(f"Налог для взрослых (10%): {TaxAm} руб.")
        total += TaxAm

    print("""
    ─────────────────────────────────────────────────────
    ИТОГО:""", total, """
    ─────────────────────────────────────────────────────
    Спасибо за заказ, ждем вас снова!""")

def OnKeyPress(event):
    global CurrentMenu, SelectedItem
    print(f"Нажата клавиша: {event.name}")

    if event.name == "n":  # переключение меню
        CurrentMenu = (CurrentMenu % 4) + 1
        ShowMenu()
        SelectedItem = 0

    elif not SelectedItem:  # Выбор позиции
        if CurrentMenu == 1 and event.name in ["1", "2", "3"]:
            SelectItem(int(event.name))
        elif CurrentMenu == 2 and event.name in ["4", "5", "6"]:
            SelectItem(int(event.name))
        elif CurrentMenu == 3 and event.name in ["7", "8", "9"] and OldOrNo == 1:
            SelectItem(int(event.name))
        elif CurrentMenu == 4 and event.name in ["1", "2", "3"]:
            SelectItem(int(event.name) + 9)  # Закуски 10,11,12
        elif event.name.lower() == "c":  # Просмотр чека
            ShowReceipt()

    else:  # выбор размера для выбранной позиции
        SizMapp = {
            "q": 15, "w": 20, "e": 25, "r": 30,
            "a": 100, "s": 250, "d": 500,
            "z": 5  # стандартный размер
        }

        if event.name in SizMapp:
            SelectSize(SizMapp[event.name])
        elif event.name.lower() in ["с", "c"] and SelectedItem in [10, 11, 12]:
            SizMap = {10: "стандарт", 11: "6шт", 12: "5шт"}
            SelectSize(SizMap[SelectedItem])


CurrentMenu = 1  # основной цикл
ShowMenu()
keyboard.on_press(OnKeyPress)
keyboard.wait()
