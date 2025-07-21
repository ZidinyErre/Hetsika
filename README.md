# Hetsika

## Description

**Hetsika** (which means "movement" in Malagasy) is an interactive Python project that uses a webcam to detect body movement and plays sounds in response to these gestures. The goal is to turn the body into an instrument, using the camera as a motion sensor without any external hardware.

This project was built as the **final project for CS50 2025**. It uses libraries such as OpenCV for video processing and motion detection, and Pygame for handling audio.

---

## Features

- Real-time webcam capture
- Background subtraction to detect moving body parts (arms, hands, etc.)
- Clean exit using a keyboard key (`q`)
- Minimalist visual interface (OpenCV windows only)

---

## Technologies Used

- **Python 3.13**
- **OpenCV (cv2)** — for video capture and motion tracking
- **NumPy** — used internally to process frame data
- **Pygame (mixer)** — for sound playback
- **Git / GitHub** — version control and project publishing

---

## Background and Motivation

As a dancer, especially in breakdance, I wanted to adapt my creation to my lifestyle.  
**Hetsika** was born from the idea of turning my movements into sound.

Rather than building a traditional app or website, I chose to let the **body become the controller**. With OpenCV and a webcam, I could capture gestures and assign different sound effects depending on movement location. It acts like an invisible musical instrument, where your space and gestures become the keys.

---

## How It Works

When the script runs, the webcam turns on and starts capturing frames in real time.
A foreground mask is generated using OpenCV’s createBackgroundSubtractorMOG2(), which highlights moving areas in white and keeps static regions black.

Each frame is then analyzed using cv2.countNonZero(), which counts the number of active (white) pixels in the mask.
This count reflects how much motion is currently visible.

If the number of white pixels exceeds a defined threshold, a looping sound is played using pygame.mixer.
If the sound was paused, it resumes from where it left off.
If there is little to no movement, the sound is paused.

This allows the user to control music playback through full-body motion:

 Moving → the music starts or resumes

 Still → the music pauses but doesn't restart from the beginning

The interaction is direct, responsive, and expressive — no keyboard or controller needed.


---

## Challenges Faced

- **Understanding motion detection logic**: It took effort to understand how background subtraction works, how `cv2.waitKey()` affects frame display, and how to interpret frame matrices.
- **Choosing a sound library**: I considered multiple libraries (like playsound or pydub) before selecting **Pygame**, which allowed better control through channels and volume.
- **Mental fatigue**: Toward the end, I felt exhausted and considered quitting. But I wanted to finish something real, something mine.
- **Next** : I feel this project need to be a mobile app now, to  be more flexible.


---

## Installation

### Prerequisites

- Python 3.10+
- pip

### Setup

```bash
# Create a virtual environment
python -m venv .venv

# Activate it (on Windows PowerShell)
.\.venv\Scripts\Activate

# Install required libraries
pip install opencv-python pygame

# (Optional) Save your dependencies
pip freeze > requirements.txt

# Run the program with your chosen algorithm
python your_script_name.py --algo MOG2
# Or:
python your_script_name.py --algo KNN


You can stop the program by pressing the q key in the OpenCV window.

Credit
This project includes guidance received via ChatGPT for development and documentation purposes.

