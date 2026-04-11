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
🔹 Advanced Task – Multi-Image Object Detection Pipeline
* Used multiple videos containing people and vehicles to ensure meaningful object detection.
* Extracted frames from videos using FFmpeg with controlled frame rate.
* Combined frames from different sources into a single dataset.
* Applied YOLOv8 pretrained model for object detection on all images.
* Generated annotated images with bounding boxes.
* Converted detected images into a video using FFmpeg.
* Adjusted frame rate to control playback speed (~30 seconds output).
* Added background audio and synchronized using FFmpeg.
  
✔ Output
* Final video created from detected images with audio overlay.
* Sample annotated images available in repository.


🧠 Observations
YOLO detects only pretrained object classes (e.g., person, car, bus).
Detection quality depends heavily on input image clarity and object presence.
Frame selection plays a key role in meaningful output.
