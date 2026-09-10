# 🏎️ Hand-Controlled Car Racing Game

> A real-time car racing game controlled using hand gestures through a webcam.

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?logo=opencv)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Hand%20Tracking-orange)
![Pygame-CE](https://img.shields.io/badge/Pygame--CE-Game%20Development-yellow)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)
![License](https://img.shields.io/badge/License-MIT-blue)

## 📌 About The Project

Hand-Controlled Car Racing Game is a real-time interactive game built with Python, OpenCV, MediaPipe, and Pygame-CE. The webcam detects the player's hand, MediaPipe extracts hand landmarks, and the game converts hand position and finger count into steering, speed, pause, and resume controls.

The game includes road obstacles, collision detection, a score system, adjustable speed, a scrolling road, live hand-tracking preview, movement smoothing, and an interactive game interface.

## 🎮 Features

- Real-time webcam hand tracking
- Left and right steering from horizontal hand position
- Acceleration and braking from vertical hand position
- Fist pause and open-hand resume gestures
- Smooth steering and hand movement
- Three-lane obstacle placement
- Scrolling road and moving obstacles
- Collision detection and game-over state
- Score and speed display
- Live camera preview with landmarks
- Keyboard restart and quit controls

## 🧠 How The Project Works

OpenCV captures and mirrors a webcam frame, then converts it to RGB. MediaPipe processes the frame and returns hand landmarks. The averaged palm position is smoothed before its horizontal coordinate controls the car and its vertical coordinate controls speed. Pygame updates and renders the game each frame.

## 🏗️ Processing Pipeline / Architecture Diagram

```text
Webcam
   ↓
OpenCV Capture and Frame Flip
   ↓
MediaPipe Hand Landmarker
   ↓
Hand Landmarks and Finger Count
   ↓
Palm X/Y Position with Smoothing
   ├── X Position → Steering
   ├── Y Position → Speed
   └── Finger Count → Pause / Resume
             ↓
       Pygame Game Loop
             ↓
Road Scrolling + Obstacles + Collision Detection
             ↓
        Score and Game UI
```

Detailed workflow:

```text
Capture frame → Detect hand → Calculate palm center → Smooth coordinates
       → Update car and speed → Move road and obstacles → Test collision
       → Update score → Draw game and preview → Display frame
```

## ✋ Hand Controls

| Hand movement or gesture | Game action |
| --- | --- |
| Hand left | Move the car left |
| Hand center horizontally | Keep the car near the corresponding road position |
| Hand right | Move the car right |
| Hand up | Accelerate |
| Hand center vertically | Gradually return toward normal speed |
| Hand down | Brake |
| Fist | Pause |
| Open hand | Resume |

Horizontal position is mapped to the playable road area. Vertical thresholds control acceleration and braking. Smoothing prevents sudden car movement.

## ⌨️ Keyboard Controls

| Key | Action |
| --- | --- |
| `R` | Restart the game, including after game over |
| `ESC` | Quit the game |

## 🛠️ Technologies Used

| Area | Technology |
| --- | --- |
| Programming language | Python |
| Computer vision | OpenCV |
| Hand tracking | MediaPipe Hand Landmarker |
| Game development | Pygame-CE |
| Supported platform | Windows 10 and Windows 11 |

## 🧩 Concepts Used

Computer vision, hand tracking, hand landmark detection, gesture recognition, image processing, real-time processing, game loops, collision detection, object movement, smooth control, and interactive UI.

## 📁 Project Structure

```text
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
├── LICENSE
└── .gitignore
```

The existing obstacle filename is intentionally kept as `obstacal.png`.

## 📄 Project Files Explanation

### `main.py`

Contains Pygame initialization, the game loop, car movement, steering, speed control, road scrolling, obstacle generation, collision detection, score updates, UI panels, camera preview, pause screen, and game-over screen.

### `hand_detection.py`

Captures webcam frames with OpenCV, runs MediaPipe hand detection, reads landmarks and palm position, counts fingers, recognizes pause/resume gestures, smooths movement coordinates, and draws landmark visualization.

### `hand_landmarker.task`

The MediaPipe Hand Landmarker model required by `hand_detection.py`. It must remain in the project root beside `main.py` and `hand_detection.py`, not inside `assets/`.

### `assets/`

- `car.png`: player car image
- `road.png`: racing road image
- `obstacal.png`: road obstacle image

## 💻 System Requirements

- Windows 10 or Windows 11
- Python 3.14.x
- A working webcam
- Keyboard and display
- Internet access for package/model download when needed

## 📦 Required Python Libraries

- `pygame-ce`
- `mediapipe`
- `opencv-contrib-python`

### Important Pygame Note

The project installs `pygame-ce`, but the Python import remains:

```python
import pygame
```

Do not use `import pygame-ce`; that is invalid Python syntax.

## 🚀 Complete Installation Guide

### Clone Instructions

```powershell
git clone https://github.com/khilarionkar05/hand-controlled-car-racing-game.git
cd hand-controlled-car-racing-game
```

### ZIP Download Instructions

Open the repository on GitHub, select **Code**, choose **Download ZIP**, extract it, and open PowerShell in the extracted `hand-controlled-car-racing-game` folder.

### Python Installation

Install Python 3.14.x for Windows and enable the option to add Python to `PATH`. Verify Python and pip:

```powershell
python --version
python -m pip --version
```

### Library Installation

```powershell
python -m pip install pygame-ce
python -m pip install mediapipe
python -m pip install opencv-contrib-python
```

### Installation Verification

```powershell
python -c "import pygame, cv2, mediapipe; print('ALL SYSTEMS OK')"
```

## 🧠 MediaPipe Model Setup

The required model is `hand_landmarker.task`. If it is missing, download it from the official MediaPipe model URL:

<https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/latest/hand_landmarker.task>

Place it directly beside `main.py` and `hand_detection.py`. Do not place it inside `assets/`. The program loads the relative path `hand_landmarker.task`.

## 📷 Webcam Setup

The project normally opens the default camera with `cv2.VideoCapture(0)`. Allow camera access in Windows. With multiple cameras, change the camera index in `hand_detection.py` from `0` to `1` or `2`.

## ▶️ How To Run

From the project root:

```powershell
python main.py
```

## 🕹️ How To Play

Keep one hand visible to the webcam. Move it horizontally to steer and vertically to adjust speed. Avoid obstacles. Make a fist to pause and show an open hand to resume. After a collision, press `R` to restart or `ESC` to quit.

## ✋ Hand Tracking System

`HandController` captures, mirrors, and converts camera frames before sending them to MediaPipe. It averages the wrist and finger-base landmarks to estimate the palm center, counts fingers, and draws hand connections and landmarks on the preview.

## ↔️ Steering System

The normalized palm X coordinate is mapped between the road boundaries. The target position is clamped inside the road, then approached gradually using a smoothing factor.

## ⚡ Speed System

Palm Y values below `0.38` increase speed, values above `0.68` decrease speed, and values between them gradually return speed toward normal. Speed is clamped between the configured minimum and maximum and advances the road and obstacles.

## ✊ Gesture System

A finger count of one or fewer is treated as a fist and pauses the game. A count of four or more is treated as an open hand and resumes a paused game. A cooldown prevents repeated toggles from one gesture.

## 🚧 Obstacle System

Obstacles are created at randomly selected positions across three road lanes. Their vertical position increases with speed, and obstacles that leave the screen are removed.

## 💥 Collision Detection

Reduced-size Pygame rectangles are created for the car and obstacles. If any rectangles overlap, the game enters the game-over state and speed stops.

## 🏆 Score System

The score increases during active play in proportion to current speed. It appears as an integer in the score panel and on the game-over screen.

## 🛣️ Game Interface

The interface displays the road, car, obstacles, score, speed, quit hint, live hand-tracking preview, and hand-control panel. Pause and game-over overlays show their corresponding status and instructions.

## 🔄 Complete Project Workflow

1. Initialize Pygame and load the game images.
2. Initialize the webcam and MediaPipe model.
3. Capture and process a frame each loop iteration.
4. Convert hand position and finger count into controls.
5. Update steering, speed, road, obstacles, and score.
6. Check the car against active obstacles.
7. Draw the game, interface, and camera preview.
8. Display the frame and release the camera on exit.

## 🧪 Testing

Verify the installation command, confirm the model is in the project root, and run `python main.py`. Test steering, acceleration, braking, fist pause, open-hand resume, collision/game over, `R` restart, and `ESC` quit. Test camera index `1` or `2` when multiple webcams are connected.

## 🛠️ Troubleshooting

### Camera not working or permission denied

Check **Settings > Privacy & security > Camera**, close other webcam applications, and retry. The default is `cv2.VideoCapture(0)`.

### Wrong camera or multiple webcam problem

Change the camera index in `hand_detection.py` from `0` to `1` or `2`.

### `ModuleNotFoundError`

Install packages with the same Python interpreter used to run the game:

```powershell
python -m pip install pygame-ce
python -m pip install mediapipe
python -m pip install opencv-contrib-python
```

### Pygame installation problems

```powershell
python -m pip install --upgrade pip
python -m pip install pygame-ce
```

The package is `pygame-ce`, but the import is `pygame`.

### MediaPipe or OpenCV installation problems

Use Python 3.14.x, upgrade pip, and retry the exact package commands above. Network or package-mirror restrictions may require another network.

### `hand_landmarker.task` not found

Confirm the exact filename and keep it directly beside `main.py`. Run the command from the repository root.

### Game running slowly

Close other camera-heavy applications, improve lighting, keep one hand visible, and reduce other system load. Camera resolution can be reduced in the source if necessary.

### Hand not detected

Keep the full hand in view, improve lighting, remove visual obstructions, and check the live preview for landmarks.

## 🖼️ Project Preview

The repository currently does not include `game-preview.png`. To add a preview later, capture a running-game screenshot, save it as `game-preview.png` in the repository root, and add:

```markdown
![Game preview](game-preview.png)
```

## 🎥 Project Demo

No demo video link is currently included. Add a real hosted demo URL here when one is available.

## 🔮 Future Improvements

Possible additions include configurable camera selection, more obstacle types, difficulty levels, sound, persistent high scores, additional gestures, and recorded demos.

## 🎓 Learning Outcomes

This project demonstrates connecting computer vision and hand landmarks to a real-time game loop, smoothing noisy input, recognizing gestures, moving objects, detecting collisions, and rendering an interactive interface.

## 🎯 Project Objective

The objective is to build an accessible racing game that demonstrates practical computer vision, gesture recognition, and interactive Python game development using a webcam as the controller.

## 👤 Author

**Onkar Khilari**

Interests: Artificial Intelligence, Machine Learning, Computer Vision, Python, Robotics, Interactive Applications, and Software Development.

GitHub: <https://github.com/khilarionkar05>

LinkedIn: Add your LinkedIn profile link here

## 🙏 Acknowledgement

This project acknowledges Sandip University and PHN Technology Pvt Ltd.

## 🔗 Connect

- GitHub: <https://github.com/khilarionkar05>
- LinkedIn: Add your LinkedIn profile link here

## 💬 Support

For setup or gameplay issues, check Troubleshooting first. When reporting a reproducible problem, include the Windows version, Python version, package versions, camera setup, and exact error message.

## 📜 License

This project is licensed under the MIT License.

See the [LICENSE](LICENSE) file for the complete license text.

The project is primarily intended for educational and learning purposes.

## ⚡ Quick Start

```powershell
git clone https://github.com/khilarionkar05/hand-controlled-car-racing-game.git
cd hand-controlled-car-racing-game
python -m pip install pygame-ce
python -m pip install mediapipe
python -m pip install opencv-contrib-python
python -c "import pygame, cv2, mediapipe; print('ALL SYSTEMS OK')"
python main.py
```

## 📦 Final Project Structure

```text
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
├── LICENSE
└── .gitignore
```
