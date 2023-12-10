import requests
import pandas as pd

class BankiApp:
    def __init__(self):
        self.base_url = 'https://www.banki.ru/banks'

    def get_bank_ratings(self):
        # Полный URL для запроса рейтинга банков
        full_url = f'{self.base_url}/ratings/'

        # Отправка запроса и получение ответа от сервера
        response = requests.get(full_url)

        # Проверка успешности ответа
        if response.status_code != 200:
            raise Exception(f"Ошибка при доступе к URL: статус {response.status_code}")

        # Использование pandas для чтения таблицы из HTML
        df_list = pd.read_html(response.content)

        # Предполагается, что нужная таблица - первая
        if len(df_list) > 0:
            df = df_list[0]
        else:
            Exception("Таблица не найдена в ответе")

        return df