
# 7. All states via SQLAlchemy
# mandatory

# Write a script that lists all State objects from the database hbtn_0e_6_usa

#     Your script should take 3 arguments: mysql username, mysql password and database name
#     You must use the module SQLAlchemy
#     You must import State and Base from model_state - from model_state import Base, State
#     Your script should connect to a MySQL server running on localhost at port 3306
#     Results must be sorted in ascending order by states.id
#     The results must be displayed as they are in the example below
#     Your code should not be executed when imported

# guillaume@ubuntu:~/$ cat 7-model_state_fetch_all.sql
# -- Insert states
# INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

# guillaume@ubuntu:~/$ cat 7-model_state_fetch_all.sql | mysql -uroot -p hbtn_0e_6_usa
# Enter password: 
# guillaume@ubuntu:~/$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa
# 1: California
# 2: Arizona
# 3: Texas
# 4: New York
# 5: Nevada
# guillaume@ubuntu:~/$ 

# No test cases needed

# ///////////////////////////////////////////////

#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa"""

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
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()
