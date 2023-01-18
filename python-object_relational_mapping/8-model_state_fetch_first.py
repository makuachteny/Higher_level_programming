#!/usr/bin/python3
<<<<<<< HEAD
"""Script that prints the first state."""
=======
"""List the first state."""
>>>>>>> fdf18b6fab8375e89fd798686f733c098325ac33


import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
<<<<<<< HEAD
    eng = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
=======
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                    argv[2],
                                                                    argv[3]))
>>>>>>> fdf18b6fab8375e89fd798686f733c098325ac33
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    first_state = session.query(State).order_by(State.id).first()
    if first_state is not None:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")
    session.close()
