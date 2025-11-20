import os
import json


def add_item(path, descr, filename, path_key, descr_key):
    data = []
    project_dir = path.parent.parent    # project / ai_generated_XXX / cbm_or_png_file
    if os.path.exists(filename):
        with open(project_dir / filename, 'r') as f:
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
