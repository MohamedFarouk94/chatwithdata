from core.components.chains import chain1234, chain52346, chain6


def run(data):
    data = chain1234.invoke(data)

    if data['code']:
        data = chain52346.invoke(data)
    else:
        data = chain6.invoke(data)

    return data
