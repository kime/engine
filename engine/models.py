import keras
from flask import jsonify

from engine import learner
from engine.storage import azure
from engine import config


def enhance(request):
    """

    :param request:
    :return:
    """
    # Load learner from weights
    if request['fixArtifacts']:
        model = learner.io.load(config.weights_path('wdsr-x4-fa'))
    else:
        model = learner.io.load(config.weights_path('edsr-x4'))

    try:
        # Download source image from Azure
        source_blob_name = request['originalImage']['blobName']
        source_image = azure.download_image('originalimages', source_blob_name)

        # Predict enhanced image
        enhanced_image = learner.enhance(model, source_image)

        # Upload enhanced image to Azure
        enhanced_blob_name = source_blob_name + '-x4' + '.png'
        azure.upload_image(enhanced_image, 'enhancedimages', enhanced_blob_name)
    finally:
        # Clear model from GPU memory
        del model
        keras.backend.clear_session()

    return jsonify(
        {
            'id': request['id'],
            'enhancedImage': {
                'blobName': enhanced_blob_name,
                'width': enhanced_image.size[0],
                'height': enhanced_image.size[1],
            }
        }
    )
