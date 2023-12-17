import pandas as pd


class DataManager:
    DATE_COLUMN = 'Date'
    HOUR_COLUMN = 'Hour'

    def __init__(self, file_path, date_column, encoding='cp1251', delimiter=';'):
        self.date_column = date_column
        self.delimiter = delimiter
        self.encoding = encoding
        self.file_path = file_path
        self.data = None

    def load_data(self):
        self.data = pd.read_csv(self.file_path, encoding=self.encoding, delimiter=self.delimiter)
        return self.data

    def preprocess_data_by_date_column(self):
        self.data[self.date_column] = pd.to_datetime(self.data[self.date_column], dayfirst=True)
        self.data[DataManager.DATE_COLUMN] = self.data[self.date_column].dt.date
        self.data[DataManager.HOUR_COLUMN] = self.data[self.date_column].dt.hour

    def create_pivot_table_by_column(self, column):
        pivot_table = self.data.pivot_table(index=DataManager.HOUR_COLUMN, columns=DataManager.DATE_COLUMN,
                                            values=column, aggfunc='count')
        pivot_table = pivot_table.fillna(0).astype(int)
        return pivot_table
