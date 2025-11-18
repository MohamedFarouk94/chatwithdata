CURRENT_PROJECTS = {}

def get_current_project(user='admin'):
    global CURRENT_PROJECTS
    return CURRENT_PROJECTS.get(user, '')

def set_current_project(user='admin', project='project_1'):
    global CURRENT_PROJECTS
    CURRENT_PROJECTS[user] = project
