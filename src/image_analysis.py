import cv2
import numpy as np


def analyze_image(path):
    image = cv2.imread(str(path))
    if image is None:
        raise ValueError(f"Unable to read image: {path}")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return {
        "file": str(path),
        "width": int(image.shape[1]),
        "height": int(image.shape[0]),
        "channels": int(image.shape[2]) if image.ndim == 3 else 1,
        "mean_intensity": round(float(np.mean(gray)), 2),
        "std_intensity": round(float(np.std(gray)), 2),
        "min_intensity": int(np.min(gray)),
        "max_intensity": int(np.max(gray)),
    }
