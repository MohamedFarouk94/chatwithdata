import json
from core.utils.paths import get_project_directory
from .project import get_current_project


HISTORY = []


def load_history():
    global HISTORY
    project_dir = get_project_directory(get_current_project())
    
    with open(project_dir / 'history.json', 'r') as f:
        HISTORY = json.load(f)


def save_history():
    global HISTORY
    project_dir = get_project_directory(get_current_project())

    with open(project_dir / 'history.json', 'w') as f:
        json.dump(HISTORY, f, indent=4)


def add_to_history(chat_segmant):
    global HISTORY
    HISTORY.extend(chat_segmant)


def get_full_history():
    global HISTORY
    return HISTORY


def get_history():
    global HISTORY
    return [m for m in HISTORY if m['role'] in ('user', 'assistant')]
