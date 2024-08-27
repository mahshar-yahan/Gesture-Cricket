# FingerMatch Cricket: A Gesture-Based Game

FingerMatch Cricket is an interactive game that leverages hand gestures to simulate a cricket match. Using MediaPipe, the game detects the number of fingers shown by the player. The objective is simple: if the player and the computer display the same number of fingers, the player is out. Otherwise, the player's run count increases.

## Project Overview

In this project, we utilize the MediaPipe library to recognize hand gestures, specifically the number of fingers shown by the player. The game follows basic cricket rules, modified for a quick and engaging experience using gesture recognition.

### Key Features
- **Gesture Recognition:** Detects the number of fingers displayed by the player using MediaPipe.
- **Game Logic:** Simple and intuitive cricket rules where matching fingers result in an out, and non-matching fingers add to the player's run total.
- **Interactive Gameplay:** Provides real-time feedback based on the player's hand gestures.

## Getting Started

### Prerequisites
- Python 3.x
- MediaPipe
- OpenCV (for camera input)

### Installation
Clone the repository:
```bash
git clone https://github.com/mahshar-yahan/Gesture-Cricket.git
cd fingermatch-cricket
