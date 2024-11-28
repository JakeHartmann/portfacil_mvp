import cv2
import tempfile


def auto_detect_and_remove_bars(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError(f"Erro ao carregar a imagem do caminho: {image_path}")

    edges = cv2.Canny(img, 100, 200)

    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    top_crop_height = 0
    bottom_crop_height = img.shape[0]

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)

        # Se o contorno estiver no topo da imagem, ajustar o top_crop_height
        if y < img.shape[0] // 10:  # Considerar apenas a parte superior
            top_crop_height = max(top_crop_height, y + h)
        
        # Se o contorno estiver na parte inferior, ajustar o bottom_crop_height
        if y > img.shape[0] * 0.9:  # Considerar apenas a parte inferior
            bottom_crop_height = min(bottom_crop_height, y)

    img_color = cv2.imread(image_path)
    if img_color is None:
        raise ValueError(f"Erro ao carregar a imagem colorida do caminho: {image_path}")
    
    # Recorta a área entre a barra superior e a barra inferior que foram detectadas
    cropped_img = img_color[top_crop_height:bottom_crop_height, :]
    with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as temp_file:
        temp_file_path = temp_file.name
        cv2.imwrite(temp_file_path, cropped_img)

    return temp_file_path
