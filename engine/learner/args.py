from argparse import ArgumentParser


def get_args():
    parser = ArgumentParser(description="Kime Engine: CLI Inference")

    # Predict options
    parser.add_argument('--learner', default='data/weights/edsr-x4-v1/edsr-16-x4-gen.h5',
                        help='path to file containing learner weights')
    parser.add_argument('--input', type=str, default='data/images/fuji.jpg',
                        help='path to input image')
    parser.add_argument('--output', type=str, default='data/images/',
                        help='directory for saving output image')
    parser.add_argument('--output-format', type=str, default='png', choices=['jpg', 'png'],
                        help='output image file format')

    # Export options
    parser.add_argument('--export-path', default='data/serveables/edsr-x4/',
                        help='path for exporting the serveable learner')
    parser.add_argument('--version', default='1')

    parser.add_argument()
    args = parser.parse_args()
    return args
