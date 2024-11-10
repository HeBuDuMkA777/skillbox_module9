print('Задача 5. Коровы')

# Для коров есть 10 стойл.
# В каждом из них условия для животных разные, поэтому и молока они дают по-разному.
# В первом стойле производят 2 литра в день, во втором — 4, в третьем — 6, далее — 8, 10, 12, 14, 16, 18 и 20.
# При этом коровы находятся не во всех стойлах.
# Свободные и занятые обозначаются строкой из букв a и b, где a — свободное стойло, b — занятое.

# Напишите программу для подсчёта получаемого молока в коровнике.
# Важно учитывать следующее взаимодействие: пользователь вводит строку из десяти символов a и b.
# Необходимо определить, сколько в итоге будет произведено молока за день.

# Пример 1
# Введите 10 стойл в одну строку. a — свободное стойло, b — занятое:
# abababaaaa
# Произведено молока за день: 24

# Пример 2
# Введите 10 стойл в одну строку. a — свободное стойло, b — занятое:
# aaababbaab
# Произведено молока за день: 54

positions = input("Введите 10 стойл в одну строку. а - свободное стойло, b - занятое: \n")
step = 2
milk_amount = 2
all_milk = 0
flag = True

while flag == True:
    if len(positions) != 10:
        positions = input("Введено неверное количество стойл! Попробуйте ввести 10 стойл: \n")
    else:
        for position in positions:
            if position.upper() == "B":
                all_milk += milk_amount
            milk_amount += step
        print(f"Произведено молока за день: {all_milk}")
        flag = False