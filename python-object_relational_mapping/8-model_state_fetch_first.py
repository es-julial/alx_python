#!/usr/bin/python3
# 8-model_state_fetch_first.py
"""import a model and fitch the first row"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format
        (argv[1],
         argv[2],
         argv[3]),
        pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    if session.query(State).count() == 0:
        print("Nothing")

    state = session.query(State).first()

    print('{}: {}'.format(state.id, state.name))

    session.close()
