import re


async def parse_amocrm_webhook_data(form_data: dict) -> dict:
    '''
    Функция обрабатывает полученные данные с вебхука амосрм.
    '''
    result_data = {}

    for key, value in form_data.items():
        key = ' '.join(re.sub(r'\[|\]', r' ', key).split())
        result_data[key] = value
    return result_data
