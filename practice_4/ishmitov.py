from banki_app import BankiApp

# Создание экземпляра класса BankiApp
app = BankiApp()

# Получение данных рейтинга банков и сохранение в переменную df
df = app.get_bank_ratings()

# Проверка результата
print(df.head())
