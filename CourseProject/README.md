## Курсовая работа. Датасеты.
по курсу *Машинное обучение*

Выполнена студенткой группы М8О-114М-22 Сучковой Натальей

### Суть задания
Было выполнено мини-исследование датасета ModelNet, с обзором его структуры, типа данных (point clouds), измеряемых на этом датасете метрик и задач.
Также была применена предобученная модель PointNet для классификации 3D объектов.

[Ссылка](https://drive.google.com/file/d/1dO3KAN53qlH_XytXsQ2Kjro4P6KsMSxc/view?usp=sharing) на скачивание zip архива датасета, или его можно найти [здесь](https://www.kaggle.com/datasets/balraj98/modelnet40-princeton-3d-object-dataset).

### Содержание
Внутри содержится основной .ipynb ноутбук, файл save.pth с весами предобученной сети 

**Немного о данных**

Goal

The goal of Princeton ModelNet project is to provide researchers in computer vision, computer graphics, robotics and cognitive science, with a comprehensive clean collection of 3D CAD models for objects.

Content

ModelNet40 dataset contains 12,311 pre-aligned shapes from 40 categories, which are split into 9,843 (80%) for training and 2,468 (20%) for testing. The CAD models are in Object File Format (OFF). Matlab functions to read and visualize OFF files are provided in Princeton Vision Toolkit (PVT).

To build the core of the dataset, a list of the most common object categories in the world was compiled, using the statistics obtained from the SUN database. Once a vocabulary for objects was established, 3D CAD models belonging to each object category was collected using online search engines by querying for each object category term. Then, human workers on Amazon Mechanical Turk were hired to manually decide whether each CAD model belonged to the specified cateogries, using an in-house designed tool with quality control. To obtain a very clean dataset, 10 popular object categories were chosen while manually deleted the models that did not belong to these categories. Furthermore, manual alignment of orientation of CAD models was performed for the 10-class subset.
