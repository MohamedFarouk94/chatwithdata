import json


def load_json_list(filename):
    with open(filename, 'r') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = []
    return data


def load_models_descriptions(project):
    return load_json_list(f'projects/{project}/models.json')


def load_plots_description(project):
    return load_json_list(f'projects/{project}/plots.json')


def get_python_imports():
    python_imports =\
"""
import json
import time
import math
import numpy as np
import pandas as pd
import sklearn.metrics as metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
from catboost import CatBoostClassifier, CatBoostRegressor
from utils import add_model, add_plot
from paths import project_dir
"""
    # These imports will not be actually imported, but the LLM will be told to act as so.
    return python_imports
