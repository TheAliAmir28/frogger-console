# 🐸 Frogger - Console Edition

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen.svg)

## 📌 Overview
This is a **text-based Python implementation** of the classic **Frogger** arcade game.  
Your mission: **Guide the frog safely across traffic** without colliding with moving obstacles.  
The game uses `.frog` configuration files to define different game maps, speeds, and difficulty levels.

---

## 🎮 How to Play
- Use **W A S D** to move:
  - `W` → Up
  - `A` → Left
  - `S` → Down
  - `D` → Right
- Use **J** to **jump** to a specified row & column (limited number of jumps per game).
- Avoid obstacles (`X`) and reach the opposite side to win.
- Colliding with a car ends the game.

---

## 🗂️ Game Files
The game includes preset `.frog` map files:
- `game1.frog` → Beginner
- `game2.frog` → Intermediate
- `game3.frog` → Expert  

Each `.frog` file defines:
1. **Grid size** (rows, columns)
2. **Number of jumps allowed**
3. **Speeds** for each row (positive = right, negative = left)
4. **Obstacle layout**

---

## 📂 Project Structure
```
frogger.py        # Main game code
game1.frog        # Beginner map configuration
game2.frog        # Intermediate map configuration
game3.frog        # Expert map configuration
```

---

## 🛠️ Installation & Setup
1. **Clone this repository**
   ```bash
   git clone https://github.com/<your-username>/frogger-console.git
   cd frogger-console
   ```

2. **Run the game**
   ```bash
   python3 frogger.py
   ```

---

## 📖 Example Gameplay
```plaintext
[1]    game1.frog
[2]    game2.frog
[3]    game3.frog
Enter an option or filename: 1
1
🐸
X   X X
  X X
...
WASDJ >> w
```

---

## ⚙️ Requirements
- Python **3.x**
- No external libraries required

---

## 📜 License
This project is licensed under the **MIT License** — free to use, modify, and share.

---

## 👨‍💻 Author
**Ali Amir**  
📧 codepirate2028@gmail.com
