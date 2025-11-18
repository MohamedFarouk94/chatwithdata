import json


get_current_project = lambda:None # temp


def load_json_list(filename):
    with open(f'{get_current_project()}/{filename}', 'r') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = []
    return data


def load_models_descriptions():
    return load_json_list('models.json')

def load_plots_description():
    return load_json_list('plots.json')