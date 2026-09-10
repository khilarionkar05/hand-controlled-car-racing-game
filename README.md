# 🏎️ Hand-Controlled Car Racing Game

> A real-time car racing game controlled using hand gestures through a webcam.

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?logo=opencv)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Hand%20Tracking-orange)
![Pygame](https://img.shields.io/badge/Pygame--CE-Game%20Development-yellow?logo=pygame)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)

---

## 📌 Project Overview

**Hand-Controlled Car Racing Game** is a real-time interactive racing game developed using **Python, OpenCV, MediaPipe, and Pygame-CE**.

The game uses a webcam to detect the player's hand in real time. Hand movement is converted into game controls, allowing the player to control the car without using a traditional keyboard or game controller.

The project demonstrates the integration of **Computer Vision, Hand Tracking, Gesture Recognition, and Game Development** in a single interactive application.

---

## 🎮 Features

- ✋ Real-time hand tracking
- 📷 Webcam-based interaction
- 🚗 Hand-controlled car steering
- ⬅️ Move hand left → Car moves left
- ➡️ Move hand right → Car moves right
- ⬆️ Move hand up → Accelerate
- ⬇️ Move hand down → Brake
- ✊ Fist gesture → Pause
- 🖐️ Open hand → Resume
- 🚧 Random road obstacle generation
- 💥 Collision detection
- 🏆 Dynamic score system
- ⚡ Dynamic game speed
- 🛣️ Scrolling racing road
- 📺 Live hand-tracking camera preview
- 🎯 Smooth hand movement control
- 🖥️ Interactive game interface

---

## 🧠 How It Works

The project uses the following real-time processing pipeline:

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
       │   Steering   │          │ Speed Control│
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
