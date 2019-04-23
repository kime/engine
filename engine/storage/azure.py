import io

from PIL import Image
from azure.storage.blob import BlockBlobService

from engine import config
from engine.util.io import image_to_bytes


def download_image(container, blob_name):
    """

    :param container: name of an existing storage container
    :param blob_name: name of the blob containing the image
    :return: a PIL Image object
    """
    account_name, access_key = config.azure_storage()
    blob_service = BlockBlobService(account_name, access_key)
    blob = blob_service.get_blob_to_bytes(container, blob_name)
    img = Image.open(io.BytesIO(blob.content))
    return img.convert('RGB') if img.mode != 'RGB' else img


def upload_image(image, container, blob_name):
    """

    :param image: a PIL Image object
    :param container: name of an existing storage container
    :param blob_name: name of the blob to save the image as
    :return: ETag and last modified properties for the Block Blob
    """
    account_name, access_key = config.azure_storage()
    blob_service = BlockBlobService(account_name, access_key)
    return blob_service.create_blob_from_bytes(container, blob_name, image_to_bytes(image))
