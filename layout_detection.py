# from deepdoctection import detect  # Descomentar ao configurar DeepDoctection


def detect_layout(image_path):
    # layout_detector = detect.load_default()
    layout_data = []
    # doc = layout_detector.from_file(image_path)
    # for item in doc["layout"]:
    #     if item["label"] == "table":
    #         layout_data.append(item["box"])
    return layout_data
