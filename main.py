import pickle
import random

# запрос новых настроек поля
def ask_settings():
    global array_game
    global num_strok
    global num_stolbets
    global count_pobeda
    while True:
        try:
            num_strok = int(input('Введите количество строк: '))  # количество строк
            break
        except ValueError:
            print("Укажите, пожалуйста, число...")
    while True:
        try:
            num_stolbets = int(input('Введите количество столбцов: '))  # количество столбцов
            break
        except ValueError:
            print("Укажите, пожалуйста, число...")
    while True:
        try:
            count_pobeda = int(input('Введите значение необходимое для победы: '))
            break
        except ValueError:
            print("Укажите, пожалуйста, число...")
        # инициализация массива пустыми значениями
    array_game = [[" " for j in range(num_stolbets)] for i in range(num_strok)]

# вход/регестрация:
def sign_in():
    # ввод обязательных перемнных
    global wanna_continue
    global down_me
    wanna_continue = '-'
    down_me = '-'
    global array_game
    global name
    global up_me
    global num_stolbets
    global num_strok
    global count_pobeda
    up_me = input('Вы здесь впервые(+/-)? ')
    while up_me != '+' and up_me != '-':
        up_me = input('Вы здесь впервые(+/-)? ')
    if up_me == '-':
        # если был новый пользователь, который сохранил игру в какой то момент, не завершив ее до конца
        with open("savegam", "rb") as f:
            num_strok_dict = pickle.load(f)
            name = input('Как мне можно к Вам обращаться? ').title()
            if name in num_strok_dict:
                print('Приятно снова встретиться с Вами, ', name.title(), '!')
            else:
                # проверка на пользователей, завершивших игру
                with open("saveres", "rb") as f:
                    games_dict = pickle.load(f)
                    for url in games_dict:
                        while name not in games_dict:
                            print('Имя не найдено, попробуйте еще раз...')
                            name = input('Как мне можно к Вам обращаться? ').title()
                    print('Приятно снова встретиться с Вами, ', name.title(), '!')
        # для старых пользователей, если есть сохраненная игра
        with open("savegam", "rb") as f:
            num_strok_dict = pickle.load(f)
            if name in num_strok_dict:
                wanna_continue = input('Хотите продолжить с сохраненного момента(+/-)? ')
                while wanna_continue != '+' and wanna_continue != '-':
                    wanna_continue = input('Хотите продолжить с сохраненного момента(+/-)? ')
                if wanna_continue == '+':
                    # выгружаем переменные из словаря с сохраненными играми по имени
                    with open("savegam", "rb") as f:
                        num_strok_dict = pickle.load(f)
                        num_stolbets_dict = pickle.load(f)
                        count_pobeda_dict = pickle.load(f)
                        up_me_dict = pickle.load(f)
                        sign_of_user_dict = pickle.load(f)
                        sign_of_computer_dict = pickle.load(f)
                        array_game_dict = pickle.load(f)
                        num_strok = num_strok_dict[str(name)]
                        num_stolbets = num_stolbets_dict[str(name)]
                        count_pobeda = count_pobeda_dict[str(name)]
                        up_me = up_me_dict[str(name)]
                        sign_of_user = sign_of_user_dict[str(name)]
                        sign_of_computer = sign_of_computer_dict[str(name)]
                        array_game = array_game_dict[str(name)]
                        print('Приятного продолжения игры, ', name.title(), '!')

                # если не захотел продолжать игру-спросить про настройки поля
                if wanna_continue == '-':
                    with open("saveever", "rb") as f:
                        num_strok_dict = pickle.load(f)
                        if name in num_strok_dict:
                            down_me = input('Хотите загрузить старые настройки поля(+/-)? ')
                            while down_me != '+' and down_me != '-':
                                down_me = input('Хотите загрузить старые настройки поля(+/-)? ')
                            if down_me == '+':
                                # выгружаем настройки поля из словаря по имени

                                with open("saveever", "rb") as f:
                                    num_strok_dict = pickle.load(f)
                                    num_stolbets_dict = pickle.load(f)
                                    count_pobeda_dict = pickle.load(f)
                                    num_strok = num_strok_dict[str(name)]
                                    num_stolbets = num_stolbets_dict[str(name)]
                                    count_pobeda = count_pobeda_dict[str(name)]
                                    # инициализация массива пустыми значениями
                                array_game = [[" " for j in range(num_stolbets)] for i in range(num_strok)]

                            # запрашиваем новые настройки поля, если не захотели загружать старые
                            else:
                                ask_settings()

                        # спрашиваем новые настройки, если нет старых
                        else:
                            ask_settings()

            # если нет сохраненной игры, просто спрашиваем про сохраненные настрйоки поля(если есть)
            else:
                with open("saveever", "rb") as f:
                    num_strok_dict = pickle.load(f)
                    if name in num_strok_dict:
                        down_me = input('Хотите загрузить старые настройки поля(+/-)? ')
                        while down_me != '+' and down_me != '-':
                            down_me = input('Хотите загрузить старые настройки поля(+/-)? ')
                        if down_me == '+':
                            with open("saveever", "rb") as f:
                                num_strok_dict = pickle.load(f)
                                num_stolbets_dict = pickle.load(f)
                                count_pobeda_dict = pickle.load(f)
                                num_strok = num_strok_dict[str(name)]
                                num_stolbets = num_stolbets_dict[str(name)]
                                count_pobeda = count_pobeda_dict[str(name)]

                                # инициализация массива пустыми значениями
                            array_game = [[" " for j in range(num_stolbets)] for i in range(num_strok)]

                        # если пользователь не захотел загружать старые
                        else:
                            ask_settings()

                    # если нет сохраненных настроек поля, спросить новые
                    else:
                        ask_settings()


    # если пользователь новый
    elif up_me == '+':
        with open('saveever', 'rb') as f:
            num_strok_dict = pickle.load(f)
            name = input('Как мне можно к Вам обращаться? ').title()
            for url in num_strok_dict:
                while name in num_strok_dict:
                    print('Данное имя занято, укажите другое... ')
                    name = input('Как мне можно к Вам обращаться? ').title()
            print('Приятно познакомиться с Вами, ', name.title(), '!')

            # спрашиваем новые настройки
            ask_settings()

        # инициализация массива пустыми значениями
        array_game = [[" " for j in range(num_stolbets)] for i in range(num_strok)]

