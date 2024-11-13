from preprocess import preprocess_image
from status_bar import auto_detect_and_remove_bars
from ocr import extract_text_from_image
# from layout_detection import detect_layout
from save_to_file import save_to_excel


def main_pipeline(image_path):
    processed_image_path = preprocess_image(image_path)

    processed_image_path = auto_detect_and_remove_bars(processed_image_path, 'sample_data/processed_image.png')

    extracted_text = extract_text_from_image(processed_image_path)
    print(extracted_text)

    # Opcional
    # layout_data = detect_layout(image_path)
    # print(layout_data)

    save_to_excel(extracted_text, output_path="sample_data/output.xlsx")


if __name__ == "__main__":
    main_pipeline("sample_data/sample_image_poc.jpg")
