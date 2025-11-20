from langchain_core.runnables import RunnableLambda
from core.prompts.prompts import prompt_template_1, prompt_template_2
from core.utils.prompt import get_python_imports, load_models_descriptions, load_plots_description


prompt_templates = [None, prompt_template_1, prompt_template_2]

def invoke_prompt(data):
    data['prompt'] = prompt_templates[data['activate_prompt']].format(
        cat_cols=data['cat_cols'],
        columns_description=data['columns_description'],
        models_descriptions=load_models_descriptions(data['project']),
        plots_descriptions=load_plots_description(data['project']),
        history=data['history'],
        python_imports=get_python_imports(),
        user_message=data['user_message'],
        generated_code=data['code'],
        code_output=data['stdout'],
    )

    return data


prompt_invoker = RunnableLambda(invoke_prompt)
