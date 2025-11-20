def parse_xml(x):
    if '<think>' not in x:
        x = '<think></think>/n' + x
        
    if '<code>' not in x:
        x += '\n<code></code>'

    a, b = x.strip().split('</think>')
    
    assert a.startswith('<think>'), "The <think> tag is not found"
    think = a[len('<think>'):].strip()

    c, d = b.strip().split('</instant_response>')

    assert c.startswith('<instant_response>'), "The <instant_response> tag is not found"
    instant_response = c[len('<instant_response>'):].strip()

    e = d.strip().split('</code>')[0]

    assert e.startswith('<code>'), "The <code> tag is not found"
    code = e[len('<code>'):].strip()

    return {
        'think': think,
        'instant_response': instant_response,
        'code': code
    }


def get_chat_segment(data):
    chat_segment = []

    chat_segment.append({'role': 'user', 'content': data['user']})
    chat_segment.append({'role': 'think', 'content': data['think_1']})
    
    if data.get('code', None):
        chat_segment.append({'role': 'code', 'content': data['code']})

    if data.get('stdout', None):
        chat_segment.append({'role': 'stdout', 'content': data['code']})

    if data.get('think_2', None):
        chat_segment.append({'role': 'think', 'content': data['think_2']})

    chat_segment.append({'role': 'assistant', 'content': data['assistant']})

    return chat_segment
