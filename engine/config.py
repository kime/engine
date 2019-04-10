import json

CONFIG_PATH = "config.json"


def azure_storage():
    with open(CONFIG_PATH, 'r') as config_file:
        config = json.load(config_file)
    return config['storage']['azure']['account_name'], \
           config['storage']['azure']['access_key']


def weights_path(model):
    """

    :param model:
    :return:
    """
    with open(CONFIG_PATH, 'r') as config_file:
        config = json.load(config_file)
    return config["path"]["weights"][model]