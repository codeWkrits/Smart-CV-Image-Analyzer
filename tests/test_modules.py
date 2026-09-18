import cv2
import numpy as np

from src.preprocessing import preprocess_image
from src.image_analysis import analyze_image
from src.shape_detection import classify_contour


def make_image(tmp_path):
    path = tmp_path / "test.jpg"
    image = np.zeros((100, 100, 3), dtype=np.uint8)
    cv2.rectangle(image, (20, 20), (80, 80), (255, 255, 255), -1)
    assert cv2.imwrite(str(path), image)
    return path


def test_analyze_image(tmp_path):
    result = analyze_image(make_image(tmp_path))
    assert result["width"] == 100
    assert result["height"] == 100
    assert result["channels"] == 3


def test_preprocess_edges(tmp_path):
    src = make_image(tmp_path)
    output = tmp_path / "edges.jpg"
    result = preprocess_image(src, output, "edges")
    assert result is not None
    assert output.exists()


def test_shape_classifier():
    triangle = np.array([[[0, 0]], [[10, 0]], [[5, 10]]], dtype=np.int32)
    assert classify_contour(triangle) == "Triangle"
