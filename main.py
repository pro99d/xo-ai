import math
score_x = -10000
score_y = 100
score_nul = -10
x_ai = False
y_ai = False
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n\n")

def check_winner(board):
    # Проверка строк
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]

    # Проверка столбцов
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    # Проверка диагоналей
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "X":
        return score_x + depth  # Если X выиграл
    elif winner == "O":
        return score_y - depth  # Если O выиграл
    elif is_board_full(board):
        return score_nul  # Ничья

    if is_maximizing:
        best_score = -math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "O"  # Ход компьютера
                    score = minimax(board, depth + 1, False)
                    board[row][col] = " "  # Отмена хода
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "X"  # Ход игрока
                    score = minimax(board, depth + 1, True)
                    board[row][col] = " "  # Отмена хода
                    best_score = min(score, best_score)
        return best_score
def find_best_move(board):
    best_score = -math.inf
    move = (-1, -1)
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = "O"  # Ход компьютера
                score = minimax(board, 3, False)
                board[row][col] = " "  # Отмена хода
                if score > best_score:
                    best_score = score
                    move = (row, col)
    return move

def main():
    x_ai = bool(input("компьютер за X?\n"))
    y_ai = bool(input("компьютер за O?\n"))
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        if current_player == "X":
            if x_ai:
                print("Ход компьютера:")
                row, col = find_best_move(board)
            else:
                row = int(input(f"Игрок {current_player}, введите номер строки (0-2): "))
                col = int(input(f"Игрок {current_player}, введите номер столбца (0-2): "))
        else:
            if y_ai:
                print("Ход компьютера:")
                row, col = find_best_move(board)
            else:
                row = int(input(f"Игрок {current_player}, введите номер строки (0-2): "))
                col = int(input(f"Игрок {current_player}, введите номер столбца (0-2): "))

        if board[row][col] != " ":
            print("Эта клетка уже занята! Попробуйте снова.")
            continue

        board[row][col] = current_player

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Игрок {winner} выиграл!")
            break

        if is_board_full(board):
            print_board(board)
            print("Ничья!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()

