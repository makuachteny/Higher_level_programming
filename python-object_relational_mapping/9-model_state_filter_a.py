#!/usr/bin/python3
<<<<<<< HEAD
"""
script that list all objects that contain a letter that takes 3 args
"""


if __name__ == "__main__":
    from sys import argv
    from model_state import State, Base
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    st = session().query(State).filter(State.name.like('%a%')).order_by(
        State.id).all()
    if st:
        for stat in st:
            if 'a' in stat.name:
                print("{}: {}".format(stat.id, stat.name))
    session().close()
=======
"""Lists all state Object that contain letter."""


import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                    argv[2],
                                                                    argv[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    s = '%a%'
    states = session.query(State).filter(State.name.like(s)).order_by(State.id)
    for state in states:
        print("{}: {}".format(state.id, state.name))
    session.close()
>>>>>>> fdf18b6fab8375e89fd798686f733c098325ac33
