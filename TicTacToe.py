# define the board
board = [[' ' for _ in range(3)] for _ in range(3)]

# define the players
players = ['X', 'O']

# define the current player
player_turn = 0

def draw_board():
  print('  0 1 2')
  for i, row in enumerate(board):
    print(i, row)

def get_move():
  while True:
    try:
      row = int(input('Enter row: '))
      col = int(input('Enter column: '))
      if board[row][col] == ' ':
        return row, col
      else:
        print('That spot is already taken. Try again.')
    except (ValueError, IndexError):
      print('Invalid input. Try again.')

def make_move(row, col):
  board[row][col] = players[player_turn]

def has_won(player):
  # check rows
  for row in board:
    if row == [player, player, player]:
      return True
  # check columns
  for col in range(3):
    if board[0][col] == player and board[1][col] == player and board[2][col] == player:
      return True
  # check diagonals
  if board[0][0] == player and board[1][1] == player and board[2][2] == player:
    return True
  if board[0][2] == player and board[1][1] == player and board[2][0] == player:
    return True
  return False

while True:
  draw_board()
  row, col = get_move()
  make_move(row, col)
  if has_won(players[player_turn]):
    print(f'Player {players[player_turn]} has won!')
    break
  player_turn = (player_turn + 1) % 2
