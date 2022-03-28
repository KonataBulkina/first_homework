my_name = 'Мария'
print(my_name)

my_age = 23
print(my_age)

five_my_name = (my_name + ' ') * 5
print(five_my_name)
print((my_name + ' ') * 5)

print("Здравствуй! Не терпится с вами познакомиться")
user_name_str = input("Как вас зовут? ")
while True:
    if ' ' in user_name_str:
        print('Ваше имя не должно содержать пробелов, попробуйте ещё раз')
        user_name_str = input("Так как же вас зовут? ")
    else:
        break

while True:
    user_age_int = (input("Сколько вам лет? "))
    if not user_age_int.isdigit():
        print('Возраст нужно указать числом, попробуйте ещё раз')
    else:
        user_age_int = int(user_age_int)
        if user_age_int <= 0 or user_age_int >= 150:
            print(f'Мне кажется, вы соврали о своем возрасте, {user_name_str}')
        else:
            break

if 0 < user_age_int < 4:
    print(f"Какая крошка, {user_name_str}!\nТы уже умеешь печатать?")
elif 3 < user_age_int < 16:
    print(f"Приветики, {user_name_str}!\nКак приятно, что дети интересуются программированием.")
elif 15 < user_age_int < 19:
    print(f"Очень приятно, {user_name_str}!\nНе думаешь сдавать егэ по информатике?")
elif 18 < user_age_int < 151:
    print(f'Очень приятно, {user_name_str}!\nМне нравится иметь дело со взрослыми')

print()
print('-' * 60)
print('Ваше имя наоборот:', user_name_str[::-1])
print('Без первых двух букв с начала и первой с конца:', user_name_str[2:-1])
print('Последние три буквы вашего имени:', user_name_str[-3:])
print('Первые пять букв:', user_name_str[:5])
print('В вашем имени', len(user_name_str), 'букв')
print('-' * 60)

age_counter = user_age_int
sum_user_age, comp_user_age = 0, 1
while age_counter != 0:
    sum_user_age += age_counter % 10
    comp_user_age *= age_counter % 10
    age_counter //= 10
print(f'Сумма чисел вашего возраста: {sum_user_age}')
print(f'Произведение чисел вашего возраста: {comp_user_age}')
print('-' * 60)
print('A ещё я могу записать ваше имя разными способами:')
print(user_name_str.upper(), user_name_str.lower(), user_name_str.capitalize(), user_name_str.swapcase())
print('-' * 60)
print('Вы спросите, зачем вам все эти данные?')
print('Не знаю)')
print()
print('Время испытать ваши математические способности!')
print('Решите пример:')
print('-' * 16)
print('88 : 4 + 66 : 2')
print('-' * 16)
while True:
    user_answer_int = (input("Ваш ответ: "))
    if not user_answer_int.isdigit():
        print('Ответ нужно указать числом, попробуйте ещё раз')
    else:
        user_answer_int = int(user_answer_int)
        if user_answer_int == 55:
            print(f'Так держать, {user_name_str}! Вы гений математики')
            break
        else:
            print(f'Вы допустили ошибку в расчетах, {user_name_str}, попробуйте ещё раз')
print()
print('Эти цветы для вас!')
print('_________(¯`.´¯)')
print('________(¯≻ ✦ ≺¯)')
print('__(¯`.´¯)(_.^._) (¯`.´¯)')
print('_(¯≻ ✦ ≺¯) _____(¯≻ ✦ ≺¯)')
print('__(_.^._) ______ (_.^._)')
