import cv2
from pathlib import Path


def load_image(path):
    image = cv2.imread(str(path))
    if image is None:
        raise ValueError(f"Unable to read image: {path}")
    return image


def preprocess_image(input_path, output_path, operation):
    image = load_image(input_path)
    if operation == "resize":
        result = cv2.resize(image, (640, 480))
    elif operation == "gray":
        result = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    elif operation == "blur":
        result = cv2.GaussianBlur(image, (5, 5), 0)
    elif operation == "threshold":
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, result = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    elif operation == "edges":
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        result = cv2.Canny(gray, 100, 200)
    else:
        raise ValueError(f"Unsupported operation: {operation}")

    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    if not cv2.imwrite(str(output), result):
        raise RuntimeError(f"Unable to write output: {output}")
    return result
