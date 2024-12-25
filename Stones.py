

board = [3, 4, 5, 6, 6]
user_number = 1
while True:
    print("Текущая позиция")
    print(board)
    print(f'Ход игрока {user_number}')
    poz = int(input("Откуда берем? ")) - 1
    kol_vo = int(input("Сколько берем? "))
    if board[int(poz)] < kol_vo:
        print("Столько нет, не жадничай")
        poz = int(input("Откуда берем? ")) - 1
        kol_vo = int(input("Сколько берем? "))
        if board[int(poz)] < kol_vo:
            print("Опять??? Пропусти ход подумай")
        else:
            board[int(poz)] -= int(kol_vo)
    else:
        board[int(poz)] -= int(kol_vo)

    if user_number == 1:
        user_number += 1
    else:
        user_number = 1
    print()
    if all([i==0 for i in board]):
        break
print("Вы победили")