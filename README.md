<div align="center">

```
██╗██╗  ██╗██╗   ██╗██████╗      ██████╗ ██╗      ██╗███╗   ██╗███████╗
██║██║  ██║██║   ██║██╔══██╗    ██╔═══██╗███╗  ██╔╝██║████╗  ██║██╔════╝
██║███████║██║   ██║██████╔╝    ██║   ██║██╔██╗██╔╝ ██║██╔██╗ ██║█████╗  
██║██╔══██║██║   ██║██╔══██╗    ██║   ██║██║╚████╔╝ ██║██║╚██╗██║██╔══╝  
██║██║  ██║╚██████╔╝██████╔╝    ╚██████╔╝██║ ╚███╔╝ ██║██║ ╚████║███████╗
╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝      ╚═════╝ ╚═╝  ╚══╝  ╚═╝╚═╝  ╚═══╝╚══════╝
```

### `MULTIMEDIA PROCESSING · COMPUTER VISION · DEEP LEARNING`

<br/>

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-00FFAA?style=for-the-badge&logo=github&logoColor=black)](https://ultralytics.com)
[![FFmpeg](https://img.shields.io/badge/FFmpeg-007808?style=for-the-badge&logo=ffmpeg&logoColor=white)](https://ffmpeg.org)
[![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org)
[![Google Colab](https://img.shields.io/badge/Google%20Colab-T4%20GPU-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=black)](https://colab.research.google.com)
[![Label Studio](https://img.shields.io/badge/Label%20Studio-Annotation-FF6B6B?style=for-the-badge)](https://labelstud.io)

<br/>

> **5 weeks. 5 modules. 1 complete AI pipeline.**
> From raw video frames to a deployed traffic intelligence system.

<br/>

---

</div>

## 📡 &nbsp;What Is This?

This repository documents an end-to-end **Computer Vision & Multimedia Processing** internship at **IHUB**, progressing from foundational video manipulation all the way to a production-grade **Traffic Density Monitoring system** trained on custom-annotated data.

Every week builds on the last — forming a complete, real-world AI engineering workflow.

```
  RAW VIDEO  ──▶  FRAME EXTRACTION  ──▶  ANNOTATION  ──▶  MODEL TRAINING  ──▶  DEPLOYMENT
      │                  │                    │                   │                  │
   FFmpeg             FFmpeg +             Label Studio        YOLOv8n           Inference
   yt-dlp             OpenCV               (Manual)          Transfer            + Video
                                                             Learning            Output
```

<br/>

---

## 🗺️ &nbsp;Journey Map

<div align="center">

| Week | Module | Core Skill | Status |
|:----:|--------|-----------|:------:|
| `01` | 🎬 Multimedia Processing | FFmpeg · Frame I/O · Audio Sync | ✅ |
| `02` | 🔍 Object Detection | YOLOv8 · Bounding Boxes · Video Pipeline | ✅ |
| `03` | 🎭 Semantic Segmentation | Pixel Masks · Video Stacking · Multi-Output | ✅ |
| `04` | 🏷️ Dataset Annotation | Label Studio · YOLO Format · Custom Classes | ✅ |
| `05` | 🚗 Custom Model Training | Transfer Learning · mAP 0.99 · Traffic AI | ✅ |

</div>

<br/>

---

## 📅 Week 01 — Multimedia Processing with FFmpeg

> *"Understanding the atom before building the molecule."*

Mastered the core building block of all CV pipelines: **video ↔ frame conversion**.

<details>
<summary><b>📂 Click to expand tasks & outputs</b></summary>

<br/>

### 🔹 Task 1 — Frame Extraction
Extract individual frames from a video at precise timestamps.

```bash
# Extract frames at custom rate
ffmpeg -i input.mp4 -vf fps=30 frames/img_%04d.jpg
```

**Outputs:** `img_1.jpg` · `img_2.jpg` · `img_3.jpg`

---

### 🔹 Task 2 — Video Reconstruction
Reassemble ~1800 extracted frames (30 FPS · 1-minute video) back into a video.

```bash
# Reconstruct video from frames
ffmpeg -framerate 30 -i frames/img_%04d.jpg -c:v libx264 output.mp4
```

---

### 🔹 Task 3 — Audio Merge
Trim a royalty-free audio track and synchronize it with the reconstructed video.

```bash
# Merge audio with video
ffmpeg -i video.mp4 -i audio.mp3 -shortest final_output.mp4
```

</details>

**🧠 Key Learnings:** Video decomposition · Frame-rate handling · Audio-video sync · Multimedia encoding

<br/>

---

## 📅 Week 02 — Object Detection with YOLOv8

> *"Teaching machines to see — and label what they see."*

Used **pretrained YOLOv8n** for zero-shot detection, then built a full image→video annotation pipeline.

<details>
<summary><b>📂 Click to expand pipeline & outputs</b></summary>

<br/>

### ⚙️ Full Pipeline

```
  Videos  ──▶  FFmpeg Frame Extraction  ──▶  YOLOv8 Detection  ──▶  Annotated Frames
      └─────────────────────────────────────────────────────────▶  Reconstructed Video
                                                                         + Audio
```

### Setup

```bash
python -m venv yolo_env
source yolo_env/bin/activate        # Linux/Mac
yolo_env\Scripts\activate           # Windows

pip install ultralytics opencv-python
```

### Detection

```python
from ultralytics import YOLO

model = YOLO("yolov8n.pt")
results = model.predict(source="frames/", save=True)
# Output → runs/detect/predict/
```

</details>

**🧠 Key Learnings:** Pretrained model inference · Bounding box generation · Image-to-video pipelines

<br/>

---

## 📅 Week 03 — Semantic Segmentation & Stacked Video Pipeline

> *"From boxes to pixels — full scene understanding."*

Extended detection into **pixel-level segmentation**, then stacked three synchronized video outputs.

<details>
<summary><b>📂 Click to expand pipeline & outputs</b></summary>

<br/>

### 🎬 Stacked Output Architecture

```
┌────────────────────────────────────────────┐
│                                            │
│  [ RAW VIDEO ] [ DETECTION ] [ SEGMENT ]   │  ◀── Side-by-side stacked output
│                                            │
└────────────────────────────────────────────┘
              + Background Audio
```

### Segmentation Command

```python
from ultralytics import YOLO

model = YOLO("yolov8n-seg.pt")
results = model.predict(source="frames/", save=True)
# Pixel-level masks generated for all 134 frames
```

### 📊 Performance Observations

| Condition | Detection | Segmentation |
|-----------|:---------:|:------------:|
| Clear HD frames | 🟢 Excellent | 🟢 Excellent |
| Large objects | 🟢 Excellent | 🟢 Best |
| Motion blur | 🟡 Reduced | 🔴 Poor |
| Low lighting | 🟡 Reduced | 🔴 Poor |

**Output:** `Week-03/outputs/final_output.mp4`

</details>

**🧠 Key Learnings:** Semantic segmentation · Pixel classification · Multi-video sync · Resolution normalization

<br/>

---

## 📅 Week 04 — YOLO Dataset Preparation & Manual Annotation

> *"No labels, no learning. The data is the model."*

Built a production-quality annotated dataset from scratch using real traffic footage.

<details>
<summary><b>📂 Click to expand dataset structure & workflow</b></summary>

<br/>

### 📁 Standard YOLO Dataset Structure

```
dataset/
├── images/
│   ├── train/          ← 70% of data
│   ├── val/            ← 20% of data
│   └── test/           ← 10% of data
├── labels/
│   ├── train/
│   └── val/
├── data.yaml           ← class names + paths
├── train.txt
└── val.txt
```

### 🏷️ YOLO Label Format

```
<class_id>  <x_center>  <y_center>  <width>  <height>
    0           0.512       0.437      0.230    0.180
```
> All values normalized `[0.0 → 1.0]` relative to image dimensions.

### Frame Extraction for Annotation

```bash
# Extract 2 frames per second from traffic video
ffmpeg -i traffic.mp4 -vf fps=2 images/img_%03d.jpg
```

### Label Studio Setup

```bash
python -m venv label_env
label_env\Scripts\activate
pip install label-studio
label-studio start
```

### 📊 Dataset Summary

| Property | Value |
|----------|-------|
| Total Images | `84` |
| Labeled Images | `34` |
| Classes | `person` · `vehicle` |
| Format | YOLO Normalized |

</details>

**🧠 Key Learnings:** Annotation workflows · YOLO format · Dataset splits · Label quality

<br/>

---

## 📅 Week 05 — Custom Model Training · Traffic Density Monitor

> *"The capstone. Transfer learning on custom data. Real-world deployment."*

<div align="center">

### 🚗 Traffic Density Monitoring System

*Built with YOLOv8 · Trained on custom traffic data · Deployed on real-world footage*

</div>

<details>
<summary><b>📂 Click to expand full pipeline</b></summary>

<br/>

### ⚙️ End-to-End Workflow

```
Pexels Traffic Video
        │
        ▼
  FFmpeg @ 5 FPS
        │
        ▼
 ┌──────────────────────────┐
 │   Dataset Split          │
 │   Train  │  Val  │ Test  │
 │    75    │  21   │  11   │
 └──────────────────────────┘
        │
        ▼
  Label Studio Annotation
  (cars · trucks · bboxes)
        │
        ▼
  Image Preprocessing
  4K (3840×2160) → 384px
  [aspect ratio preserved]
        │
        ▼
  YOLOv8n Transfer Learning
  Google Colab · T4 GPU
  100 epochs · imgsz=384
        │
        ▼
  Inference on Test Set
        │
        ▼
  Final Video + Audio Output
```

</details>

### 📈 Training Configuration

```yaml
model:     yolov8n.pt      # pretrained base
epochs:    100
imgsz:     384
data:      data.yaml
device:    T4 GPU (Colab)
```

### 📊 Model Performance

<div align="center">

| Metric | Score | Rating |
|--------|:-----:|:------:|
| **Precision** | `0.905` | 🟢 Excellent |
| **Recall** | `0.647` | 🟡 Good |
| **mAP@50** | `0.662` | 🟡 Good |
| **mAP@50:95** | `0.460` | 🟡 Good |
| **Training Time** | `~0.031 hrs` | ⚡ Fast |

</div>

### 🎯 Per-Class Breakdown

<div align="center">

| Class | mAP@50 | Bar |
|-------|:------:|-----|
| 🚗 **car** | `0.989` | `█████████▉` |
| 🚛 **truck** | `0.336` | `███▍` |

</div>

> **Note:** Truck detection underperformed due to limited training samples. Adding more annotated truck images in future iterations will significantly boost recall.

<br/>

---

## 🗂️ Repository Structure

```
IHUB-OnlineInternship/
│
├── 📁 Week-01/                  ← FFmpeg · Frame I/O · Audio Sync
├── 📁 Week-02/                  ← YOLOv8 Detection · Video Pipeline
├── 📁 Week-03/                  ← Segmentation · Stacked Output
├── 📁 Week-04/                  ← Label Studio · Custom Dataset
│
└── 📁 Week-05/                  ← 🏆 Capstone Project
    ├── dataset/                 ← train / val / test splits
    ├── resized/                 ← 384px preprocessed images
    ├── outputs/                 ← inference results
    ├── runs/                    ← YOLOv8 training runs
    ├── weights/                 ← best.pt · last.pt
    ├── data.yaml
    ├── train.txt
    ├── val.txt
    ├── commands.txt
    ├── notes.txt
    └── README.md
```

<br/>

---

## 🛠️ Tech Stack

<div align="center">

| Category | Tools |
|----------|-------|
| **Video Processing** | FFmpeg · yt-dlp · OpenCV |
| **Detection & Segmentation** | Ultralytics YOLOv8 (`n`, `n-seg`) |
| **Annotation** | Label Studio |
| **Training** | Google Colab · T4 GPU |
| **Language** | Python 3.10+ |
| **Environment** | venv |

</div>

<br/>

---

## 🧠 Skills Gained

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  VIDEO ENGINEERING          AI / ML                             │
│  ─────────────────          ──────                              │
│  ✦ Frame extraction         ✦ Transfer learning                │
│  ✦ Video reconstruction     ✦ Custom model training            │
│  ✦ Audio synchronization    ✦ mAP / Precision / Recall         │
│  ✦ FPS & resolution norm    ✦ Inference pipelines              │
│                                                                 │
│  COMPUTER VISION            DATA ENGINEERING                    │
│  ────────────────           ────────────────                    │
│  ✦ Object detection         ✦ Dataset design & splits          │
│  ✦ Semantic segmentation    ✦ Manual annotation workflows      │
│  ✦ Bounding boxes           ✦ YOLO label format                │
│  ✦ Pixel-level masks        ✦ data.yaml · metadata files       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

<br/>

---

## 🚀 Real-World Applications

<div align="center">

| Domain | Use Case |
|--------|----------|
| 🏙️ **Smart Cities** | Traffic density & flow monitoring |
| 🏥 **Medical Imaging** | Organ / lesion segmentation |
| 🚘 **Autonomous Vehicles** | Pedestrian & obstacle detection |
| 🔐 **Surveillance** | Crowd analysis & anomaly detection |
| 🛡️ **Defense** | Target recognition systems |

</div>

<br/>

---

## 📌 Future Improvements

- [ ] 🔁 Expand truck dataset → improve recall from `0.336` to `0.80+`
- [ ] 📦 Add instance segmentation for vehicle silhouettes
- [ ] 📡 Build real-time webcam / RTSP stream inference
- [ ] 📊 Add a traffic density heatmap overlay
- [ ] 🌐 Deploy as a Flask / FastAPI web app
- [ ] 🧪 Experiment with YOLOv8m / YOLOv8l for higher accuracy

<br/>

---

<div align="center">

---

**IHUB Online Internship · Computer Vision Track**

*Built week by week · Frame by frame · Pixel by pixel*

---

</div>
