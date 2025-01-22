"""
Число 31 в данном контексте связано с размером типа данных в компьютере, который используется для представления целых чисел. В большинстве современных архитектур, таких как 32-битные и 64-битные процессоры, целые числа представлены в виде 32-битных или 64-битных знаковых значений.

Подробное объяснение:
1. Знаковые целые числа: В большинстве систем целые числа представлены в формате двойного дополнения (two’s complement). В этом формате старший бит числа (самый левый) используется для обозначения знака числа:
  • Если старший бит равен 0, то число положительное или ноль.
  • Если старший бит равен 1, то число отрицательное.
 2. Сдвиг на 31 бит:
  • Когда вы сдвигаете разность  a - b  вправо на 31 бит, это позволяет из старшего бита (бита знака) получить либо 0, либо -1.
  • Если результат  a - b  положителен или равен 0 (то есть  a >= b ), бит знака будет равен 0, и сдвиг вправо на 31 бит даст 0.
  • Если  a - b  отрицательное (то есть  a < b ), бит знака будет равен 1, а сдвиг вправо на 31 бит даст -1, так как арифметический сдвиг сохраняет знак числа.

Почему именно 31 бит?
  • 31 бит выбирается потому, что для 32-битных целых чисел старший бит находится на позиции 31 (нумерация начинается с 0).
  • Сдвиг на 31 бит переносит знак числа (старший бит) в крайний правый бит (младший), превращая его в 0 или -1.
  • Мы используем 31, потому что сдвиг вправо должен полностью сдвинуть все биты, кроме бита знака.

Пример:
  • Если a = 10, b = 20:
      • Разность a - b = 10 - 20 = -10.
      • В двоичной системе, если мы рассматриваем 32-битное представление, -10 выглядит как 11111111111111111111111111110110.
      • При сдвиге на 31 бит вправо результат будет 11111111111111111111111111111111, что соответствует значению -1.
  • Если a = 20, b = 10:
      • Разность a - b = 20 - 10 = 10.
      • В двоичной системе 10 выглядит как 00000000000000000000000000001010.
      • При сдвиге на 31 бит вправо результат будет 00000000000000000000000000000000, что соответствует значению 0.

Таким образом, сдвиг на 31 бит позволяет получить информацию о знаке разности, что помогает решить задачу без явного использования операторов сравнения.
"""


def max_of_two(x: int, y: int) -> int:
    diff_sign = (x - y) >> 31  # 0 if x >= y, -1 if x < y.
    return x * (1 + diff_sign) - y * diff_sign


assert max_of_two(-100, 100) == 100
assert max_of_two(5, 2) == 5
assert max_of_two(4, 4) == 4
assert max_of_two(10, 20) == 20
assert max_of_two(95, -1) == 95
assert max_of_two(95, -1) == 95
