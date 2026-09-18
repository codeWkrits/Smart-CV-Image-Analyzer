# Design Decisions and Rationale

## Python + OpenCV
Python provides concise implementation while OpenCV supplies standard image and video-processing primitives required by the course domain.

## Command-Line Interface
The evaluation requires terminal execution without a GUI-based setup, so the interface is based on `argparse`.

## Modular Architecture
Each major CV task is isolated in a separate module. This makes the code easier to test, extend, and maintain.

## Classical Computer Vision Methods
The project uses grayscale conversion, Gaussian blur, thresholding, Canny edges, contours, polygon approximation, Haar cascades, and frame differencing. These methods are transparent and practical for an academic demonstration.

## No Database or External Service
The system is intentionally file-based. It does not require credentials, API keys, or network services. Configuration is provided through command-line arguments.
