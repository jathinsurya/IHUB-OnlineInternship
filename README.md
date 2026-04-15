# IHUB Online Internship – Weekly Tasks

## 📌 Overview

This repository contains my submissions for Week 1 and Week 2 of the IHUB Online Internship. The tasks focus on multimedia processing using FFmpeg and basic computer vision using Ultralytics YOLO.

---

# 📅 Week 1 – Multimedia Processing (FFmpeg)

## 🔹 Task 1: Extract Frames from Video

* Downloaded a short video.
* Used FFmpeg to extract specific frames at different timestamps.
* Generated sample images:

  * img_1.jpg
  * img_2.jpg
  * img_3.jpg

---

## 🔹 Task 2: Frames to Video

* Extracted frames from a 1-minute segment at **30 FPS (~1800 frames)**.
* Reconstructed the video from these frames using FFmpeg.
* Uploaded the generated video to Google Drive.

---

## 🔹 Task 3: Audio Merge

* Selected a 1-minute audio track from Pixabay.
* Trimmed the audio to exactly 60 seconds.
* Merged the audio with the reconstructed video using FFmpeg.
* Generated final video with synchronized audio.

---

## 🛠 Tools Used (Week 1)

* FFmpeg
* yt-dlp (for downloading videos)
* Google Drive (for video hosting)

---

# 📅 Week 2 – Python Virtual Environment & Object Detection

## 🔹 Virtual Environment Setup

* Created a Python virtual environment using `venv`.
* Activated environment and installed required packages.

---

## 🔹 Ultralytics YOLO Object Detection

* Installed Ultralytics package inside the virtual environment.
* Used pretrained **YOLOv8n model** for object detection.
* Ran detection on a sample image.

### ✔ Output

* Generated image with bounding boxes and labels (e.g., person, bus).
* Output stored in:

  ```
  runs/detect/predict/
  ```

---

## 🛠 Tools Used (Week 2)

* Python (venv)
* Ultralytics YOLOv8
* OpenCV (dependency)

---

# 📂 Repository Structure

```
Week-01/
  ├── Task1_ffmpeg_frames/
  ├── Task2_frames_to_video/
  └── Task3_audio_merge/

Week-02/
  ├── venv_setup/
  └── ultralytics_detection/
```

---

# 📊 Key Learnings

* Understanding video processing pipeline (frames extraction & reconstruction)
* Working with frame rates and encoding
* Audio-video synchronization using FFmpeg
* Setting up isolated Python environments
* Running pretrained deep learning models for object detection

---

# 🔗 Outputs

* Sample images and detection outputs are included in the repository.
* Generated videos are shared via Google Drive links inside respective folders.

---

# 🚀 Conclusion

These tasks helped build a strong foundation in:

* Multimedia processing
* Command-line tools (FFmpeg)
* Python environment management
* Basic computer vision workflows

---
Advanced Task: Multi-Image Object Detection Pipeline
📌 Objective

To extend basic object detection to a full pipeline by processing multiple images extracted from videos, applying detection, and reconstructing results into a video.

⚙️ Workflow
Selected multiple videos containing people and vehicles for meaningful detection.
Extracted frames using FFmpeg at controlled frame rates.
Combined frames from different video sources into a single dataset.
Applied Ultralytics YOLOv8n (pretrained) model on all images.
Generated annotated images with bounding boxes and class labels.
Converted detected images into a video using FFmpeg.
Adjusted frame rate to control playback speed (~30 seconds output).
Added background audio and synchronized video using FFmpeg.
✔ Output
Final video showing detected objects with bounding boxes.
Sample annotated images included in repository.
Video link provided via Google Drive.
🧠 Observations
YOLO detects only pretrained object classes (e.g., person, car, bus).
Detection quality improves with clear and well-lit images.
Poor resolution and motion blur reduce detection accuracy.
Frame selection significantly impacts overall output quality.
📅 Week 3 – Semantic Segmentation & Performance Analysis
📌 Objective

To perform semantic segmentation on images and analyze model performance using inference-based metrics.

⚙️ Workflow
Used previously extracted images as input dataset.
Applied YOLOv8 segmentation model (yolov8n-seg.pt).
Generated images with pixel-level colored masks for each object.
Renamed output images into a continuous sequence.
Converted segmented images into video using FFmpeg.
Added new background audio to enhance visualization.
🎯 Key Concept
Object Detection → Provides bounding boxes
Segmentation → Provides exact object boundaries (pixel-level)
✔ Output
Segmented images with colored masks.
Final video showing semantic segmentation results.
Sample segmented outputs included in repository.
Video link provided via Google Drive.
📊 Performance Metrics (Inference-Based)

Since pretrained models were used without training, performance was analyzed using prediction outputs:

Total images processed: 134
Detection count per image analyzed
Object distribution observed across frames
Observations:
Higher object density observed in frames from longer video (v2).
Better segmentation results for large and clearly visible objects.
Reduced performance in low-resolution frames (640×360).
Model limited to predefined classes.
Graphs Included:
Detection count per image
🧠 Applications of Semantic Segmentation
Medical Imaging → Tumor boundary detection
Autonomous Driving → Road and pedestrian understanding
Surveillance Systems → Activity monitoring
Defense Systems → Target identification
🚀 Conclusion

This week expanded the pipeline from object detection to pixel-level understanding of images.

Key takeaways:

Segmentation provides more precise information than detection.
Model performance depends heavily on input quality.
Combining FFmpeg + YOLO enables powerful end-to-end vision pipelines.
