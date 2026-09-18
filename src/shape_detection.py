import cv2
from pathlib import Path


def classify_contour(contour):
    perimeter = cv2.arcLength(contour, True)
    if perimeter == 0:
        return "Unknown"
    approx = cv2.approxPolyDP(contour, 0.04 * perimeter, True)
    n = len(approx)
    if n == 3:
        return "Triangle"
    if n == 4:
        x, y, w, h = cv2.boundingRect(approx)
        ratio = w / float(h) if h else 0
        return "Square" if 0.90 <= ratio <= 1.10 else "Rectangle"
    if n > 6:
        return "Circle"
    return f"{n}-sided polygon"


def detect_shapes(input_path, output_path):
    image = cv2.imread(str(input_path))
    if image is None:
        raise ValueError(f"Unable to read image: {input_path}")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    count = 0
    for contour in contours:
        if cv2.contourArea(contour) < 100:
            continue
        count += 1
        x, y, w, h = cv2.boundingRect(contour)
        label = classify_contour(contour)
        cv2.drawContours(image, [contour], -1, (255, 0, 0), 2)
        cv2.putText(image, label, (x, max(y - 5, 15)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    if not cv2.imwrite(str(output), image):
        raise RuntimeError(f"Unable to write output: {output}")
    return count
