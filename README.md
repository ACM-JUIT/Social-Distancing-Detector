
<img alt="Python" src="https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white"/> <img alt="OpenCV" src="https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white"/>

# Social-Distancing-in-Real-Time
Social distancing in Real-Time using live video stream/IP camera in OpenCV.


Input      |  Output
:-------------------------:|:-------------------------:
![Input](resources/input.gif "Input")  |  ![Output](resources/output.gif "Output")

---
## Features
- Accept feed from live cam, IP camera and custom video input.
- Counting the number of people in real-time.
- Sending an alert(audio) if the people are way over the 
   social distancing limits.
- Safe distance entered by the user (GUI)
- Detect humans in the frame with yolov4
- Stores violations in a csv file.

---
## Setup
💻 Install the dependencies on command line:

```sh
$ pip install -r requirement.txt
```

💻 To run the program on command line:

```sh
$ python social distance detector.pyw
```

💻 To run the GUI on command line:

```sh
$ python social distance detector gui.pyw
```
</br>

---


