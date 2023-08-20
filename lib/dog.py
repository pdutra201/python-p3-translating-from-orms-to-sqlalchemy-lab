from models import Dog
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (create_engine, desc,
    Index, Column, DateTime, Integer, String)
from sqlalchemy.orm import sessionmaker


def create_table(base, engine):
    if __name__ == '__main__':
        base.metadata.create_all(engine)

def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    dogs = session.query(Dog).all()
    return dogs

def find_by_name(session, name):
    dog = session.query(Dog).filter(Dog.name.like(f'{name}')).first()
    return dog

def find_by_id(session, id):
    dog = session.query(Dog).filter(Dog.id == id).first()
    return dog

def find_by_name_and_breed(session, name, breed):
    dog = session.query(Dog).filter(Dog.name.like(f'{name}'), Dog.breed.like(f'{breed}')).first()
    return dog

def update_breed(session, dog, breed):
    session.query(Dog).filter(Dog.id == dog.id).update({
        Dog.breed: breed
    })