# Импорт библитек, необходимых для EDA
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
from matplotlib import pyplot as plt

colors = ['#b5de2b', '#6ece58', '#35b779', '#1f9e89', '#26828e', '#31688e', '#3e4989', '#482878', '#440154', '#253494', '#225ea8', '#1d91c0','#41b6c4','#7fcdbb','#c7e9b4','#edf8b1','#ffffd9']

relative_path = 'data/AptamerModifData.csv'
df = pd.read_csv(relative_path)
df = df.drop(columns = ['Article', 'DOI', 'Origin sequence', 'Melting temperature, oC', 'Comments'])
df['Stability t1/2, h'] = pd.to_numeric(df['Stability t1/2, h'], errors='coerce')
df = df.dropna()


def plot_pie(df, column, title, colors):
    """
    Построение круговой диаграммы для указанного столбца DataFrame.

    Parameters:
    df (pd.DataFrame): Исходный DataFrame.
    column (str): Название столбца для построения диаграммы.
    title (str): Заголовок диаграммы.
    colors (list): Список цветов для диаграммы.
    """
    if column not in df.columns:
        raise ValueError(f"Столбец '{column}' не найден в DataFrame")

    value_counts = df[column].value_counts()

    # Построение круговой диаграммы
    fig = px.pie(values=value_counts.values, names=value_counts.index, color_discrete_sequence=colors, title=title)

    # Вывод графика
    fig.show()

def plot_bar(df, column, title, colors):
    """
    Построение стобчатой диаграммы для указанного столбца DataFrame.

    Parameters:
    df (pd.DataFrame): Исходный DataFrame.
    column (str): Название столбца для построения диаграммы.
    title (str): Заголовок диаграммы.
    colors (list): Список цветов для диаграммы.
    """
    if column not in df.columns:
        raise ValueError(f"Столбец '{column}' не найден в DataFrame")

    value_counts = df[column].value_counts()

    # Построение диаграммы
    fig = px.bar(df, x=value_counts.index, y=value_counts.values, 
                color=value_counts.index, color_discrete_sequence=colors, 
                title=title, labels={'x': '', 'y': 'Количество'})
    fig.update_layout(showlegend=False)
    # Вывод графика
    fig.show()


plot_bar(df, 'Environment', "Среды, использовавшиеся для определения стабильности", colors)
plot_bar(df, 'Type', "Типы последовательностей, представленных в датасете", colors)
plot_pie(df, 'Modified', "Соотношение модифицированных и немодифицированных последовательностей", colors)



# Создание подграфиков
fig = make_subplots(rows=1, cols=2, subplot_titles=("Гистограмма", "Violin Plot"), column_widths=[0.5, 0.5])

# Добавление гистограммы
hist_fig = px.histogram(df, x = "Stability t1/2, h",
         color_discrete_sequence = colors, 
         opacity = 0.8)


fig.add_trace(hist_fig['data'][0], row=1, col=1)

# Добавление violin диаграммы
violin_fig = px.violin(df, y="Stability t1/2, h",
        color_discrete_sequence=colors)


fig.add_trace(violin_fig['data'][0], row=1, col=2)

# Настройка макета
fig.update_layout(showlegend=True, title_text="Распределение значений периода полураспада", height=600,  width=1200) 

fig.show()



# Создание подграфиков
fig = make_subplots(rows=1, cols=2, subplot_titles=("Гистограмма ", "Box Plot"), column_widths=[0.5, 0.5])

# Добавление гистограммы
hist_fig = px.histogram(df, x = "Stability t1/2, h", color = 'Type',
         color_discrete_sequence = colors, 
         opacity = 0.7)


for trace in hist_fig['data']:
    fig.add_trace(trace, row=1, col=1)

# Добавление violin диаграммы
violin_fig = px.box(df, y="Stability t1/2, h", x="Type", color="Type",
        color_discrete_sequence=colors)

for trace in violin_fig['data']:
    fig.add_trace(trace, row=1, col=2)

fig.add_trace(violin_fig['data'][0], row=1, col=2)

# Настройка макета
fig.update_layout(barmode='stack', showlegend=True, title_text="Распределение значений периода полураспада среди различных типов последовательностей", height=600,  width=1200) 

fig.show()



# Создание подграфиков
fig = make_subplots(rows=1, cols=2, subplot_titles=("Гистограмма", "Box Plot"), column_widths=[0.5, 0.5])

# Добавление гистограммы
hist_fig = px.histogram(df, x = "Stability t1/2, h", color = 'Modified',
         color_discrete_sequence = colors, 
         opacity = 0.7)


for trace in hist_fig['data']:
    fig.add_trace(trace, row=1, col=1)

# Добавление violin диаграммы
violin_fig = px.box(df, y="Stability t1/2, h", x="Modified", color="Modified",
        color_discrete_sequence=colors)

for trace in violin_fig['data']:
    fig.add_trace(trace, row=1, col=2)

fig.add_trace(violin_fig['data'][0], row=1, col=2)

# Настройка макета
fig.update_layout(barmode='stack', showlegend=True, title_text="Распределение значений периода полураспада среди модифицированных и немодифицированных последовательностей", height=600,  width=1200) 

fig.show()


import re
from collections import defaultdict
from modifications import modifications_dict

# Регулярное выражение для поиска модификаций
# Мы используем позиционный захват, чтобы найти модификации, которые не являются префиксами других модификаций
modification_pattern = re.compile('|'.join(map(re.escape, modifications_dict.keys())))

# Словарь для подсчета модификаций
modification_count = defaultdict(int)

# Проход по каждой строке в датасете
for seq in df['Sequence']:
    # Нахождение всех модификаций в строке
    found_modifications = modification_pattern.findall(seq)
    
    # Множество для хранения уникальных модификаций в этой строке
    unique_modifications = set()
    
    for mod in found_modifications:
        # Проверяем, добавлена ли модификация в множество
        if mod not in unique_modifications:
            # Если нет, добавляем её и увеличиваем счетчик модификации
            unique_modifications.add(mod)
            modification_count[mod] += 1

# Вывод результатов
for mod, count in modification_count.items():
    print(f"{modifications_dict[mod]}: {count}")

    modification_df = pd.DataFrame.from_dict(modification_count, orient='index', columns=['Count'])
modification_df = modification_df.reset_index()
modification_df['Modification'] = modification_df['index'].map(modifications_dict)

# Создание столбчатой диаграммы
fig = px.bar(
    modification_df, 
    x='Modification', 
    y='Count', 
    color='Modification', 
    color_discrete_sequence=colors, 
    title='Количество модификаций каждого вида',
    labels={'Modification': 'Вид модификации', 'Count': 'Количество вхождений'},
    text='Count'  # Добавляем значения на столбцы
)

fig.update_layout(
    showlegend=False,    
    height=600,  width=1200
)

fig.update_traces(textposition='outside')

# Отображение графика
fig.show()