from langchain_core.runnables import RunnableLambda
from core.utils.utils import parse_xml


def parse(data):
    parsed_output = parse_xml(data['response'])
    data.update(parsed_output)
    return data


parser = RunnableLambda(parse)
