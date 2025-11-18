import io, contextlib, traceback

import re
import numpy as np
import pandas as pd
import math
import time
import matplotlib.pyplot as plt
import seaborn as sns
import json
import sklearn.metrics as metrics
from sklearn.model_selection import train_test_split
from catboost import CatBoostClassifier, CatBoostRegressor


namespace = {
    're': re,
    'np': np,
    'pd': pd,
    'math': math,
    'plt': plt,
    'sns': sns,
    'CatBoostClassifier': CatBoostClassifier,
    'CatBoostRegressor': CatBoostRegressor,
    'json': json,
    'time': time,
    # 'add_model': add_model, # LATER
    # 'add_plot': add_plot, # LATER
    'train_test_split': train_test_split,
    'metrics': metrics
}

def run_agent_code(code, work_dir=''):
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
            exec(code, namespace, namespace)
        return {"ok": True, "stdout": buf.getvalue(), "error": None}

    except Exception:
        return {"ok": False, "stdout": buf.getvalue(), "error": traceback.format_exc()}
