# DataDrivenEngineering

## Анализ датасета модификаций аптамеров
Этот проект предназначен для чтения, обработки и визуализации данных о модификациях аптамеров из CSV файла. Данные представляют собой информацию об экспериментах по увеличению стабильности олигонуклеотидов: нуклеотидную последовательность, включенные модификации, данные о стабильности, выраженные в периоде полураспада, условия эксперимента, тип олигонуклеотида, название и doi статьи. Код позволяет получить различные графики для анализа распределения стабильности, а также представленности раздичныз сред, типов и модификаций.

## Используемые библиотеки

*   **pandas (pd):** Для работы с данными в формате таблиц (DataFrame).
*   **plotly.express (px):** Для создания интерактивных графиков.
*   **plotly.subplots (make_subplots):** Для создания графиков с несколькими подграфиками.
*   **re:** Для работы с регулярными выражениями.
*   **collections.defaultdict:** Для удобного подсчета элементов.

## Файлы
AptamerModifData.csv: Исходный файл с данными о модифицированных апамерах.
modifications.py: Файл с словарем модификаций.

## Результаты

После запуска кода будут сгенерированы и отображены следующие графики:

*   Столбчатая диаграмма, показывающая распределение последовательностей по типам сред.
*   Столбчатая диаграмма, показывающая распределение последовательностей по типам олигонуклеотидов.
*   Круговая диаграмма, показывающая соотношение модифицированных и немодифицированных последовательностей.
*   Совмещенные гистограмма и violin plot для распределения значений периода полураспада.
*   Совмещенные гистограмма и box plot для распределения значений периода полураспада по типам последовательностей.
*   Совмещенные гистограмма и box plot для распределения значений периода полураспада по признаку модификации.
*   Столбчатая диаграмма, показывающая количество вхождений каждой модификации.

## Анализ модификаций
Код предусматривает поиск и подсчет различных модификаций в последовательностях апамеров, а также их визуализацию в виде столбчатой диаграммы.
