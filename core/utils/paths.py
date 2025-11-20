from pathlib import Path


CORE_DIR = Path(__file__).resolve().parent.parent
PROJECTS_DIR = CORE_DIR / "projects"

def get_project_directory(project):
    global PROJECTS_DIR
    return PROJECTS_DIR / project
