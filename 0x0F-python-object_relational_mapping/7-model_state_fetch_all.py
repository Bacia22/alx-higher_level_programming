#!/usr/bin/pyton3
"""
Script that lists all State objects from the database - Usage module SQLAlchemy
"""
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqllchemy.com import sessionmaker

if __name__== "__main":

    # create an engine
    engine = create_engine('mysql+mmysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3], pool_pre_ping=True

        # create a configured "Session" class
        Session = sessionmaker(bind=engine)
        #create a Session
        session = Session()
        Base.metadata.create_all(engine)

        s_tate = session.query(State).order_by(State.id).all()
        for state in s_tate:
            print("{}: {}".format(state.id, state.name))
        session.close()
