import json

CONFIG_PATH = "config.json"
with open(CONFIG_PATH, 'r') as config_file:
    config = json.load(config_file)


def backend_credentials():
    return config['backend']['username'], config['backend']['secret_hash']


def azure_storage():
    return config['storage']['azure']['account_name'], \
           config['storage']['azure']['access_key']


def weights_path(model):
    return config["path"]["weights"][model]
