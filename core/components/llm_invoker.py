from langchain_core.runnables import RunnableLambda
from core.models.groq import llm


def invoke_llm(data):
    data['response'] = llm.invoke(data['prompt'])
    return data


llm_invoker = RunnableLambda(invoke_llm)
