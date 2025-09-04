from loguru import logger


async def parse_amocrm_webhook_data(form_data: dict) -> str:
    '''
    Функция обрабатывает полученные данные с вебхука амосрм.
    '''

    statuses = {'add': 'Пользователь добавил информацию: ',
                'update': 'Пользователь обновил информцию: ',
                'delete': 'Пользователь удалил задачу: '}
    actions = {'0': 'Какое-то действие ', '1': 'Связаться ', '2': 'Встреча '}
    task_type = '0'

    for key, value in form_data.items():
        if 'task_type' in key:
            task_type = value
        if 'task' in key:
            if 'delete' in key:
                result = statuses['delete'] + value
            if 'text' in key:
                for status in statuses:
                    if status in key:
                        result = (statuses.get(status, '')
                                  + actions.get(task_type, 'Какое-то действие ')
                                  + value)
                break
    logger.info(f'Обработаны данные: {result}')
    return result
