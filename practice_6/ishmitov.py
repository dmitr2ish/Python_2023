from data_manager import DataManager
from visualizer import Visualizer

def main():
    # Инициализация
    file_path = './data/data__1_.csv'
    title_table = "Количество личных дел, обработанных приемной комиссией по часам"
    x_label = 'Дата'
    y_label = 'Час'
    data_manager = DataManager(file_path, 'Дата создания')

    # Загрузка и обработка
    data_manager.load_data()
    data_manager.preprocess_data_by_date_column()

    # Создание таблицы
    pivot_table = data_manager.create_pivot_table_by_column('ЛД')

    # Визуализация таблицы
    Visualizer.plot_heatmap(pivot_table, (15, 9), title_table, x_label, y_label)

if __name__ == "__main__":
    main()
