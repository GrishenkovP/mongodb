# Подключаем библиотеку
import pymongo
from pymongo import MongoClient
import datetime
import pprint

# Если запускаем контейнер в Docker
# docker run -d -p 127.0.0.1:27017:27017 --name mongodb mongo

# Cоединение с сервером базы данных (по умолчанию подключение осуществляется на localhost:27017)
client = MongoClient('localhost', 27017)

# Получение доступа к базе данных
db = client.db_test

# Данные в MongoDB представлены и хранятся в виде JSON документов.
# В PyMongo мы используем словари представления документов.
project = {"name": "A1","description": "NoSQL data warehouse","tags": ["db", "mongodb", "pymongo"],"date": datetime.datetime.utcnow()}

# Добавление документа в коллекцию. Коллекция представляет собой группу документов, хранящихся в MongoDB,
# и может рассматриваться как эквивалент таблицы в реляционной базе данных. Когда документ будет добавлен,
# автоматически создается специальный ключ - "_id", если документ уже не содержит таковой.
# Значение "_id" должно быть уникальным для коллекции. insert_one () возвращает экземпляр InsertOneResult.
projects = db.projects
projects_id = projects.insert_one(project).inserted_id

# Массовое добавление документов в коллекцию
project_list = [{"name": "A2","description": "SQL data warehouse","tags": ["db", "postgresql"],"date": datetime.datetime.utcnow()},
            {"name": "A3","description": "NoSQL data warehouse","tags": ["db", "redis"],"date": datetime.datetime.utcnow()},
            {"name": "B2","description": "Python. Script. Data Science","tags": ["python", "pandas", "numpy"],"date": datetime.datetime.utcnow()},
            {"name": "B3","description": "Python. Script. ETL","tags": ["python", "etl", "airflow"],"date": datetime.datetime.utcnow()},
            {"name": "C1","description": "R. Data Science","tags": ["r"],"date": datetime.datetime.utcnow()},
            {"name": "C4","description": "Scala. Data Science","tags": ["scala"],"date": datetime.datetime.utcnow()}
           ]
result_insert = projects.insert_many(project_list)

# Проверяем, что коллекция projects физически создалась в БД.
print(db.list_collection_names())

# Получение певого документа из коллекции
project_first = projects.find_one()
print(project_first)

# Перебрать все документы
for i in projects.find():
    print(i)

# Подсчет записей по условию
count_A3 = projects.count_documents({"name": "A3"})
print(count_A3)

# Сортировка записей по условию
for i in projects.find().sort("name"):
    pprint.pprint(i)

# Выбор столбцов для вывода (1/0)
for i in projects.find({},{"name":1,"_id":0}).sort("name"):
    pprint.pprint(i)

# Логические операторы (работает только в MongoDB Compass)
# for i in projects.find({$or:[{"name":"A1"},{"tags": "scala"}]}):
#     pprint.pprint(i)
