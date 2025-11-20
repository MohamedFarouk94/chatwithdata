from langchain_core.runnables import RunnableLambda
from core.utils.utils import parse_xml


def parse(data):
    parsed_output = parse_xml(data['response'])
    data[f'think_{data['activate_prompt']}'] = parsed_output['think']
    data['assistant'] = parsed_output['instant_response']
    data['code'] = parsed_output['code']
    return data


parser = RunnableLambda(parse)
