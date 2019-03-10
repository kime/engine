import os

import numpy as np
from PIL import Image

from engine import learner
from engine.util import io


def enhance(model, image):
    """

    :param model:
    :param image:
    :return:
    """
    sr = model.predict(np.expand_dims(image, axis=0))[0]
    sr = np.clip(sr, 0, 255).astype('uint8')
    return Image.fromarray(sr)


if __name__ == '__main__':
    # Get commandline args
    args = learner.get_args()

    # Load learner from weights
    model = learner.io.load(args.model)

    # Load image and enhance it
    output = enhance(model, io.load_image(args.input))

    # Save output to file
    os.makedirs(args.output, exist_ok=True)
    output_filename = '%s_sr.%s' % (os.path.splitext(os.path.split(args.input)[1])[0], args.output_format)
    output.save(os.path.join(args.output, output_filename))
