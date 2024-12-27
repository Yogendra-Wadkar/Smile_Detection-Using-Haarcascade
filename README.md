# Smile Detection Using Haarcascade

## 📖 Introduction
Welcome to the Smile Detection project! This repository showcases the implementation of a real-time smile detection system using Haarcascade classifiers in OpenCV. The project focuses on identifying smiles from facial features in video streams or images with high accuracy and efficiency. 🎉✨🎥

![Smile Detection Demo](https://github.com/user-attachments/assets/0e6b1a98-2ee0-4453-bb63-b6451cd4fff5)

## What's Inside?
- **Source Code:** Contains the Python script for smile detection, leveraging Haarcascade and OpenCV.
- **Model Files:** Includes the Haarcascade XML file for face detection and the pre-trained model for smile classification.
- **Demo Video:** Provides a sample video showcasing the smile detection system in action. 🎥📂✅

## Features
- **Real-Time Detection:** Detect smiles in live video streams or pre-recorded videos.
- **Haarcascade Classifiers:** Utilized Haarcascade for face and feature detection.
- **Pre-trained Model Integration:** Incorporates a pre-trained CNN model for accurate smile classification.
- **Optimized Performance:** Achieves fast and reliable results with minimal processing delay. 🚀📊😃

## How It Works
1. **Face Detection:** The system uses Haarcascade to detect faces within frames.
2. **Feature Extraction:** Extracts regions of interest (ROIs) around detected faces.
3. **Smile Classification:** A pre-trained CNN model classifies whether the detected face is smiling or not.
4. **Display Results:** Labels and bounding boxes are displayed on the video frame in real-time. 🤔📸✅

## How to Use This Repository
1. **Clone this repository** to your local machine:
   ```bash
   git clone https://github.com/YourUsername/Smile-Detection-Using-Haarcascade.git
   ```
2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the smile detection script:**
   ```bash
   python smile_detection.py
   ```
4. **Test the system** with a video by replacing the `video_path` variable in the script with the path to your video file. 🎬📋💻

## Demo Highlights
- **Input:** Video feed or pre-recorded video file.
- **Output:** Annotated frames showing detected faces and smile labels ("Smiling" or "Not Smiling").
- **Customization:** Easily configurable parameters for face detection sensitivity and model thresholds. 🎥📊🎨

## Technical Details
- **Frameworks:** OpenCV, Keras
- **Classifier:** Haarcascade Frontal Face Classifier
- **Model:** Pre-trained CNN for smile classification. 🧠💡📂

## Future Enhancements
- Extend support for detecting additional facial expressions.
- Optimize the model for mobile and edge devices.
- Incorporate advanced techniques like DNN-based face detection for improved accuracy. 🤖📈🌟

Ready to explore the smile detection journey? Clone or download this repository and get started today! 🚀✨😃

