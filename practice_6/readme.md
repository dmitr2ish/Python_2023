Используйте файл data.csv в качестве источника данных. Это данные о работе приёмной комиссии университета.

Вот структура объекта DataFrame:
````
Index(['№', 'ЛД', 'ФИО', 'Статус', 'Приориетет', 'Рейтинг', 'Факультет',
       'Форма обучения', 'Период обучения', 'Срок обучения', 'Курс',
       'Код Специальности', 'Специальность', 'Образовательный уровень',
       'Комиссия', 'Тип док. об обр.', 'Серия', 'Номер', 'Ср. балл', 'Награды',
       'Оригинал', 'Коментарии', 'Бюджет', 'Общий конкурс', 'Целевой конкурс',
       'Дата создания', 'Тех. секретарь', 'Unnamed: 27'],
      dtype='object')
````
Столбец ‘ЛД’ содержит уникальный номер личного дела абитуриента. По уникальным записям этого столбца можно определить, сколько абитуриентов и в какое время обратились в приёмную комиссию.

Столбец ‘Дата создания’ содержит не только дату обращения, но и время. Абитуриенты, у которых дата и час совпадают, а различаются только минуты, обратились в приёмную комиссию в один и тот же час. Оцените нагрузку на приёмную комиссию.

Для этого необходимо:

- Преобразовать тип данных в столбце ‘Дата создания’ при помощи метода pd.to_datetime (25 баллов).
- Добавить к данным два столбца: ‘Date’ и ’Hour’, взяв данные из столбца ‘Дата создания’ (25 баллов).
- Построить сводную таблицу, содержащую количество личных дел, принятых приёмной комиссией в течение каждого рабочего часа (index = 'Hour', columns = 'Date') (25 баллов).
- Построить графическое представление данных в виде heatmap из библиотеки SeaBorn (25 баллов).