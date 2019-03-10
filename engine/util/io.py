import io

from PIL import Image


def load_image(path):
    """
    Load image to memory from the filesystem
    :param path: path to image file
    :return: a PIL Image object
    """
    img = Image.open(path)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    return img


def image_to_bytes(image, format='PNG'):
    """

    :param image: a PIL Image object
    :param format: optional format override for file extension
    :return: a Bytes array of the image
    """
    image_bytes = io.BytesIO()
    image.save(image_bytes, format=format)
    return image_bytes.getvalue()
