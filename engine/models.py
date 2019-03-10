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
    model = learner.io.load(config.weights_path('edsr-x4'))

    # Download source image from Azure
    source_filename = request['image']['original']['filename']
    source_image = azure.download_image('originalimages', source_filename)

    # Predict enhanced image
    enhanced_image = learner.enhance(model, source_image)

    # Clear model from GPU memory
    del model
    keras.backend.clear_session()

    # Upload enhanced image to Azure
    enhanced_filename = request['id'] + '-x4' + '.png'
    azure.upload_image(enhanced_image, 'enhancedimages', enhanced_filename)

    return jsonify(
        {
            'id': request['id'],
            'name': request['name'],
            'uploaded': request['uploaded'],
            'image': {
                'original': request['image']['original'],
                'enhanced': {
                    'filename': enhanced_filename,
                    'width': None,
                    'height': None,
                    'multiplier': '4x',
                    'fixArtifacts': False
                }
            }
        }
    )
