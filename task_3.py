print('Задача 3. Марсоход-2')

# К роботу Валли отправили «коллегу» Билли.
# Это его первая высадка на Марс, поэтому его тестируют в прямоугольном помещении размером 15 × 20 м.
# Марсоход высаживается в центре комнаты (в точке 8, 10), затем управление им передаётся оператору, то есть пользователю вашей программы.

# Программа спрашивает, в какую сторону оператор хочет направить робота:
# север (клавиша W), юг (клавиша S), запад (клавиша A) или восток (клавиша D).
# Оператор делает выбор, марсоход перемещается в эту сторону на один метр, а программа сообщает новую позицию робота.
# Если марсоход упёрся в стену, он не должен пытаться переместиться в сторону стены — в этом случае его позиция не меняется.

# Создайте программу для управления роботом Билли.

# Пример:
# [Программа]: Марсоход находится на позиции 6, 19, введите команду:
# [Оператор]: A
# [Программа]: Марсоход находится на позиции 5, 19, введите команду:
# [Оператор]: W
# [Программа]: Марсоход находится на позиции 5, 20, введите команду:
# [Оператор]: W
# [Программа]: Марсоход находится на позиции 5, 20, введите команду:

maximum_x = 15
maximum_y = 20
minimum_x = 1
minimum_y = 1

position_x = 8
position_y = 10

while True:
    comand = input(f'[Программа]: Марсоход находится на позиции {position_x}, {position_y}, введите команду: ')
    if comand.upper() == "A":
        position_x -= 1
    elif comand.upper() == "D":
        position_x += 1
    elif comand.upper() == "W":
        position_y += 1
    elif comand.upper() == "S":
        position_y -= 1
    else:
        print("[Программа]: Команда не известна, введите корректную команду: (W, S, A, D) ") 
    if position_y > maximum_y:
        position_y = maximum_y
        continue
    if position_y < minimum_y:
        position_y = minimum_y
        continue
    if position_x > maximum_x:
        position_x = maximum_x
        continue
    if position_x < minimum_x:
        position_x = minimum_x
        continue