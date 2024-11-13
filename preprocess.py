import cv2
import numpy as np


def preprocess_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    _, binary_img = cv2.threshold(img, 170, 255, cv2.THRESH_BINARY_INV)
    kernel = np.ones((1, 1), np.uint8)
    cleaned_img = cv2.morphologyEx(binary_img, cv2.MORPH_OPEN, kernel)
    processed_image_path = "sample_data/processed_image.png"
    cv2.imwrite(processed_image_path, cleaned_img)
    return processed_image_path
