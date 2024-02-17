# Цель работы: Применить dunder (двойное подчеркивание - __) методы iter, next в своём классе
class EvenNumbers:
    def __init__(self, start=0, end=1):
        if not start < end:  # Значение атрибута start всегда меньше значения атрибута end
            print('Значение атрибута start долджно быть меньше значения атрибута end')
        if start % 2:  # проверка на "вшивость"
            start += 1
        self.start = start - 2  # start – начальное значение (если значение не передано, то 0)
        self.end = end  # end – конечное значение (если значение не передано, то 1)

    def __iter__(self):
        self.i = self.start  # обнуляем счетчик
        return self

    def __next__(self):
        self.i += 2
        if self.i < self.end:
            return self.i
        raise StopIteration()


en = EvenNumbers(10, 8)
for i in en:
    print(i)
