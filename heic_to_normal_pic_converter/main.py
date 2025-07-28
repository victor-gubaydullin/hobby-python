import os
from PIL import Image
from pillow_heif import register_heif_opener

register_heif_opener()

file_name = "example.HEIC"  # Replace with your HEIC file name
output_format = "PNG"  # Change to desired output format (e.g., "JPEG")

input_path = os.path.join(os.getcwd(), "heic_to_normal_pic_converter", file_name)
output_path = os.path.join(os.getcwd(), file_name.replace('.HEIC', f'.{output_format}'))

if not os.path.exists(input_path):
    raise FileNotFoundError(f"The file {input_path} does not exist.")
else:
    image = Image.open(input_path)
    image.save(output_path)

    print(f"Converted and saved to: {output_path}")