# инструкция
def display_instruct(array_game):
    """Выводит на экран  иснтрукцию для игрока"""
    print(
        """
Добро пожаловать в игру Крестики-нолики!
С Вами будет сражаться компьютер.
Если захотите прервать игру, то у вас будет возможность в любой момент начать ее с сохранённого момента, 
просто введите '0' вместо номера строки или столбца!
Чтобы сделать свой ход, введите сначала номер строки, а затем-номер столбца.
Числа соответсвуют полям доски:""")
    # показывает доску
    board(array_game)

# игровая доска
def board(array_game):
    # печать номеров столбцов
    i = 0
    print(" ", end='')
    while i < (len(array_game[0]) * 2 + 1):
        if i % 2 == 0:
            print(" ", end='')
        else:
            print(i // 2 + 1, end='')
        i += 1
    print("")

    i = 0

    while i < len(array_game):
        print(i + 1, end='')  # печать номера строки
        j = 0
        # печать строки
        while j < (len(array_game[i]) * 2 + 1):
            if j % 2 == 0:
                print("|", end='')
            else:
                print(array_game[i][j // 2], end='')
            j += 1
        print("")
        i += 1


# новая доска
def new_board(array_game):
    for i in range(num_strok):
        for j in range(num_stolbets):
            if array_game[i][j] == 'X' or array_game[i][j] == 'O':
                array_game[i][j] = ' '


# кто ходит первым(случайный выбор)
def who_goes_first():
    global sign_of_user
    global sign_of_computer
    sign_of_user = ''
    sign_of_computer = ''
    """Выбор первого хода, 0 - человек, 1 -компьютер"""
    first = random.randint(0, 1)
    if first == 0:
        print('Поздравляю, Вы ходите первым!')
        sign_of_user = 'X'
        sign_of_computer = 'O'
    else:
        print('Первым выпал шанс ходить компьютеру')
        sign_of_user = 'O'
        sign_of_computer = 'X'


# если первый ход компьютера
def if_comp_first(array_game):
    if sign_of_computer == 'X':
        move_of_computer(array_game)
        board(array_game)


# ход игрока
def move_of_user(array_game):
    while True:
        try:
            stroka = int(input('Введите номер строки: '))
            break
        except ValueError:
            print("Укажите, пожалуйста, число...")
    if stroka == 0:
        save_moment()
    while True:
        try:
            stolbets = int(input('Введите номер столбца: '))
            break
        except ValueError:
            print("Укажите, пожалуйста, число...")
    if stolbets == 0:
        save_moment()
    while stroka > num_strok or stroka < 0 or stolbets > num_stolbets or stolbets < 0:
        print('Так нельзя! Попробуйте еще раз')
        stroka = int(input('Введите номер строки: '))
        stolbets = int(input('Введите номер столбца: '))
    while array_game[stroka - 1][stolbets - 1] == "X" or array_game[stroka - 1][stolbets - 1] == "O":
        print('Здесь занято!')
        stroka = int(input('Введите номер строки: '))
        stolbets = int(input('Введите номер столбца: '))
    else:
        array_game[stroka - 1][stolbets - 1] = sign_of_user


# ход компьютера
def move_of_computer(array_game):
    c = True
    while c:
        a = random.randint(0, num_strok - 1)
        b = random.randint(0, num_stolbets - 1)
        if array_game[a][b] != 'X' \
                and array_game[a][b] != 'O':
            array_game[a][b] = sign_of_computer
            c = False
        else:
            continue


# проверка победы
def who_wins(symbol):
    # проверка по столбцу
    for j in range(num_stolbets):
        count_symbol = 0
        for i in range(num_strok):
            if array_game[i][j] == symbol:
                count_symbol += 1
                if count_symbol == count_pobeda:
                    return True
            else:
                count_symbol = 0

    # проверка по строке
    for i in range(num_strok):
        count_symbol = 0
        for j in range(num_stolbets):
            if array_game[i][j] == symbol:
                count_symbol += 1
                if count_symbol == count_pobeda:
                    return True
            else:
                count_symbol = 0

    # главная диагональ
    for line in range(num_strok - count_pobeda + 1):
        for k in range(num_stolbets - count_pobeda + 1):
            count_symbol1 = 0
            count_symbol2 = 0
            for i in range(num_strok - line):
                if i + k == num_stolbets:
                    break
                else:
                    if array_game[line + i][i + k] == symbol:
                        count_symbol1 += 1
                        if count_symbol1 == count_pobeda:
                            return True
                    else:
                        count_symbol1 = 0
    # побочная диагональ
                    if array_game[line + i][num_stolbets - i - k - 1] == symbol:
                        count_symbol2 += 1
                        if count_symbol2 == count_pobeda:
                            return True
                    else:
                        count_symbol2 = 0
    return False

# ничья
def tie(array_game):
    count_symbol = 0
    count_tie = num_strok * num_stolbets
    for i in range(num_strok):
        for j in range(num_stolbets):
            if array_game[i][j] == 'X' or array_game[i][j] == 'O':
                count_symbol += 1
                if count_symbol == count_tie:
                    return True
    return False

def save_moment():
    # остановка игры и сохранение
    import sys
    continue_game = input('Хотите сохранить текущее состояние игры?(+/-)? ')
    while continue_game != '+' and continue_game != '-':
        continue_game = input('Хотите сохранить текущее состояние игры?(+/-)? ')
    if continue_game == '+':
        with open("savegam", "rb") as f:
            num_strok_dict = pickle.load(f)
            num_stolbets_dict = pickle.load(f)
            count_pobeda_dict = pickle.load(f)
            up_me_dict = pickle.load(f)
            sign_of_user_dict = pickle.load(f)
            sign_of_computer_dict = pickle.load(f)
            array_game_dict = pickle.load(f)
        num_strok_dict.update({str(name): num_strok})
        num_stolbets_dict.update({str(name): num_stolbets})
        count_pobeda_dict.update({str(name): count_pobeda})
        up_me_dict.update({str(name): up_me})
        sign_of_user_dict.update({str(name): sign_of_user})
        sign_of_computer_dict.update({str(name): sign_of_computer})
        array_game_dict.update({str(name): array_game})
        with open("savegam", "wb") as f:
            pickle.dump(num_strok_dict, f)
            pickle.dump(num_stolbets_dict, f)
            pickle.dump(count_pobeda_dict, f)
            pickle.dump(up_me_dict, f)
            pickle.dump(sign_of_user_dict, f)
            pickle.dump(sign_of_computer_dict, f)
            pickle.dump(array_game_dict, f)
            print('Будьте убеждены, ваши данные сохранены!')
            sys.exit()
    else:
        print('Будет приятно встретиться с вами вновь!')
        sys.exit()

# сохранение настроек поля
def save_me():
    save_me = input('Хотите сохранить настройки поля(+/-)? ')
    while save_me != '+' and save_me != '-':
        save_me = input('Хотите настройки поля(+/-)? ')

    # сохраняет номер строки, столбца и количество символов для победы:
    if save_me == '+':
        with open("saveever", "rb") as f:
            num_strok_dict = pickle.load(f)
            num_stolbets_dict = pickle.load(f)
            count_pobeda_dict = pickle.load(f)
        num_strok_dict.update({str(name): num_strok})
        num_stolbets_dict.update({str(name): num_stolbets})
        count_pobeda_dict.update({str(name): count_pobeda})
        with open("saveever", "wb") as f:
            pickle.dump(num_strok_dict, f)
            pickle.dump(num_stolbets_dict, f)
            pickle.dump(count_pobeda_dict, f)

# сохраняет результаты
def save_res():
    if up_me == '+':
        games = 0
        wins = 0
        lose = 0
        tie = 0
        with open('saveres', 'rb') as f:
            games_dict = pickle.load(f)
            wins_dict = pickle.load(f)
            lose_dict = pickle.load(f)
            tie_dict = pickle.load(f)
    else:
        with open('saveres', 'rb') as f:
            games_dict = pickle.load(f)
            wins_dict = pickle.load(f)
            lose_dict = pickle.load(f)
            tie_dict = pickle.load(f)
            games = games_dict[str(name)]
            wins = wins_dict[str(name)]
            lose = lose_dict[str(name)]
            tie = tie_dict[str(name)]
    if who_wins(sign_of_user):
        wins += 1
        games += 1
    elif who_wins(sign_of_computer):
        lose += 1
        games += 1
    else:
        tie += 1
        games += 1
    games_dict.update({str(name): games})
    wins_dict.update({str(name): wins})
    lose_dict.update({str(name): lose})
    tie_dict.update({str(name): tie})
    with open("saveres", "wb") as f:
        pickle.dump(games_dict, f)
        pickle.dump(wins_dict, f)
        pickle.dump(lose_dict, f)
        pickle.dump(tie_dict, f)

# очистка словаря если сохраенная игра была завершена
def del_moment():
    if wanna_continue == '+':
        with open("savegam", "rb") as f:
            num_strok_dict = pickle.load(f)
            num_stolbets_dict = pickle.load(f)
            count_pobeda_dict = pickle.load(f)
            up_me_dict = pickle.load(f)
            sign_of_user_dict = pickle.load(f)
            sign_of_computer_dict = pickle.load(f)
            array_game_dict = pickle.load(f)
            del num_strok_dict[name]
            del num_stolbets_dict[name]
            del count_pobeda_dict[name]
            del up_me_dict[name]
            del sign_of_user_dict[name]
            del sign_of_computer_dict[name]
            del array_game_dict[name]
        with open("savegam", "wb") as f:
            pickle.dump(num_strok_dict, f)
            pickle.dump(num_stolbets_dict, f)
            pickle.dump(count_pobeda_dict, f)
            pickle.dump(up_me_dict, f)
            pickle.dump(sign_of_user_dict, f)
            pickle.dump(sign_of_computer_dict, f)
            pickle.dump(array_game_dict, f)

# игра
def main():
    sign_in()
    if up_me == '-' or wanna_continue == '+':
        instruct = input('Хотите просмотреть руководство по игре еще раз(+/-)? ')
        while instruct != '+' and instruct != '-':
            instruct = input('Хотите просмотреть руководство по игре еще раз(+/-)? ')
        if instruct == '+':
            display_instruct(array_game)
            input('Нажмите любую клавишу, чтобы продолжить...')
        else:
            board(array_game)
    else:
        display_instruct(array_game)
        input('Нажмите любую клавишу, чтобы продолжить...')

    # определять кто ходит первый, если это не сохраненная игра
    if wanna_continue != '+':
        who_goes_first()
        if_comp_first(array_game)
    while True:
        if sign_of_user == 'X':
            move_of_user(array_game)
            board(array_game)
            if who_wins(sign_of_user):
                print('Ваша взяла!')
                break
            if tie(array_game):
                print('Ничья!')
                break
            move_of_computer(array_game)
            board(array_game)
            if who_wins(sign_of_computer):
                print('Победу одержал ИИ!')
                break
            if tie(array_game):
                print('tie')
                break
        else:
            if who_wins(sign_of_computer):
                print('Победу одержал ИИ!')
                break
            move_of_user(array_game)
            board(array_game)
            if who_wins(sign_of_user):
                print('Ваша взяла!')
                break
            if tie(array_game):
                print('Ничья!')
                break
            move_of_computer(array_game)
            board(array_game)
            if who_wins(sign_of_computer):
                print('Победу одержал ИИ!')
                break
            if tie(array_game):
                print('Ничья!')
                break


    # удаляет законченную сохраненную игру из словаря
    if wanna_continue == '+':
        del_moment()

    # сохраняет статистику игр
    save_res()

    # сохраняет новые настройки поля пользователя
    if down_me != '+':
        save_me()

    # запрос на просмотр статистики игры
    wanna_view = input('Хотите посмотреть статистику игры(+/-)? ')
    while wanna_view != '+' and wanna_view != '-':
        wanna_view = input('Хотите посмотреть статистику игры(+/-)? ')
    if wanna_view == '+':
        with open('saveres', 'rb') as f:
            games_dict = pickle.load(f)
            wins_dict = pickle.load(f)
            lose_dict = pickle.load(f)
            tie_dict = pickle.load(f)
        a = [(k, games_dict[k]) for k in sorted(games_dict, key=games_dict.get, reverse=True)]
        b = [(k, wins_dict[k]) for k in sorted(wins_dict, key=wins_dict.get, reverse=True)]
        c = [(k, lose_dict[k]) for k in sorted(lose_dict, key=lose_dict.get, reverse=True)]
        d = [(k, tie_dict[k]) for k in sorted(tie_dict, key=tie_dict.get, reverse=True)]
        a = dict(a)
        print('Количество игр:')
        for key, value in a.items():
            print(key, '->', value, ' ', end='')
        b = dict(b)
        print('\nПобеды:')
        for key, value in b.items():
            print(key, '->', value, ' ', end='')
        c = dict(c)
        print('\nПоражения:')
        for key, value in c.items():
            print(key, '->', value, ' ', end='')
        d = dict(d)
        print('\nНичьи:')
        for key, value in d.items():
            print(key, '->', value, ' ', end='')
        print('\nСпасибо за игру, приходите еще!')
        input()
    if wanna_view == '-':
        print('Спасибо за игру, приходите еще!')
        input()
main()
