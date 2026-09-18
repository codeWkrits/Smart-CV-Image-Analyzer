# Class / Component Design

The project uses a modular functional design so each computer vision operation can be tested independently.

| Component | Responsibility |
|---|---|
| `main.py` | CLI routing and input validation |
| `preprocessing.py` | Image transformations |
| `object_detection.py` | Face detection |
| `shape_detection.py` | Contour and shape classification |
| `image_analysis.py` | Image statistics |
| `video_analysis.py` | Motion analysis |
| `report_generator.py` | JSON report generation |

This separation improves maintainability, reuse, testing, and clarity.
