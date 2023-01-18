#!/usr/bin/python3
<<<<<<< HEAD
"""Script that adds Louisiana to the database"""

import sys
=======
"""Add Louisiana to a DB."""


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
    new_state = State(name='Louisiana')
    session.add(new_state)
    state = session.query(State).filter_by(name='Louisiana').first()
    print(str(state.id))
    session.commit()
    session.close()
