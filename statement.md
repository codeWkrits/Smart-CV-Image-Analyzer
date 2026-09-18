# Project Statement

## Problem Statement
Manual inspection of digital images and video is time-consuming and inconsistent. This project provides a lightweight computer vision pipeline that preprocesses media, detects faces, identifies geometric shapes, calculates image statistics, analyzes motion in video, and stores structured results.

## Scope
The system accepts image and video files through a command-line interface. It performs preprocessing, Haar-cascade face detection, contour-based shape detection, image analytics, and frame-difference motion analysis. It is intended for academic learning and demonstration.

## Target Users
- Computer vision students
- Developers learning OpenCV
- Academic project evaluators
- Users needing basic offline media analysis

## High-Level Features
1. Image preprocessing
2. Face/object detection
3. Shape detection
4. Image analytics and reporting
5. Video motion analysis

## Functional Requirements
- Accept valid image/video paths.
- Validate file existence and readability.
- Apply selected preprocessing operations.
- Detect faces using OpenCV Haar cascade.
- Detect basic geometric shapes using contours.
- Calculate image dimensions and intensity statistics.
- Detect moving regions in video frames.
- Save processed media and analysis reports.

## Non-Functional Requirements
- Performance: avoid unnecessary repeated processing.
- Usability: clear CLI commands and messages.
- Reliability: validate input and handle unreadable media.
- Maintainability: keep CV operations modular.
- Resource efficiency: release video resources correctly.
- Error handling: return actionable errors for invalid input.
