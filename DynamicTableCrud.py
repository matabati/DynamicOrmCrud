import sqlalchemy as db
from sqlalchemy.orm import sessionmaker

name = input("what is your table name?")

engine = db.create_engine('')
connection = engine.connect() 
metadata = db.MetaData()
table_engine = db.Table(name, metadata, autoload_with=engine)

Session = sessionmaker(bind=engine)
session = Session()

class TableCrud:
    def __init__(self, table):
        self.table = table

    def createItem(self, column_name, column_type):
        try:
            if column_name not in self.table.columns: 
                query = f'ALTER TABLE {self.table} ADD {column_name} {column_type};'
                connection.execute(query) 
                session.commit()
            else:
                raise Exception("This column already exists")
        except Exception as e:
            print(e)

    def getItems(self):
        items = self.table.columns.keys()
        return items

    def getOneItem(self, column_name):
        try:
            if column_name in self.table.columns:
                items = session.query(self.table.c[column_name]).all()
                return items
            else:
                raise Exception("Column does not exist")
        except Exception as e:
                print(e)

    def updateItem(self, column_name, new_name, new_type):
        try:
            if column_name in self.table.columns:
                query = f'ALTER TABLE {self.table} RENAME COLUMN {column_name} TO {new_name};'
                connection.execute(query) 
                query = f'ALTER TABLE {self.table} ALTER COLUMN {new_name} TYPE {new_type};'
                connection.execute(query)
                session.commit()
            else:
                raise Exception("Column does not exist")
        except Exception as e:
            print(e)

    def deleteItem(self, column_name):
        try:
            if column_name in self.table.columns:
                query = f'ALTER TABLE {self.table} DROP COLUMN {column_name};'
                connection.execute(query) 
                session.commit()

            else:
                raise Exception("Column does not exist")
        except Exception as e:
            print(e)


crud_obj = TableCrud(table_engine)