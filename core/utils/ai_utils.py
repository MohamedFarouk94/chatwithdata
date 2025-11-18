import os
import json


def add_item(path, descr, filename, path_key, descr_key):
    data = []
    project = path.split('/')[1]
    if os.path.exists(filename):
        with open(f'projects/{project}/filename', 'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    
    data.append({
        path_key: path,
        descr_key: descr
    })

    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def add_model(model_path, model_descr):
    add_item(model_path, model_descr, 'models.json', 'model_path', 'model_descr')


def add_plot(plot_path, plot_descr):
    add_item(plot_path, plot_descr, 'plots.json', 'plot_path', 'plot_descr')
