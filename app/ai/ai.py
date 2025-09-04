from dotenv import load_dotenv
from loguru import logger

import openai
import os


load_dotenv()


async def create_client_openai() -> openai.AsyncClient:
    '''
    Создает клиента OpenAI по API ключу из .env
    '''

    try:
        return await openai.AsyncOpenAI(api_key=os.dotenv('OPENAI_API_KEY'))
    except openai.APIStatusError as e:
        logger.error('Ошибка инициализации OpenAI клиента, '
                     f'OPENAI_API_KEY установлен не корректно. \n{e}')
    except Exception as e:
        logger.error('Неизвестная ошибка при инициализации')


async def text_processing_using_openai(text: str) -> str:
    '''
    Преобразует полученный текст с помощью OpenAI
    '''

    client = await create_client_openai()
    try:
        response = await client.chat.completions.create(
            model='gpt-4o-mini',
            messages=[
                {'role': 'system',
                 'content': ('Вы — полезный помощник, '
                             'который отлично перефразирует текст, '
                             'делая его более лаконичным и профессиональным.')},
                {'role': 'user',
                 'content': (f'перефразируйте следующий текст:\n\n"{text}"')}
            ],
            max_tokens=100,
            temperature=0.6,
            n=1,
        )
        result = response.choices[0].message.content
        logger.info(f'Обработаны данные {result}')
        return result
    except openai.APIConnectionError as e:
        logger.error('Ошибка соединения с API OpenAI: {e}')
    except openai.RateLimitError as e:
        logger.error('Превышен лимит запросов: {e}')
    except openai.AuthenticationError as e:
        logger.error('Ошибка аутентификации: {e}')
    except openai.APIStatusError as e:
        logger.error(f'Ошибка API (код {e.status_code}): {e.response}')
    except Exception as e:
        logger.error('Произошла непредвиденная ошибка: {e}')
