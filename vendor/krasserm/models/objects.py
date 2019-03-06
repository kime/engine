import tensorflow as tf
from keras import backend as K
from keras.losses import mean_absolute_error

from vendor.krasserm.models import weightnorm


def _crop_hr_in_training(hr, sr):
    """
    Remove margin of size scale*2 from hr in training phase.

    The margin is computed from size difference of hr and sr
    so that no explicit scale parameter is needed. This is only
    needed for WDSR models.
    """

    margin = (tf.shape(hr)[1] - tf.shape(sr)[1]) // 2

    # crop only if margin > 0
    hr_crop = tf.cond(tf.equal(margin, 0),
                      lambda: hr,
                      lambda: hr[:, margin:-margin, margin:-margin, :])

    hr = K.in_train_phase(hr_crop, hr)
    hr.uses_learning_phase = True
    return hr, sr


def mae(hr, sr):
    hr, sr = _crop_hr_in_training(hr, sr)
    return mean_absolute_error(hr, sr)


def psnr(hr, sr):
    hr, sr = _crop_hr_in_training(hr, sr)
    return tf.image.psnr(hr, sr, max_val=255)


custom_objects = {
    'tf': tf,
    'AdamWithWeightnorm': weightnorm.AdamWithWeightnorm,
    'mae': mae,
    'psnr': psnr
}

backwards_compat_objects = {
    'mae_scale_2': mae,
    'mae_scale_3': mae,
    'mae_scale_4': mae,
    'psnr_scale_2': psnr,
    'psnr_scale_3': psnr,
    'psnr_scale_4': psnr
}