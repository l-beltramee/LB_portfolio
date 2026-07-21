# Tic Tac Toe

## How to Play
1. The board will be displayed with numbers 1 to 9 representing each position
2. Enter the number of the position where you want to place your X
3. The computer will make its move automatically
4. The game continues until someone wins or it's a draw

### Board Positions
```
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
```

## How to Run

### Requirements
- Python 3.x installed on your computer

### Steps

1. Clone the repository:
```bash
git clone https://github.com/l-beltramee/LB_portfolio.git
```

2. Navigate to the game folder:
```bash
cd LB_portfolio/Jogos
```

3. Run the game:
```bash
python jogo_da_velha.py
```

## Game Example

```
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]

Enter position: 5
[1, 2, 3]
[4, 'X', 6]
[7, 8, 9]

(Computer plays...)
```

## Features

- Computer plays randomly
- Victory check (rows, columns and diagonals)
- Draw detection

## Future Improvements

- Smarter AI for the computer
- Graphical interface
- Score tracking

## Author

Created by Luccas Beltrame
