import os

# Configuration reading utility
def ReadConfig(key = None):
    import configparser
    config = configparser.ConfigParser()

    # Get the project root (parent of 'core' directory)
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(project_root, 'config.cfg')

    # Read the config file and remove inline comments so values like
    # "excel # Options: csv, excel" don't break the value parsing.
    raw = open(config_path, 'r', encoding='utf-8').read()
    cleaned_lines = []
    for line in raw.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith(('#', ';')):
            continue
        # remove inline comments starting with # or ;
        for c in ('#', ';'):
            if c in line:
                line = line.split(c, 1)[0]
        cleaned_lines.append(line.rstrip())

    cleaned = '\n'.join(cleaned_lines)
    config.read_string('[DEFAULT]\n' + cleaned)
    if key is None:
        return config['DEFAULT']
    val = config['DEFAULT'].get(key)
    return val.strip() if val is not None else None

def ReadAllConfig():
    return {
        'FILE_EXCEL': ReadConfig('FILE_EXCEL'),
        'EXPORT_DIR': ReadConfig('EXPORT_DIR'),
        'HOST': ReadConfig('HOST'),
        'PORT': ReadConfig('PORT'),
    }
