from langchain_core.runnables import RunnableLambda

def end_query(data):
    return data


query_ender = RunnableLambda(end_query)
