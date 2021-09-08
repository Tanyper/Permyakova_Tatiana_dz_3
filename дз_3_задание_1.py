num = {"zero":"Ноль","one":"Один","two":"Два", "three":"Три", "for":"Четыре","five":"Пять", "six": "Шесть","seven":"Семь",
       "eight":"Восемь", "nine":"Девять", "ten":"Десять"}
def translate (number):
    return num.get (number)
print (translate(input("Введите любой номер на английском: ")))