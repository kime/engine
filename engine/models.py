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
    if request['fix_artifacts']:
        model = learner.io.load(config.weights_path('wdsr-x4-fa'))
    else:
        model = learner.io.load(config.weights_path('edsr-x4'))

    # Download source image from Azure
    source_blob_name = request['image']['original']['blob_name']
    source_image = azure.download_image('originalimages', source_blob_name)

    # Predict enhanced image
    enhanced_image = learner.enhance(model, source_image)

    # Clear model from GPU memory
    del model
    keras.backend.clear_session()

    # Upload enhanced image to Azure
    enhanced_blob_name = source_blob_name + '-x4' + '.png'
    azure.upload_image(enhanced_image, 'enhancedimages', enhanced_blob_name)

    return jsonify(
        {
            'id': request['id'],
            'image': {
                'original': request['image']['original'],
                'enhanced': {
                    'blob_name': enhanced_blob_name,
                    'width': None,
                    'height': None,
                }
            }
        }
    )
