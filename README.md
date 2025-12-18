 

# Road Damage Detection using YOLO Models

## Model Performance Comparison

| Model       | Precision | Recall  | mAP@50  | mAP@50-95 |
|-------------|-----------|---------|---------|-----------|
| YOLOv7      | 0.6349    | 0.6261  | 0.6423  | 0.3912    |
| YOLOv8-S    | 0.7786    | 0.7173  | 0.7639  | 0.5417    |
| YOLOv8-M    | **0.8058**| **0.7382** | **0.7916** | **0.5770** |
| YOLOv11-S   | 0.79 (approx) | 0.69 (approx) | 0.74  | 0.51      |
| YOLOv11-M   | 0.71      | 0.68    | 0.70    | 0.47      |

---

## Abstract

**Road safety** is heavily dependent on timely detection and classification of road surface defects such as potholes, cracks, and lane-damaging anomalies, which may cause vehicle instability, traffic accidents, and long-term infrastructural degradation. With modern advances in deep learning and real-time computer vision, object detection architectures such as the YOLO (You Only Look Once) family have become widely adopted for autonomous driving and infrastructure inspection tasks.

This paper presents a detailed comparative analysis of three generations of YOLO models—YOLOv7, YOLOv8 (small and medium variants), and YOLOv11 (small and medium variants)—trained on the publicly available Road Damage Dataset hosted on Roboflow. The evaluation focuses on precision, recall, mAP@50, and mAP@50:95 in order to determine architectural efficiency and real-world deployment suitability.

Results indicate that YOLOv8-M achieves the highest overall accuracy with a mean Average Precision (mAP@0.5) of 0.7916 and mAP@0.5:0.95 of 0.5770, surpassing YOLOv7 and YOLOv11 models trained for equal or fewer epochs. YOLOv11 models demonstrate strong potential but require additional training iterations to stabilize performance.

The findings highlight the importance of model scaling, pretrained weights, and transfer learning in low- to medium-sized datasets and present future directions including large-scale training on datasets exceeding 100,000 annotated samples for robust deployment in smart transportation systems and autonomous inspection vehicles.

---

## Conclusion

This study demonstrates that YOLOv8-M currently offers the best performance–efficiency trade-off for road damage detection tasks on medium-sized datasets. YOLOv11, although promising, requires extended training to fully exploit architecture improvements.

