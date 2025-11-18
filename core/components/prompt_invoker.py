from langchain_core.runnables import RunnableLambda
from core.prompts.prompts import prompt_template_1, prompt_template_2
from core.utils.prompt_utils import get_python_imports


prompt_templates = [None, prompt_template_1, prompt_template_2]

def invoke_prompt(data):
    data['prompt'] = prompt_templates[data['activate_prompt']].format(
        project=data['project'],
        data_path=data['data_path'],
        cat_cols=data['cat_cols'],
        columns_description=data['columns_description'],
        models_descriptions=data['models_description'],
        plots_descriptions=data['plots_description'],
        history=data['history'],
        python_imports=get_python_imports(),
        user_message=data['user_message'],
        generated_code=data['code'],
        code_output=data['stdout'],
    )

    return data


prompt_invoker = RunnableLambda(invoke_prompt)
