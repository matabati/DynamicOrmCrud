import sqlalchemy as db
from sqlalchemy.orm import sessionmaker

name = input("what is your table name? ")

engine = db.create_engine('postgresql+psycopg2://')
connection = engine.connect() 
metadata = db.MetaData()
table_engine = db.Table(name, metadata, autoload_with=engine)

Session = sessionmaker(bind=engine)
session = Session()

class Data_crud:

    def __init__(self, session, table):
        self.session = session
        self.table = table

    def createItem(self, data):

        keys_list =  ''
        values_list = ''

        keys = data.keys()
        for key in keys:
            keys_list = keys_list + key + ','
        keys_list = keys_list[:-1]

        values = data.values()
        for value in values:
            values_list = values_list + '\'' + value + '\'' + ','
        values_list = values_list[:-1]

        query = f'INSERT INTO {self.table}({keys_list}) VALUES({values_list});'
        connection.execute(query)
        self.session.commit()

    def getItems(self):
        items = self.session.query(self.table).all()
        return items

    def getOneItem(self, id):
        item = self.session.query(self.table).filter_by(id= id).first()
        return item

    def updateItem(self, id, new_data): 
        try:
            self.session.begin()
            for key, value in new_data.items():
                query = f'UPDATE {self.table} SET {key} = \'{value}\' WHERE id = \'{id}\';'
                connection.execute(query)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            print(f"An error occurred: {e}")
        finally:
            session.close()

    def deleteItem(self, id):
        self.session.query(self.table).filter_by(id= id).delete()
        self.session.commit()

crud_obj = Data_crud(session, table_engine)
#print(crud_obj.getOneItem('baec6dac-1d89-44bc-be83-1316ddc26625'))
#crud_obj.createItem({'body' : 'atefe', 'taggable_type' : 'App\Models\Search', 'created_at' : '2023-11-22 15:51:14', 'updated_at' : '2023-11-22 15:51:14', 'taggable_id' : '6f958558-32e7-414a-be78-8872df996320', 'id' : 'baec6dac-1d89-44bc-be83-1316ddc26625'})
