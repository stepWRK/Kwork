# уравень B
# №1
# Вычислительная сложность линейного поиска выше в худшем случае
# линейный поиск (LinearSearch) в худшем случае перебирает все n элементов списка
#    временная сложность: O(n)
# бинарный поиск (BinarySearch) требует предварительно отсортированный список на каждом шаге он делит область поиска пополам, поэтому в худшем случае количество шагов — log₂(n)
#    временная сложность: O(log n)
# Итог: при x → ∞ линейный поиск работает значительно медленнее логично что МЕДЛЕНЕЕ
# Ps: если вам нужно доказательство то просто посммотрите коды других в гите
#
# №2 -----------------------------------------------------------------------
import random, time
X = 10
Num = [random.randint(1, 100) for _ in range(X)]
Even = sum(1 for x in Num if x % 2 == 0)
Odd = X - Even
Result = Even * Odd
print("всего:", Num, "четных:", Even, "нечетных:", Odd, "количество пар с нечетной сумой:", Result)

print("""      
""")# №3 -----------------------------------------------------------------------

Xx = 10
list1 = [random.randint(1, 100) for _ in range(Xx)]
list2 = [random.randint(1, 100) for _ in range(Xx)]
list1.sort()
list2.sort()
print("отсортированный список 1:", list1, "отсортированный список 2:", list2)
def MergeSortedList(a, b):
    Merged = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            Merged.append(a[i])
            i += 1
        else:
            Merged.append(b[j])
            j += 1
    Merged.extend(a[i:])
    Merged.extend(b[j:])
    return Merged
MergedList = MergeSortedList(list1, list2)
print("отсортированный слитый список:", MergedList)

print("""      
""")# №4 -----------------------------------------------------------------------
def LinearSearch(lys, element):#линейный
    for i in range(len(lys)):
        if lys[i] == element:
            return i
    return -1
def BinarySearch(lys, val):#биарный нет блин небинарный
    first = 0
    last = len(lys) - 1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first + last) // 2
        if lys[mid] == val:
            index = mid
        else:
            if val < lys[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return index

Sizes = [1000, 10000, 100000, 1000000, 10000000]  # добавил 10 млн
results = []

for size in Sizes:
    Arr = sorted([random.randint(1, 1000000) for _ in range(size)])
    Target = Arr[-1]
    Start = time.PerCount()
    LinearSearch(Arr, Target) # рубрика ЭЭЭЭЭЭКАСПЕРЕМЕНТЫЫЫ
    LinTime = time.PerCount() - Start
    Repeats = 1000
    Start = time.PerCount()
    for _ in range(Repeats):
        BinarySearch(Arr, Target)
    BinTIme = (time.PerCount() - Start) / Repeats
    results.append((size, LinTime, BinTIme))
print(f"{'Колч':<12} {'Линейный (s)':<15} {'бинарный (s)':<18} {'соотношение':<10}")
for size, lt, bt in results:
    ratio = lt / bt
    print(f"{size:<12} {lt:<15.6f} {bt:<18.10f} {ratio:<10.2f}")