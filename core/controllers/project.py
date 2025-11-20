import json
from pathlib import Path
from core.utils.paths import PROJECTS_DIR


CURRENT_PROJECTS = {}

def get_current_project(user='admin'):
    global CURRENT_PROJECTS
    return CURRENT_PROJECTS.get(user, '')


def set_current_project(user='admin', project='project_1'):
    global CURRENT_PROJECTS
    CURRENT_PROJECTS[user] = project


def create_project(project, df, cat_cols, columns_description):
    project_dir = PROJECTS_DIR / project
    project_dir.mkdir(parents=True, exist_ok=True)

    models_dir = project_dir / 'ai_generated_models'
    models_dir.mkdir(parents=True, exist_ok=True)

    plots_dir = project_dir / 'ai_generated_plots'
    plots_dir.mkdir(parents=True, exist_ok=True)

    df.to_csv(project_dir / 'df.csv', index=False)

    with open(project_dir / 'cat_cols.json', 'w') as f:
        json.dump(cat_cols, f, indent=4)

    with open(project_dir / 'columns_description.json', 'w') as f:
        json.dump(columns_description, f, indent=4)
    
    with open(project_dir / 'models.json', 'w') as f:
        json.dump([], f, indent=4)

    with open(project_dir / 'plots.json', 'w') as f:
        json.dump([], f, indent=4)

    with open(project_dir / 'history.json', 'w') as f:
        json.dump([], f, indent=4)

    with open(project_dir / 'ai_generated_models/models.txt', 'w') as f:
        f.write('Here should be catboost models, but they will not be pushed to github!!')
