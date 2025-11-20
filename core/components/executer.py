from langchain_core.runnables import RunnableLambda
from core.utils.exec import run_agent_code

def execute(data):
    code_res = run_agent_code(data['code'], data['project'])
    data.update(code_res)
    data['activate_prompt'] = 2
    return data


executer = RunnableLambda(execute)
