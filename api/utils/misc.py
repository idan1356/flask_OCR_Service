import base64
import io
from typing import List

from PIL import Image, ImageDraw


def add_sentence_outline_to_image(image_bytes: bytes, rectangle_list: List, image_file_extension: str) -> bytes:
    image = Image.open(io.BytesIO(image_bytes))
    draw = ImageDraw.Draw(image)

    for entry in rectangle_list:
        coordinates = [tuple(point) for point in entry]
        draw.polygon(coordinates, outline=(0, 255, 0), width=2)

    output_image_io = io.BytesIO()
    image.save(output_image_io, format=image_file_extension)
    output_image_io.seek(0)
    output_image_bytes = output_image_io.read()

    return output_image_bytes


def image_bytes_to_base64(image_bytes: bytes) -> str:
    return base64.b64encode(image_bytes).decode("utf-8")


def get_file_extension_from_name(file_name: str) -> str:
    return file_name.split('.')[1]
