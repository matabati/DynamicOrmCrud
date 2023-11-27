from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = 'postgresql+psycopg2://postgres:atpq238rz@127.0.0.1:5433/postgres'

engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)
session = Session()


class Data_crud:

    def __init__(self, session):
        self.session = session

    def add(self, data):
        self.session.add(data)
        self.session.commit()

    def getItems(self):
        items = self.session.query(Recipe).all()
        return items

    def getOneItem(self, id):
        item = self.session.query(Recipe).filter_by(id= id).first()
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
        order = self.session.query(Recipe).filter_by(id= id).first()
        if order:
            self.session.delete(order)
            self.session.commit()

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    ingredients = Column(String)
    instructions = Column(String)

new_recipe = Recipe(id=1, name='Pizza', ingredients='Dough, Tomato Sauce, Cheese', instructions='Bake at 200C for 20 minutes')
crud_obj = Crud(session)

crud_obj.add(new_recipe)

recipes = crud_obj.getItems()
for recipe in recipes:
    print(recipe.name, recipe.ingredients, recipe.instructions)

#crud_obj.update(1, {'name': 'New Name', 'ingredients': 'New Ingredients'})