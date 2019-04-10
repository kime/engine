import os

import keras
import tensorflow as tf

from engine.learner.args import get_args
from vendor.krasserm.models.objects import custom_objects, backwards_compat_objects


def export(model, export_path, version):
    """

    :param model:
    :param export_path:
    :param version:
    :return:
    """
    export_path = os.path.join(export_path, str(version))
    if os.path.isdir(export_path):
        raise IOError('Export directory is not empty')

    tf.saved_model.simple_save(
        keras.backend.get_session(),
        export_path,
        inputs={'input_image': model.input},
        outputs={t.name: t for t in model.outputs})


def load(path):
    """

    :param path:
    :return:
    """
    return keras.models.load_model(filepath=path,
                                   custom_objects={**custom_objects,
                                                   **backwards_compat_objects}
                                   )


if __name__ == '__main__':
    # Get commandline args
    args = get_args()

    # Load learner from weights
    model = load(args.model)

    # Export SavedModel object
    export(model, args.export_path, args.version)
