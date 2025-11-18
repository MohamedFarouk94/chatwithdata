from langchain_core.runnables import RunnableLambda


def start_query(data):
    data['activate_prompt'] = 1
    return data


query_starter = RunnableLambda(start_query)
