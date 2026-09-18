import cv2
from pathlib import Path


def detect_faces(input_path, output_path):
    image = cv2.imread(str(input_path))
    if image is None:
        raise ValueError(f"Unable to read image: {input_path}")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )
    if cascade.empty():
        raise RuntimeError("OpenCV Haar cascade could not be loaded")

    objects = cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
    )
    for (x, y, w, h) in objects:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(image, "Face", (x, max(y - 8, 15)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    if not cv2.imwrite(str(output), image):
        raise RuntimeError(f"Unable to write output: {output}")
    return len(objects)
