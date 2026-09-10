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