field = [['-' for j in range(3)] for i in range(3)]
ask, check_x, check_y, win, draw = 0, 0, 0, 0, 0
possible_moves = ['1', '2', '3']
player1 = 'Крестик'
player2 = 'Нолик'


def col_row_print():
    print('  1 2 3')
    for i in range(len(field)):  # функция принта актуального поля
        print(i + 1, *field[i], end='\n')


def check_line(sym):          # функция проверки на выигрыш по строкам
    c_x = 0
    for i in range(3):
        if c_x != 3:
            for j in field[i]:
                if j == sym:
                    c_x += 1
                else:
                    c_x = 0
                    break
    return (c_x == 3) or False


def check_coll(sym):          # функция проверки на выигрыш по столбцам
    c_y = 0
    for i in range(3):
        for j in range(3):
            if field[j][i] == sym:
                c_y += 1
            else:
                c_y = 0
                break
        if c_y == 3:
            break
    return (c_y == 3) or False


def check_diag(sym):          # функция проверки на выигрыш по диагоналям
    c_z = 0
    for i in range(3):
        for j in field[i][i]:
            if j == sym:
                c_z += 1
            else:
                c_z = 0
                break
    if c_z != 3:
        if field[0][2] == sym and field[1][1] == sym and field[2][0] == sym:
            c_z = 3
    return (c_z == 3) or False


def check_status_x():           # общая функция проверки для X
    if check_line('x') or check_coll('x') or check_diag('x'):
        return f'Победил {player1}!'
    else:
        return False


def check_status_o():           # общая функция проверки для O
    if check_line('o') or check_coll('o') or check_diag('o'):
        return f'Победил {player2}!'
    else:
        return False


while ask != 'out':             # основной код игры
    print('_____ Крестики-нолики ____', '______ Главное меню ______', sep='\n')
    print('Чтобы изменить имена игроков, введите "name"', 'Чтобы выйти из игры, введите "out"',
          'Чтобы начать новую игру введите любой символ или нажмите Enter ', sep='\n')
    ask = input()
    if ask == 'name':
        player1 = input('Введите имя игрока, играющего за Х или нажмите Enter для имени по умолчанию: ')
        player2 = input('Введите имя игрока, играющего за O или нажмите Enter для имени по умолчанию: ')
        if player1 == '' or player2 == '':
            player1, player2 = 'Крестик', 'Нолик'
            continue
        continue
    if ask != 'out':
        win = 0
        draw = 0
        field = [['-' for j in range(3)] for i in range(3)]
        col_row_print()
        while win != 1:
            check_x = 0
            check_y = 0
            while check_x != 1:
                if win != 1:
                    x = input('Ходит X - введите через пробел номер строки и номер столбца: ').split()
                    if len(x) != 2 or x == '':
                        col_row_print()
                        print('_!_ Введите корректные значения _!_')
                        continue
                    elif x[0] not in possible_moves or x[1] not in possible_moves:
                        col_row_print()
                        print('_!_ Введите корректные значения _!_')
                        continue
                    elif field[int(x[0]) - 1][int(x[1]) - 1] == 'o':
                        col_row_print()
                        print('_!_ Вы  не можете сюда сходить, соперник вас опередил, повторите попытку _!_')
                        field[int(x[0]) - 1][int(x[1]) - 1] = 'o'
                        continue
                    elif field[int(x[0]) - 1][int(x[1]) - 1] == 'x':
                        col_row_print()
                        print('_!_ Вы не можете ходить два раза в одно и то же место, повторите попытку _!_')
                        field[int(x[0]) - 1][int(x[1]) - 1] = 'x'
                        continue
                    field[int(x[0]) - 1][int(x[1]) - 1] = 'x'
                    draw += 1
                    col_row_print()
                    if check_status_x():
                        win = 1
                        print(check_status_x())
                        break
                    elif draw >= 9:
                        print('Ничья!')
                        win = 1
                        break
                    else:
                        check_x = 1
                else:
                    break
            while check_y != 1:
                if win != 1:
                    x = input('Ходит О - введите через пробел номер строки и номер столбца: ').split()
                    if len(x) != 2 or x == '':
                        col_row_print()
                        print('_!_ Введите корректные значения _!_')
                        continue
                    elif x[0] not in possible_moves or x[1] not in possible_moves:
                        col_row_print()
                        print('_!_ Введите корректные значения _!_')
                        continue
                    elif field[int(x[0]) - 1][int(x[1]) - 1] == 'x':
                        col_row_print()
                        print('_!_ Вы  не можете сюда сходить, соперник вас опередил, повторите попытку _!_')
                        field[int(x[0]) - 1][int(x[1]) - 1] = 'x'
                        continue
                    elif field[int(x[0]) - 1][int(x[1]) - 1] == 'o':
                        col_row_print()
                        print('_!_ Вы не можете ходить два раза в одно и то же место, повторите попытку _!_')
                        field[int(x[0]) - 1][int(x[1]) - 1] = 'o'
                        continue
                    field[int(x[0]) - 1][int(x[1]) - 1] = 'o'
                    draw += 1
                    col_row_print()
                    if check_status_o():
                        print(check_status_o())
                        win = 1
                        break
                    elif draw >= 9:
                        print('Ничья!')
                        win = 1
                        break
                    else:
                        check_y = 1
                else:
                    break
    else:
        print('Пока-пока!')
        break
