from random import *
def prov(x): #Проверка на дурака
    if x.isdigit():
        x = int(x)
        return x
    else:
        return 'error'
def game(): #Игра
    bool = True
    print('Добро пожаловать в числовую угадайку')
    print('Укажите максимальное число для игры') #Ввод предела игры
    num3 = input()
    num3 = prov(num3)
    while num3 == 'error':
        print('Вы, написали не целое число!', 'Введите целое число') #Поворный ввод, если ввели не число
        num3 = input()
        num3 = prov(num3)
    num = randrange(1,num3)
    kp = 0

    print('Игра начинается')
    while bool == True:
        print('Введите число от 1 до', num3)
        num2 = input()
        num2 = prov(num2)
        while num2 == 'error':
            print('Вы, написали не целое число!', 'Введите число от 1 до', num3) #Поворный ввод, если ввели не число
            num2 = input()
            num2 = prov(num2)
        kp += 1
        if num > num2:
            print('Слишком мало, попробуйте еще раз')
        if num < num2:
            print('Слишком много, попробуйте еще раз')
        if num == num2:
            print('Вы угадали, поздравляем!', 'Количество попыток:', kp)
            bool = False
    return 'Спасибо, что играли в числовую угадайку. Еще увидимся...'
otv = 'Yes'
while otv == 'Yes':
    print(game())
    print('Поиграем еще раз? Yes|No')
    otv = input()

