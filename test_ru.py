from armpy.ru import *

вывод()
вывод('Тестирование русской версии')
вывод()
число1 = ввод("Введите число 1: ")
число2 = ввод("Введите число 2: ")
число1 = целое(число1)
число2 = целое(число2)
ответ = число1 / число2
вывод("Сумма:", число1 + число2)
вывод("Деление:", ответ)
вывод("Округление:", округлять(ответ))
