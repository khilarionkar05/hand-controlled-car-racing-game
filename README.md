# 🏎️ Hand-Controlled Car Racing Game

> A real-time car racing game controlled using hand gestures through a webcam.

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?logo=opencv)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Hand%20Tracking-orange)
![Pygame](https://img.shields.io/badge/Pygame--CE-2.5.8-yellow)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)
![License](https://img.shields.io/badge/License-Educational-lightgrey)

---

# 📌 About The Project

**Hand-Controlled Car Racing Game** is a real-time interactive racing game developed using:

- 🐍 Python
- 👁️ OpenCV
- ✋ MediaPipe
- 🎮 Pygame-CE

The game uses a webcam to detect the player's hand and converts hand movements into game controls.

The player can control the racing car without using a traditional game controller.

Hand movement controls:

- Car steering
- Acceleration
- Braking

Hand gestures control:

- Pause
- Resume

The game also includes:

- Road obstacles
- Collision detection
- Score system
- Speed system
- Scrolling road
- Live hand-tracking preview
- Interactive game interface

---

# 🎮 Features

- ✋ Real-time hand tracking
- 📷 Webcam-based control
- 🚗 Hand-controlled car
- ⬅️ Left-hand movement → Car moves left
- ➡️ Right-hand movement → Car moves right
- ⬆️ Hand up → Accelerate
- ⬇️ Hand down → Brake
- ✊ Fist → Pause
- 🖐️ Open hand → Resume
- 🚧 Random obstacles
- 💥 Collision detection
- 🏆 Score system
- ⚡ Dynamic speed
- 🛣️ Scrolling road
- 📺 Live camera preview
- 🎯 Smooth hand movement
- 🖥️ Pygame interface

---

# 🧠 How The Project Works

The project uses the following processing pipeline:

```text
                    ┌──────────────┐
                    │    Webcam    │
                    └──────┬───────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ OpenCV Capture  │
                  └────────┬────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ MediaPipe Hand      │
                │ Landmarker          │
                └──────────┬──────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Hand Landmarks  │
                  └────────┬────────┘
                           │
              ┌────────────┴────────────┐
              │                         │
              ▼                         ▼
       ┌──────────────┐          ┌──────────────┐
       │ X Position   │          │ Y Position   │
       └──────┬───────┘          └──────┬───────┘
              │                         │
              ▼                         ▼
       ┌──────────────┐          ┌──────────────┐
       │ Car Steering │          │ Speed Control│
       └──────┬───────┘          └──────┬───────┘
              │                         │
              └────────────┬────────────┘
                           ▼
                    ┌─────────────┐
                    │   Pygame    │
                    │    Game     │
                    └──────┬──────┘
                           │
                ┌──────────┴──────────┐
                │                     │
                ▼                     ▼
          ┌───────────┐        ┌──────────────┐
          │ Obstacles │        │  Collision   │
          └─────┬─────┘        └──────┬───────┘
                │                     │
                └──────────┬──────────┘
                           ▼
                       ┌───────┐
                       │ Score │
                       └───────┘
✋ Hand Controls
Hand Movement / Gesture	Game Action
Move hand left	🚗 Move car left
Move hand right	🚗 Move car right
Move hand up	⚡ Accelerate
Move hand down	🛑 Brake
✊ Fist	⏸️ Pause
🖐️ Open hand	▶️ Resume
⌨️ Keyboard Controls
Key	Action
R	Restart after game over
ESC	Quit the game

The main gameplay is controlled using hand movement.

Keyboard controls are only used for restarting and exiting the game.

🛠️ Technologies Used
Programming Language
Python
Computer Vision
OpenCV
MediaPipe
Game Development
Pygame-CE
Concepts Used
Computer Vision
Hand Tracking
Hand Landmark Detection
Gesture Recognition
Image Processing
Real-Time Processing
Game Loop
Collision Detection
Object Movement
Smooth Control
Interactive UI
📁 Project Structure
hand-controlled-car-racing-game/
│
├── assets/
│   ├── car.png
│   ├── obstacal.png
│   └── road.png
│
├── hand_detection.py
├── hand_landmarker.task
├── main.py
├── README.md
└── .gitignore
📄 Project Files
main.py

The main game program.

It controls:

Pygame initialization
Game window
Game loop
Car movement
Steering
Speed control
Road scrolling
Obstacle generation
Collision detection
Score
Game UI
Camera preview
Pause screen
Game-over screen
hand_detection.py

The hand-control module.

It handles:

Webcam capture
OpenCV image processing
MediaPipe hand detection
Hand landmarks
Palm position
Finger counting
Gesture recognition
Movement smoothing
Hand landmark visualization
hand_landmarker.task

This is the pre-trained MediaPipe Hand Landmarker model.

It is required by the hand detection program.

The program loads this model using:

model_asset_path="hand_landmarker.task"
assets/

Contains the game graphics.

car.png

Player car image.

road.png

Racing road image.

obstacal.png

Road obstacle image.

Note: obstacal.png intentionally uses the existing project filename.

💻 System Requirements
Operating System

The project is designed for:

Windows 10 / Windows 11
Python

Recommended:

Python 3.14.x
Hardware

A computer with:

Webcam
Keyboard
Display
Internet connection for initial installation

A reasonably capable computer is recommended for smooth real-time hand tracking.

📦 Required Python Libraries

The project requires:

pygame-ce
mediapipe
opencv-contrib-python
⚙️ Complete Installation Guide

Follow the steps below if you want to run this project on your own computer.

1️⃣ Install Python

Download and install Python from:

https://www.python.org/downloads/

After installation, check the Python version:

python --version

Example:

Python 3.14.6

Also check pip:

python -m pip --version
2️⃣ Download The Project

There are two ways to get the project.

Method 1 — Clone Using Git

Install Git if it is not already installed:

https://git-scm.com/downloads

Then open Command Prompt or PowerShell.

Run:

git clone https://github.com/YOUR-USERNAME/hand-controlled-car-racing-game.git

Replace:

YOUR-USERNAME

with the GitHub username that owns this repository.

Then enter the project folder:

cd hand-controlled-car-racing-game
3️⃣ Download ZIP Instead

If you don't have Git, you can download the repository as a ZIP file.

On GitHub:

Repository
   ↓
Code
   ↓
Download ZIP

Extract the ZIP file.

Then open the extracted project folder.

Example:

C:\Users\YourName\Desktop\hand-controlled-car-racing-game
4️⃣ Open Terminal In The Project Folder

Open PowerShell or Command Prompt inside the project folder.

You should be inside:

hand-controlled-car-racing-game

Check the files:

dir

You should see:

assets
hand_detection.py
hand_landmarker.task
main.py
README.md
5️⃣ Install Pygame-CE

Run:

python -m pip install pygame-ce
6️⃣ Install MediaPipe

Run:

python -m pip install mediapipe
7️⃣ Install OpenCV

Run:

python -m pip install opencv-contrib-python
8️⃣ Verify The Installation

Run:

python -c "import pygame; print('Pygame:', pygame.version.ver)"

Then:

python -c "import mediapipe as mp; print('MediaPipe:', mp.__version__)"

Then:

python -c "import cv2; print('OpenCV:', cv2.__version__)"

You can also check everything together:

python -c "import pygame, cv2, mediapipe; print('All required libraries are installed successfully!')"
🤖 MediaPipe Model Setup

The project requires:

hand_landmarker.task

Download the MediaPipe Hand Landmarker model from the official MediaPipe model storage:

https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/latest/hand_landmarker.task

Place the downloaded file directly inside the project root folder.

The final structure must be:

hand-controlled-car-racing-game/
│
├── assets/
│   ├── car.png
│   ├── obstacal.png
│   └── road.png
│
├── hand_detection.py
├── hand_landmarker.task
├── main.py
└── README.md
📷 Webcam Setup

The game uses the computer's default webcam.

Before running the game:

Connect your webcam.
Make sure Windows can access it.
Close other applications that are currently using the webcam.
Make sure the camera is positioned so your hand is clearly visible.

The project uses:

cv2.VideoCapture(0)

This normally selects the default webcam.

▶️ Run The Game

After completing the installation, run:

python main.py

The game window should open.

The webcam will start detecting your hand.

Place your hand in front of the webcam.

🎮 How To Play
Step 1

Start the game:

python main.py
Step 2

Show your hand to the webcam.

Step 3

Move your hand horizontally.

LEFT  →  Car Left

RIGHT →  Car Right
Step 4

Move your hand vertically.

UP   → Accelerate

DOWN → Brake
Step 5

Use gestures.

✊ Fist
   ↓
Pause


🖐️ Open Hand
   ↓
Resume
Step 6

Avoid the obstacles and continue driving.

Step 7

Try to achieve the highest score.

🧠 Hand Tracking System

MediaPipe detects the hand and provides hand landmarks.

The project uses palm-related landmarks to calculate the approximate hand position.

The calculated position is then converted into game controls.

Webcam
   ↓
OpenCV
   ↓
MediaPipe
   ↓
Hand Landmarks
   ↓
Palm Position
   ↓
Game Controls
🚗 Steering System

The horizontal hand position controls the car.

Hand Left
    ↓
Car Left


Hand Center
    ↓
Car Center


Hand Right
    ↓
Car Right

The movement is smoothed so that the car does not move suddenly.

⚡ Speed System

The vertical hand position controls the speed.

Hand Up
   ↓
Accelerate


Hand Center
   ↓
Normal Speed


Hand Down
   ↓
Brake

The speed is limited between the configured minimum and maximum values.

✊ Gesture System

The project counts the detected fingers.

Fist
Fist
 ↓
Very few fingers detected
 ↓
Pause
Open Hand
Open Hand
 ↓
Multiple fingers detected
 ↓
Resume

A cooldown is used so that one gesture does not repeatedly trigger an action every frame.

🚧 Obstacle System

Obstacles are randomly generated on the road.

The game continuously:

Generate Obstacle
       ↓
Place Obstacle
       ↓
Move Obstacle
       ↓
Check Collision
       ↓
Remove Old Obstacle

Obstacles can appear across the available road lanes.

💥 Collision Detection

The game uses rectangular collision detection.

The player car has a collision area.

Each obstacle has a collision area.

The game checks whether these areas overlap.

Car
 +
Obstacle
 ↓
Collision
 ↓
Game Over
🏆 Score System

The score increases while the player is driving.

The score is displayed in the game interface.

The current speed is also displayed.

The objective is to survive as long as possible and achieve a high score.

🖥️ Game Interface

The game interface contains:

Score
Speed
Car
Racing road
Obstacles
Hand-tracking preview
Hand-control instructions
Pause screen
Game-over screen
🔄 Complete Project Workflow
             START
               │
               ▼
        Start Python Program
               │
               ▼
          Open Webcam
               │
               ▼
       Capture Camera Frame
               │
               ▼
       Detect Hand With
          MediaPipe
               │
               ▼
        Get Hand Landmarks
               │
        ┌──────┴──────┐
        │             │
        ▼             ▼
   X Position     Y Position
        │             │
        ▼             ▼
    Steering      Speed Control
        │             │
        └──────┬──────┘
               │
               ▼
          Gesture Check
               │
               ▼
        Update Pygame Game
               │
               ▼
       Generate Obstacles
               │
               ▼
       Check Collision
               │
          ┌────┴────┐
          │         │
          ▼         ▼
       No Hit      Hit
          │         │
          ▼         ▼
       Continue   Game Over
          │
          ▼
        Increase Score
          │
          ▼
         Repeat
🧪 Testing

After installation, test each component separately if necessary.

Test Python
python --version
Test Pygame
python -c "import pygame; print('Pygame OK')"
Test OpenCV
python -c "import cv2; print('OpenCV OK')"
Test MediaPipe
python -c "import mediapipe; print('MediaPipe OK')"
Test Everything
python -c "import pygame, cv2, mediapipe; print('ALL SYSTEMS OK')"

Then start the game:

python main.py
❗ Troubleshooting
Camera Is Not Working

Make sure:

Webcam is connected.
Windows has camera permission.
No other application is using the camera.
The correct camera is selected.

The default camera is:

cv2.VideoCapture(0)

If your computer has multiple cameras, the camera index may need to be changed.

ModuleNotFoundError

Example:

ModuleNotFoundError: No module named 'pygame'

Install the missing library:

python -m pip install pygame-ce

For MediaPipe:

python -m pip install mediapipe

For OpenCV:

python -m pip install opencv-contrib-python
hand_landmarker.task Not Found

If you see an error related to:

hand_landmarker.task

make sure the file is directly inside the project folder:

hand-controlled-car-racing-game/
│
├── hand_landmarker.task
├── main.py
└── hand_detection.py

Do not put it inside the assets folder unless the code path is changed accordingly.

Pygame Installation Problem

The project uses:

pygame-ce

Install it using:

python -m pip install pygame-ce

The Python code still imports:

import pygame
Game Is Running Slowly

Try:

Closing unnecessary applications.
Improving room lighting.
Keeping your hand clearly visible.
Moving the webcam closer.
Using a stable webcam position.
📸 Project Preview

Add your project screenshot to:

assets/game-preview.png

Then add:

![Hand Controlled Car Racing Game](assets/game-preview.png)
🎥 Project Demo

A demonstration video can be shared through LinkedIn or another video platform.

Example:

Demo Video:
Add your video link here
🚀 Future Improvements

Possible future improvements include:

🏁 Multiple racing levels
📈 Progressive difficulty
🚗 Multiple cars
🚧 More obstacle types
🎵 Sound effects
🎶 Background music
🏆 High-score saving
🔥 Nitro boost gesture
✋ Advanced gesture recognition
🤲 Two-hand control
🎮 Gesture-based restart
🏆 Online leaderboard
📊 Game statistics
🎨 Improved UI
🌐 Multiplayer mode
📚 Learning Outcomes

This project provided practical experience with:

Python programming
Computer Vision
OpenCV
MediaPipe
Hand Tracking
Hand Landmark Detection
Gesture Recognition
Webcam Processing
Real-Time Image Processing
Pygame
Game Development
Collision Detection
Game Loops
Interactive UI
Real-Time Control
🎯 Project Objective

The main objective of this project is to demonstrate how Computer Vision can be used as an alternative input method for interactive applications.

The webcam acts as the input device, MediaPipe processes the hand, and Pygame converts the detected movement and gestures into game actions.

👨‍💻 Author
Onkar Khilari

Computer Science / AI-ML enthusiast interested in:

Artificial Intelligence
Machine Learning
Computer Vision
Python
Robotics
Interactive Applications
Software Development
🎓 Acknowledgement

Special thanks to:

Sandip University

and

PHN Technology Pvt Ltd

for the learning environment and opportunities that encourage practical technology projects.

🔗 Connect
GitHub
https://github.com/YOUR-USERNAME
LinkedIn
https://www.linkedin.com/in/YOUR-LINKEDIN-USERNAME/

Replace the above placeholders with your actual profile links.

⭐ Support

If you like this project, please consider giving the repository a ⭐ Star.

Your feedback, suggestions and contributions are welcome.

📜 License

This project is created for educational and learning purposes.

You are welcome to study and modify the project for educational use.


### One important change I recommend

For someone else to **actually run your project easily**, your GitHub repository should contain these files:

```text
hand-controlled-car-racing-game/
│
├── assets/
│   ├── car.png
│   ├── obstacal.png
│   ├── road.png
│   └── game-preview.png
│
├── hand_detection.py
├── hand_landmarker.task
├── main.py
├── README.md
└── .gitignore