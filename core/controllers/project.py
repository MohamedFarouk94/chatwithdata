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


def create_project(project, df):
    project_dir = PROJECTS_DIR / project
    project_dir.mkdir(parents=True, exist_ok=True)

    models_dir = project_dir / 'ai_generated_models'
    models_dir.mkdir(parents=True, exist_ok=True)

    plots_dir = project_dir / 'ai_generated_plots'
    plots_dir.mkdir(parents=True, exist_ok=True)

    df.to_csv(project_dir / 'df.csv', index=False)

    with open(project_dir / 'models.json', 'w') as f:
        json.dump([], f, indent=4)

    with open(project_dir / 'plots.json', 'w') as f:
        json.dump([], f, indent=4)
