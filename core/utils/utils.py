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
