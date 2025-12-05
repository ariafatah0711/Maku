import os

class Color:
    RED = "#FF0000"
    GREEN = "#00FF00"
    BLUE = "#0000FF"
    YELLOW = "#FFFF00"
    BLACK = "#000000"
    WHITE = "#FFFFFF"
    GRAY = "#808080"
    ORANGE = "#FFA500"

def ReadConfig(key):
    import configparser
    config = configparser.ConfigParser()

    # Get the project root (parent of 'core' directory)
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(project_root, 'config.cfg')

    config.read_string('[DEFAULT]\n' + open(config_path).read())
    return config['DEFAULT'].get(key)
