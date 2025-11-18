from langchain_core.runnables import RunnableLambda
from core.prompts.prompts import prompt_template_1, prompt_template_2


prompt_templates = [None, prompt_template_1, prompt_template_2]

python_imports="""
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

def invoke_prompt(data):
    data['prompt'] = prompt_templates[data['activate_prompt']].format(
        project=data['project'],
        data_path=data['data_path'],
        cat_cols=data['cat_cols'],
        columns_description=data['columns_description'],
        models_descriptions=data['models_description'],
        plots_descriptions=data['plots_description'],
        history=data['history'],
        python_imports=python_imports,
        user_message=data['user_message'],
        generated_code=data['code'],
        code_output=data['stdout'],
    )

    return data


prompt_invoker = RunnableLambda(invoke_prompt)
