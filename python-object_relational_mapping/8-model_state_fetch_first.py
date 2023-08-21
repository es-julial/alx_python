
# 8. First state
# mandatory

# Write a script that prints the first State object from the database hbtn_0e_6_usa

#     Your script should take 3 arguments: mysql username, mysql password and database name
#     You must use the module SQLAlchemy
#     You must import State and Base from model_state - from model_state import Base, State
#     Your script should connect to a MySQL server running on localhost at port 3306
#     The state you display must be the first in states.id
#     You are not allowed to fetch all states from the database before displaying the result
#     The results must be displayed as they are in the example below
#     If the table states is empty, print Nothing followed by a new line
#     Your code should not be executed when imported

# guillaume@ubuntu:~/$ ./8-model_state_fetch_first.py root root hbtn_0e_6_usa
# 1: California
# guillaume@ubuntu:~/$ 

# No test cases needed

# ///////////////////////////////////////////////

#!/usr/bin/python3
"""prints the first State object from the database hbtn_0e_6_usa"""

if __name__ == "__main__":

    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    first = session.query(State).order_by(State.id).first()
    if first:
        print("{}: {}".format(first.id, first.name))
    else:
        print("Nothing")
    session.close()
