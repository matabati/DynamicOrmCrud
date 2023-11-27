import sqlalchemy as db
from sqlalchemy import select
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine 
from sqlalchemy import text

name = input()

engine = db.create_engine('postgresql+psycopg2://postgres:atpq238rz@127.0.0.1:5433/postgres')
metadata = db.MetaData()
table_name = db.Table(name, metadata, autoload_with=engine)

new_column = Column('nananana', String)
table_name.append_column(new_column)

alter_stmt = table_name.to_metadata(metadata).compile(engine)

#Execute the ALTER TABLE statement
with engine.connect() as conn:
    conn.execute(alter_stmt)

#connection = engine.connect() 
#query = text(f'ALTER TABLE {table_name} ADD colorrring VARCHAR(255);')
#connection.execute(query) 