import sqlalchemy as db
from sqlalchemy import select
from sqlalchemy import create_engine 
from sqlalchemy import Column, Integer, String

name = input()

engine = db.create_engine('postgresql+psycopg2://postgres:atpq238rz@127.0.0.1:5433/postgres')
connection = engine.connect() 
metadata = db.MetaData()
table_engine = db.Table(name, metadata, autoload_with=engine)

class TableCrud:
    def __init__(self, table):
        self.table = table

    def add(self, column_name, column_type):
        try:
            if column_name not in self.table.columns: 
                query = f'ALTER TABLE {self.table} ADD {column_name} integer;'
                connection.execute(query) 
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
                item = []
                stmt = select(self.table.columns.column_name)
                with engine.connect() as conn:
                    result = conn.execute(stmt)
                for row in result:
                    item.append(row.body)
                return item
            else:
                raise Exception("Column does not exist")
        except Exception as e:
                print(e)

    def update(self, column_name, new_name, new_type):
        try:
            if column_name in self.table.columns:
                with engine.connect() as conn:
                    conn.execute(f'ALTER TABLE {self.table} RENAME COLUMN {column_name} TO {new_name}')
                    conn.execute(f'ALTER TABLE {self.table} ALTER COLUMN {new_name} TYPE {new_type}')
            else:
                raise Exception("Column does not exist")
        except Exception as e:
            print(e)

    def delete(self, column_name):
        try:
            if column_name in self.table.columns:
                with engine.connect() as conn:
                    conn.execute(f'ALTER TABLE {self.table} DROP COLUMN {column_name}')
            else:
                raise Exception("Column does not exist")
        except Exception as e:
            print(e)

crud_obj = TableCrud(table_engine)
crud_obj.add("hello", String)
print(crud_obj.getItems())