import cv2
import numpy as np
import tempfile


def preprocess_image(image_path):
    # Carregar a imagem em escala de cinza
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError(f"Erro ao carregar a imagem do caminho: {image_path}")

    # Aplicar threshold para binarizar a imagem
    _, binary_img = cv2.threshold(img, 170, 255, cv2.THRESH_BINARY_INV)

    # Aplicar operação morfológica para limpar a imagem
    kernel = np.ones((1, 1), np.uint8)
    cleaned_img = cv2.morphologyEx(binary_img, cv2.MORPH_OPEN, kernel)

    # Criar um arquivo temporário para salvar a imagem processada
    with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as temp_file:
        processed_image_path = temp_file.name
        cv2.imwrite(processed_image_path, cleaned_img)

    return processed_image_path
