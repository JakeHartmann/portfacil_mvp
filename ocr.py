import os
import pytesseract

# Obtém o caminho do Tesseract de uma variável de ambiente
tesseract_path = os.getenv("TESSERACT_CMD", r'C:\Program Files\Tesseract-OCR\tesseract.exe')
pytesseract.pytesseract.tesseract_cmd = tesseract_path

def extract_text_from_image(image_path) -> str:
    custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=$%,.0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    text = pytesseract.image_to_string(image_path, config=custom_config)
    return text
