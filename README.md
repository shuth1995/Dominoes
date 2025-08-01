# 🎲 Dominoes Game (Python)

This project implements a text-based version of the classic **Dominoes game**, where a human player competes against an AI computer opponent. The game logic is fully contained in `dominoes.py`, with clear rules, a turn-based structure, and simple terminal-based interaction.

---

## 🕹️ How to Play

- You are dealt a hand of 7 dominos, and the computer gets 7 as well.
- A double (like `[6, 6]`) starts the game.
- On your turn, type the number corresponding to the domino you want to play:
  - Use a **positive number** to place a domino on the **right** end.
  - Use a **negative number** to place it on the **left** end.
  - Enter `0` to draw a domino from the stock if you have no legal moves.
- The game continues until:
  - One player runs out of dominos → they win.
  - Neither player can move and the stock is empty → it’s a draw.
  - A number appears 8 times and is on both ends → it’s a draw.

---

## 🔧 Features

-	Full domino set generation (28 unique pieces)
- Player and computer hands with valid double starts
-	Dynamic domino snake display with ellipsis shortening
-	Turn-based logic with error handling
-	AI logic based on frequency scoring
-	Win, lose, and draw conditions

## 📂 File Structure
```
dominoes/
├── dominoes.py       # Main game script
├── README.md         # Project documentation
└── requirements.txt  # Environment dependencies
```

---

### Run the Game

```bash
python dominoes.py
