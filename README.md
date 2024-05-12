# Real-Time Face Detection and Verification

This project combines real-time face detection using MTCNN and face verification using DeepFace. It captures frames from the webcam, detects faces, and verifies them against a known face database.

## Features

- Real-time face detection using MTCNN.
- Face verification against a known face database using DeepFace.
- Continuous webcam capture and processing.
- Automatic cleanup of detected faces folder.

## Prerequisites

Before running the code, ensure you have the following installed:

- Python 3.x
- OpenCV (`pip install opencv-python`)
- MTCNN (`pip install mtcnn`)
- DeepFace (`pip install deepface`)

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/jibincb/face-identification.git
2. Navigate to the project directory:
   cd face-identification
3. Run the script:
   python face_detection_verification.py

## File Structure
face_detection_verification.py: Main script for real-time face detection and verification.
detected/: Folder to store detected faces (which will be generated automatically).
faces/: Folder containing known faces for verification.

## Contributions
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
