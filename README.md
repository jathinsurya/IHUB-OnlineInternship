# IHUB Online Internship – Weekly Tasks

## 📌 Overview

This repository contains my work for the IHUB Online Internship, covering multimedia processing and computer vision pipelines using FFmpeg and Ultralytics YOLO.

---

# 📅 Week 1 – Multimedia Processing (FFmpeg)

## 🔹 Task 1: Extract Frames from Video
- Downloaded a sample video
- Extracted frames at specific timestamps using FFmpeg
- Generated sample images:
  - img_1.jpg
  - img_2.jpg
  - img_3.jpg

---

## 🔹 Task 2: Frames to Video
- Extracted frames from a 1-minute video segment (~1800 frames at 30 FPS)
- Reconstructed video from frames using FFmpeg
- Uploaded output video to Google Drive

---

## 🔹 Task 3: Audio Merge
- Selected a 1-minute audio track
- Trimmed audio to match video duration
- Merged audio and video using FFmpeg

---

## 🛠 Tools Used (Week 1)
- FFmpeg
- yt-dlp
- Google Drive

---

# 📅 Week 2 – Object Detection using YOLOv8

## 🔹 Virtual Environment Setup
- Created isolated Python environment using `venv`
- Installed required libraries

---

## 🔹 Object Detection
- Used pretrained **YOLOv8n model**
- Performed object detection on images
- Generated annotated outputs with bounding boxes

### ✔ Output
- Detection results stored in:runs/detect/predict/

  
---

## 🔹 Advanced Task – Multi-Image Detection Pipeline

### ⚙️ Workflow
- Selected videos containing **people and vehicles**
- Extracted frames using FFmpeg
- Applied YOLOv8 detection on all frames
- Generated annotated images
- Converted images back to video
- Adjusted playback speed
- Added background audio

### ✔ Output
- Final detection video
- Sample annotated images
- Google Drive link provided

---

## 🛠 Tools Used (Week 2)
- Python (venv)
- Ultralytics YOLOv8
- OpenCV

---

# 📅 Week 3 – Semantic Segmentation & Video Pipeline

## 📌 Objective
Extend object detection to **semantic segmentation** and build a complete video pipeline.

---

## 🔹 Workflow

1. Converted raw images into video (OpenCV)
2. Applied YOLOv8 object detection
3. Applied YOLOv8 semantic segmentation
4. Generated segmented images (pixel-level masks)
5. Converted outputs into videos using FFmpeg
6. Normalized FPS and resolution (4 FPS, 640×360)
7. Stacked videos vertically:
 - Raw Video
 - Detection Video
 - Segmentation Video
8. Added background audio to final output

---

## 🎯 Key Concepts

- **Object Detection** → Bounding boxes
- **Semantic Segmentation** → Pixel-level classification

---

## 📂 Outputs

- Final stacked video available in repository: Week-03/outputs/final_output.mp4

---

## 📊 Performance Observations

- Total images processed: **134**
- Detection accuracy improves with clear, high-resolution frames
- Segmentation performs best on larger objects
- Performance drops in low-resolution (640×360) frames
- Model limited to pretrained object classes

---

## 📈 Analysis

- Frames from longer videos had higher object density
- Motion blur and poor lighting reduce detection accuracy
- Consistent frame sequencing is critical for synchronization

---

## 🧠 Applications

- Medical Imaging → Tumor detection
- Autonomous Driving → Road and pedestrian segmentation
- Surveillance Systems → Activity monitoring
- Defense Systems → Target tracking

---

# 📂 Repository Structure
Week-01/
Week-02/
Week-03/
├── outputs/
│ └── final_output.mp4
├── commands.txt
├── notes.txt
└── README.md


---

# 📊 Key Learnings

- Video processing using FFmpeg
- Frame extraction and reconstruction
- Audio-video synchronization
- Environment setup using Python venv
- Object detection using pretrained models
- Semantic segmentation for pixel-level understanding
- Importance of data consistency in pipelines

---

# 🚀 Conclusion

This internship helped build a complete understanding of:

- Multimedia processing pipelines
- Computer vision workflows
- End-to-end integration of FFmpeg and deep learning models

The transition from detection to segmentation highlights the importance of precision in real-world applications.

---
