# Road Damage Detection Using Different Versions of YOLO

This repository provides a **comparative implementation and analysis** of road damage detection using multiple YOLO versions, including **YOLOv7, YOLOv8, and YOLOv11**.
The project allows users to test images and videos, compare results across models, and generate a **final prediction by selecting the best-performing model output**.

---

## 📌 Project Overview

* Implemented **YOLOv7, YOLOv8, and YOLOv11** models
* Each model folder contains:

  * Trained `best.pt` weights
  * Inference results on the dataset
* A **comparative analysis report** is included
* A **Streamlit-based application** (`app.py`) selects the best prediction among all models and displays the final road damage detection output

---

## 📁 Repository Structure

Each YOLO version has its own directory with trained models, inference scripts, and results.

### YOLOv8

* Contains `image+videorunner.py` to run inference on:

  * Images
  * Videos
* Stores inference results in **JSON format**
* Example results path:

  ```
  Road_Damage_Detection_Using_Different_Versions_Of_Yolo/
  └── using Yolov8/
      └── Videos/
  ```

  * Includes results for:

    * Videos
    * Car-view images
    * Snapshot images

### YOLOv11

* Contains an `infer/` directory
* Stores **bounding-box annotated images** from inference

### Yolov7

Github link for it - https://github.com/sachin23052005/Road_damage_detection_using_Yolov7

---

## 🧠 Final Model Selection Logic

The file `app.py` performs the **final inference pipeline**, where:

* Outputs from all YOLO versions are evaluated
* The best-performing model’s prediction is selected
* Final road damage detection results are displayed to the user

---

## 🚀 Using the Models Directly (Minimal Setup)

To avoid unnecessary directories and run only the final application, you can extract the trained models and organize them as follows:

```
project/
│
├── app.py
├── models/
│   ├── yolov7.pt
│   ├── yolov8s.pt
│   ├── yolov8m.pt
│   ├── yolov11s.pt
│   └── yolov11m.pt
├── requirements.txt
```

> 📌 The `.pt` files can be found inside the `runs/` directory of each YOLO model folder.

---

## 🛠 Installation & Run Instructions

### 1️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

### 2️⃣ Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Arrange the Models

Place all required `.pt` files inside the `models/` directory as shown above.

### 5️⃣ Run the Application

```bash
streamlit run app.py
```

---

## 📊 Features

* Supports **image and video input**
* Compares predictions from multiple YOLO versions
* Displays **final optimized road damage detection**
* Easy-to-use **Streamlit interface**

---

## 📄 Notes

* Ensure compatible versions of PyTorch and YOLO are installed as specified in `requirements.txt`
* GPU support is recommended for faster inference
* JSON-based results allow easy integration with other systems

---
## Model Performance Comparison

| Model       | Precision | Recall  | mAP@50  | mAP@50-95 |
|-------------|-----------|---------|---------|-----------|
| YOLOv7      | 0.6349    | 0.6261  | 0.6423  | 0.3912    |
| YOLOv8-S    | 0.7786    | 0.7173  | 0.7639  | 0.5417    |
| YOLOv8-M    | **0.8058**| **0.7382** | **0.7916** | **0.5770** |
| YOLOv11-S   | 0.79 (approx) | 0.69 (approx) | 0.74  | 0.51      |
| YOLOv11-M   | 0.71      | 0.68    | 0.70    | 0.47      |

---

