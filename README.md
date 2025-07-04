# 🁢 Interactive Domino Game (Python)
---

This project is a terminal-based interactive Domino game that simulates a match between a human player and a computer opponent. It showcases core programming concepts such as game loops, input validation, and basic AI logic.

### 🎮 Game Overview

The game uses the full set of 28 unique domino pieces. These are randomly distributed as follows: player - 7 pieces; computer - 7 pieces; stock (pile) - 14 pieces. The player with the highest double automatically places it to start the domino snake. The opposing player makes the first move.

### 📟 Game Display

The current number of stock, computer pieces and user pieces is displayed each turn. The domino snake is shown throughout. If the snake grows beyond 6 dominos, only the first 3 and last 3 pieces are displayed (with ... in the middle for clarity). Press Enter when prompted to let the computer take its turn.

<img width="566" alt="Screenshot 2025-07-04 at 16 05 24" src="https://github.com/user-attachments/assets/6aed3da2-57d9-4417-a637-cfd9180198e6" />


### 🔢 How to Play

To play a domino, enter the number corresponding to its position in your hand. To place a domino on the left side of the snake, prefix your input with a minus sign (e.g. -2). To place it on the right, enter the number without a prefix (e.g. 2). A move is only valid if the chosen domino shares a number with either end of the domino snake. If necessary, it will be automatically flipped to fit. If no valid move is possible, enter 0 to draw a piece from the stock (if available). If the stock is empty, you’ll simply skip your turn.

<img width="560" alt="Screenshot 2025-07-04 at 16 06 08" src="https://github.com/user-attachments/assets/9cd45bc6-1c58-4ec3-9a73-b907750e2301" />


### ⚠️ Input Validation

Invalid inputs (e.g. out-of-range index, non-integer values) will display an error message. You’ll be prompted to enter a new value until a valid move is made.

<img width="561" alt="Screenshot 2025-07-04 at 16 06 40" src="https://github.com/user-attachments/assets/d35fa5a2-2be7-495c-bac5-aa3675146af2" />


### 🧠 Computer AI Logic

The computer plays strategically. It evaluates its dominos based on the frequency of numbers in the domino snake and its own hand. Dominos containing more common numbers get higher scores. The computer plays the highest-scoring valid domino available. If none are valid, it draws from the stock or skips the turn.

### 🏁 Game End Conditions

The game ends when either player runs out of dominos (that player wins), neither player can make a move and the stock is empty (draw), or the numbers at both ends of the snake are the same and that number appears 8 times or more in the snake (draw due to stalemate).

<img width="560" alt="Screenshot 2025-07-04 at 16 08 35" src="https://github.com/user-attachments/assets/046fc3c1-a45c-4ec1-9490-f9f5668da66c" />
