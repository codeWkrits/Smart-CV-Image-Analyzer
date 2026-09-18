# Smart Image Analysis and Object Detection System Using Computer Vision

A modular Python + OpenCV academic project that runs completely from the command line. It processes images and videos through multiple computer vision pipelines and produces annotated outputs plus structured analysis data.

## Author
**Kriti Kumari**

## Project Overview
The system provides a practical computer vision workflow for:
1. Image preprocessing
2. Face/object detection
3. Geometric shape detection
4. Image analytics and JSON reporting
5. Video motion analysis

No GUI, API key, database, or external service is required.

## Functional Requirements
- Accept a valid image or video path.
- Validate that the input exists and can be read.
- Run image preprocessing operations.
- Detect faces using an OpenCV Haar cascade.
- Detect basic geometric shapes using contours.
- Calculate image dimensions and intensity statistics.
- Detect motion regions in video.
- Save processed outputs and a JSON analysis report.

## Non-Functional Requirements
- **Performance:** use focused processing pipelines without unnecessary repeated computation.
- **Usability:** simple CLI commands with clear help and status messages.
- **Reliability:** validate input files and media streams before processing.
- **Maintainability:** separate functions by computer vision responsibility.
- **Resource efficiency:** release OpenCV video capture and writer resources.
- **Error handling:** convert invalid input and processing failures into readable CLI errors.

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
├── input/
│   └── sample.ppm
├── src/
│   ├── __init__.py
│   ├── preprocessing.py
│   ├── object_detection.py
│   ├── shape_detection.py
│   ├── image_analysis.py
│   ├── video_analysis.py
│   └── report_generator.py
├── tests/
│   ├── __init__.py
│   └── test_modules.py
└── docs/
    ├── objectives.md
    ├── architecture.md
    ├── workflow.md
    ├── class_design.md
    ├── design_decisions.md
    ├── implementation.md
    ├── results.md
    └── testing.md
```

## Step-by-Step Setup

### 1. Install Python
Install Python 3.10 or newer and confirm:
```bash
python --version
```

### 2. Clone the repository
```bash
git clone https://github.com/codeWkrits/Smart-CV-Image-Analyzer.git
cd Smart-CV-Image-Analyzer
```

### 3. Create an isolated environment
```bash
python -m venv .venv
```

### 4. Activate the environment

Windows:
```bash
.venv\\Scripts\\activate
```

macOS/Linux:
```bash
source .venv/bin/activate
```

### 5. Install dependencies
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 6. Configuration
No external credentials or API keys are required. Input media and output locations are supplied as command-line arguments.

## Run the Project

### Complete image analysis
The repository contains `input/sample.ppm`, so the evaluator can run the project immediately:
```bash
python main.py image --input input/sample.ppm --output output
```

Expected outputs:
- `output/edges.jpg`
- `output/shapes.jpg`
- `output/detected.jpg`
- `output/analysis_report.json`

### Individual preprocessing
```bash
python main.py preprocess --input input/sample.ppm --operation edges --output output/edges.jpg
```
Supported operations: `resize`, `gray`, `blur`, `threshold`, `edges`.

### Shape detection
```bash
python main.py shapes --input input/sample.ppm --output output/shapes.jpg
```

### Face detection
```bash
python main.py detect --input input/sample.ppm --output output/detected.jpg
```

### Video motion analysis
Use any readable video file:
```bash
python main.py video --input input/sample.mp4 --output output/motion.mp4
```

## Testing

Install the dependencies, then run:
```bash
pytest -q
```

The tests cover:
- image-statistic extraction;
- preprocessing output creation; and
- contour-based shape classification.

## Academic Alignment
The project applies computer vision concepts including image representation, preprocessing, Gaussian filtering, thresholding, Canny edge detection, contours, polygon approximation, Haar-cascade detection, image statistics, frame differencing, and structured reporting.

Detailed project artefacts are in `docs/`, including the problem statement, objectives, architecture, workflow, UML-style diagrams, design rationale, implementation details, results, and testing approach.
