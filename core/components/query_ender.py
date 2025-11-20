from langchain_core.runnables import RunnableLambda
from core.utils.utils import get_chat_segment
from core.controllers.history import add_to_history, save_history

def end_query(data):
    chat_segmant = get_chat_segment(data)
    add_to_history(chat_segmant)
    save_history()
    return data


query_ender = RunnableLambda(end_query)
