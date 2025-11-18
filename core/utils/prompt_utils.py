import json
from core.controllers.project import get_current_project


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


def get_python_imports():
    python_imports = """
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
"""
    return python_imports
