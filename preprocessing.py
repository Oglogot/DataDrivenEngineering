# Импорт библитек
import pandas as pd
import os
from sklearn.preprocessing import MinMaxScaler

# Получаем путь к директории, где находится текущий скрипт
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
print(f"Current working directory: {os.getcwd()}")

# Все равно при запуске через терминал работает, а через "Run" в vs code нет. Штош

if not os.path.exists("data"):
    os.makedirs("data")
    print("Папка 'data' создана.")

# Загрузка датасета
relative_path = 'data/AptamerModifData.csv'
if not os.path.exists(relative_path):
    raise FileNotFoundError(f"Файл {relative_path} не найден. Проверьте путь.")
df = pd.read_csv(relative_path)

# Очистка датасета
df = df.drop(columns = ['Article', 'Origin sequence', 'Melting temperature, oC', 'Comments'])
df['Stability t1/2, h'] = pd.to_numeric(df['Stability t1/2, h'], errors='coerce')
df = df.dropna()
df = df[df['Stability t1/2, h'] <= 500] # Удаление выбросов
df.to_csv("./data/AptamerModifDataCleaned.csv", index=False) # Сохраняем очищенный датасет

# Нормализация и энкодинг признаков
scaler = MinMaxScaler()
df_scaled = df.copy()
df_scaled[['Concentration of envi, %', 'Temperature, oC']] = scaler.fit_transform(
    df[['Concentration of envi, %', 'Temperature, oC']])
df_encoded = pd.get_dummies(df_scaled, columns=['Environment', 'Type'])
df_encoded.to_csv("./data/AptamerModifDataPreproc.csv", index=False) # Сохраняем подготовленный датасет