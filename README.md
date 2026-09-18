# Smart Image Analysis and Object Detection System Using Computer Vision

A modular Python + OpenCV academic project that processes images and videos through multiple computer vision pipelines and produces annotated outputs plus structured analysis data.

## Author
**Kriti Kumari**

## Overview
The system provides a command-line workflow for preprocessing images, detecting faces, recognizing basic geometric shapes, calculating image statistics, detecting motion in video, and saving a JSON analysis report.

## Major Functional Modules
1. **Image Preprocessing** — resize, grayscale, Gaussian blur, thresholding, and Canny edge detection.
2. **Object/Face Detection** — OpenCV Haar-cascade based face detection with annotated bounding boxes.
3. **Shape Detection** — contour extraction and polygon approximation for triangles, squares, rectangles, circles, and other polygons.
4. **Image Analytics & Reporting** — dimensions, channels, intensity statistics, detection counts, and JSON report generation.
5. **Video Motion Analysis** — frame differencing with motion-region annotation and saved output video.

## Non-Functional Requirements Addressed
- **Performance:** avoids unnecessary repeated image conversions inside each operation.
- **Usability:** simple CLI commands and readable status/error messages.
- **Reliability:** input validation and media-open checks.
- **Maintainability:** separate modules with focused responsibilities.
- **Resource efficiency:** releases OpenCV video capture/writer resources.
- **Error handling:** invalid inputs and unsupported operations produce actionable errors.

## Technology Stack
- Python 3.10+
- OpenCV
- NumPy
- Pytest

## Repository Structure
```text
Smart-CV-Image-Analyzer/
├── README.md
├── statement.md
├── requirements.txt
├── main.py
├── src/
│   ├── preprocessing.py
│   ├── object_detection.py
│   ├── shape_detection.py
│   ├── image_analysis.py
│   ├── video_analysis.py
│   └── report_generator.py
├── tests/
│   └── test_modules.py
└── docs/
    ├── architecture.md
    ├── workflow.md
    ├── class_design.md
    └── testing.md
```

## Setup
```bash
python -m venv .venv
```

### Windows
```bash
.venv\\Scripts\\activate
```

### macOS/Linux
```bash
source .venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage
### Complete image analysis
```bash
python main.py image --input input/sample.jpg --output output
```

This creates edge, shape, and face-detection images plus `analysis_report.json`.

### Preprocessing
```bash
python main.py preprocess --input input/sample.jpg --operation edges --output output/edges.jpg
```

Supported operations: `resize`, `gray`, `blur`, `threshold`, `edges`.

### Shape detection
```bash
python main.py shapes --input input/sample.jpg --output output/shapes.jpg
```

### Face detection
```bash
python main.py detect --input input/sample.jpg --output output/detected.jpg
```

### Video motion analysis
```bash
python main.py video --input input/sample.mp4 --output output/motion.mp4
```

## Testing
Run:
```bash
pytest -q
```

The test suite covers image-statistic extraction, preprocessing output creation, and contour classification.

## Academic Alignment
The implementation demonstrates computer vision concepts including image representation, preprocessing, filtering, thresholding, edge detection, contours, object detection, feature/statistical analysis, and video processing.

Architecture, workflow, sequence, component design, and testing documentation are available in `docs/`.
