# System Architecture

```mermaid
flowchart LR
    A[CLI User] --> B[Input Validation]
    B --> C[Preprocessing]
    B --> D[Object Detection]
    B --> E[Shape Detection]
    B --> F[Video Analysis]
    C --> G[Image Analytics]
    D --> G
    E --> G
    G --> H[JSON Report]
    C --> I[Output Media]
    D --> I
    E --> I
    F --> I
```

## Components
- `main.py`: command-line routing and validation.
- `preprocessing.py`: image transformations.
- `object_detection.py`: Haar-cascade face detection.
- `shape_detection.py`: contour extraction and classification.
- `image_analysis.py`: image statistics.
- `video_analysis.py`: motion detection using frame differencing.
- `report_generator.py`: structured JSON output.
