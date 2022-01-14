"""

Киберколбаса
Написать класс Sausage, имитирующий киберколбасу. Киберколбаса может быть проинициализирована
нулём значений (создаётся колбаса по умолчанию, см. пример), одним (фарш типа str) и
двумя (фарш, и объём типа Fraction). Длина целого батона киберколбасы — 12 символов фарша и
2 символа оболочки. Колбаса единичного объёма — это один полный батон, более, чем единичного —
это несколько батонов (последний, возможно, неполон). Неполный батон заканчивается срезом.
Киберколбаса поддерживает операции умножения и деления на целое число, сложение и вычитание с
другой киберколбасой (фарш результата совпадает с фаршем первого операнда), а также взятие абсолютного
значения (возвращается объём). Отрицательного объёма не бывает, в этом случае он делается нулевым.
Если объём киберколбасы нулевой, батон считается пустым.

Примеры
Входные данные
a, b, c = Sausage(), Sausage("HAM", "5/6"), Sausage("SPAM.", 1.25)
print(a, b, c, sep="\n")
print(a+b+c)
print(b*2, 4*c/5, sep="\n")
d, e = b+a/6-5*c/4, a-c
print(d, not d)
print(e, not e)
Результат работы
/------------\
|pork!pork!po|
|pork!pork!po|
|pork!pork!po|
\------------/
/----------|
|HAMHAMHAMH|
|HAMHAMHAMH|
|HAMHAMHAMH|
\----------|
/------------\/---|
|SPAM.SPAM.SP||SPA|
|SPAM.SPAM.SP||SPA|
|SPAM.SPAM.SP||SPA|
\------------/\---|
/------------\/------------\/------------\/-|
|pork!pork!po||pork!pork!po||pork!pork!po||p|
|pork!pork!po||pork!pork!po||pork!pork!po||p|
|pork!pork!po||pork!pork!po||pork!pork!po||p|
\------------/\------------/\------------/\-|
/------------\/--------|
|HAMHAMHAMHAM||HAMHAMHA|
|HAMHAMHAMHAM||HAMHAMHA|
|HAMHAMHAMHAM||HAMHAMHA|
\------------/\--------|
/------------\
|SPAM.SPAM.SP|
|SPAM.SPAM.SP|
|SPAM.SPAM.SP|
\------------/
/|
||
||
||
\| True
/|
||
||
||
\| True

"""


from fractions import Fraction


class Sausage:
    def __init__(self, filling='pork!', volume="1.0"):
        self.filling = filling
        if Fraction(volume) >= 0.0:
            self.volume = volume
        else:
            self.volume = "0.0"

    def __add__(self, other):
        return Sausage(self.filling, str(Fraction(self.volume) + Fraction(other.volume)))

    def __sub__(self, other):
        return Sausage(self.filling, str(Fraction(self.volume) - Fraction(other.volume)))

    def __mul__(self, other):
        return Sausage(self.filling, str(Fraction(self.volume) * Fraction(other)))

    def __rmul__(self, other):
        return Sausage(self.filling, str(Fraction(self.volume) * Fraction(other)))

    def __truediv__(self, other):
        return Sausage(self.filling, str(Fraction(self.volume) / Fraction(other)))

    def __abs__(self):
        return Fraction(self.volume)

    def __bool__(self):
        if Fraction(self.volume) == 0.0:
            return False
        else:
            return True

    def __str__(self):
        saus_cnt = int(Fraction(self.volume))
        is_whole = float(Fraction(self.volume) % 1) == 0.0

        word_cnt = int(12 // len(self.filling))
        end_ind = int(12 % len(self.filling))

        top = saus_cnt * ("/" + '-' * 12 + "\\")
        saus = saus_cnt * ("|" + self.filling * word_cnt + self.filling[:end_ind] + '|')
        end = saus_cnt * ("\\" + '-' * 12 + "/")

        float_part = Fraction(self.volume) % 1 * 12
        if not is_whole or Fraction(self.volume) == 0.0:
            word_cnt = int(float_part // len(self.filling))
            end_ind = int(float_part % len(self.filling))

            top += "/" + '-' * int(float_part) + "|"
            saus += "|" + self.filling * word_cnt + self.filling[:end_ind] + '|'
            end += "\\" + '-' * int(float_part) + "|"

        res = top + '\n' + (saus + '\n') * 3 + end

        return res