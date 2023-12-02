import sqlalchemy as db
from sqlalchemy.orm import sessionmaker

name = input("what is your table name?")

engine = db.create_engine('')
connection = engine.connect() 
metadata = db.MetaData()
table_engine = db.Table(name, metadata, autoload_with=engine)

Session = sessionmaker(bind=engine)
session = Session()

class Data_crud:

    def __init__(self, session, table):
        self.session = session
        self.table = table

    def add(self, data):
        self.session.add(data)
        self.session.commit()

    def getItems(self):
        items = self.session.query(self.table).all()
        return items

    def getOneItem(self, id):
        item = self.session.query(self.table).filter_by(id= id).first()
        return item

    def update(self, id, new_data):
        try:
            self.session.begin()
            item = self.getOneItem(id)
            for key, value in new_data.items():
                setattr(item, key, value)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            print(f"An error occurred: {e}")

    def delete(self, id):
        order = self.session.query(self.table).filter_by(id= id).first()
        if order:
            self.session.delete(order)
            self.session.commit()

crud_obj = Data_crud(session, table_engine)