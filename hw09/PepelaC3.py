"""
Пепелац-Ц-III
Пепелац собирается из отдельных деталей по инструкции.
В инструкцию входит перечень подсистем, из которых состоит пепелац (не менее двух),
собственных деталей пепелаца и списка всех деталей, которые требуются для сборки.
Это последняя строка инструкции. В начале инструкции идут описания самих подсистем в формате
«имя_системы» «перечень подсистем» «список собственных деталей». Проверить корректность инструкции —
соответствует ли она правилам. Если соответствует — вывести «Correct», в противном случае — «Incorrect».

Правила:

Имя подсистемы — одна заглавная латинская буква (проверять не надо)
Имя детали — одна строчная латинская буква (проверять не надо)
«Список» деталей или подсистем — это строка, возможно, пустая
В разных подсистемах могут встречаться детали с одинаковыми именами
{i} В каждом списке все буквы разные
{i} Поиск детали осуществляется по алгоритму «MRO C3»: в порядке появления подсистем в списке, но также и в том
порядке, в котором они требуют детали друг из друга. Если совмещение порядков невозможно, инструкция некорректна
Например, если подсистеме B требуются детали из подсистемы A, но в како-то списке A идет раньше B — инструкция некорректна
{i} Деталь из списка необходимых должна присутствовать среди собственных или в перечисленных подсистемах
Примеры
Входные данные
A abc
B cde
C A f
D AB e
DC e abcdef

Результат работы
Correct

"""

class_definition = \
"""
class {cls_name}({parents}):
    def __init__(self):
        self.details = set()
        super().__init__()
        self.details.update("{details}")


"""

program_code = ""

a = "1 cls definition"
cls_name, parents, details = "", "", ""

a = input().split()
while len(a[0]) == 1:
    cls_name = a[0]
    if len(a) == 3:
        parents = ",".join(a[1])
        details = a[2]
    elif len(a) == 2:
        if a[1] == a[1].upper():
            parents = ",".join(a[1])
            details = ""
        else:
            parents = ""
            details = a[1]

    program_code += class_definition.format(cls_name=cls_name, parents=parents, details=details)
    a = input().split()

parents = ",".join(a[0])
details = "" if len(a) == 2 else a[1]
required_details = a[1] if len(a) == 2 else a[2]

program_code += class_definition.format(cls_name="NewClass", parents=parents, details=details)

program_code += "obj = NewClass()\n"

program_code += f"if obj.details & set(\"{required_details}\") != set(\"{required_details}\"):\n    raise Exception"

# f = open("program.py", "w")
# f.write(program_code)

try:
    exec(program_code)
    print("Correct")
except:
    print("Incorrect")