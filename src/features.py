import cv2
import numpy as np

def extract_features(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    blur = cv2.Laplacian(gray, cv2.CV_64F).var()
    brightness = np.mean(gray)
    contrast = np.std(gray)

    return {
        "blur": float(blur),
        "brightness": float(brightness),
        "contrast": float(contrast)
    }