
# 6. First state model
# mandatory

# Write a python file that contains the class definition of a State and an instance Base = declarative_base():

#     State class:
#         inherits from Base Tips
#         links to the MySQL table states
#         class attribute id that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
#         class attribute name that represents a column of a string with maximum 128 characters and can’t be null
#     You must use the module SQLAlchemy
#     Your script should connect to a MySQL server running on localhost at port 3306
#     WARNING: all classes who inherit from Base must be imported before calling Base.metadata.create_all(engine)

# guillaume@ubuntu:~/$ cat 6-model_state.sql
# -- Create database hbtn_0e_6_usa
# CREATE DATABASE IF NOT EXISTS hbtn_0e_6_usa;
# USE hbtn_0e_6_usa;
# SHOW CREATE TABLE states;

# guillaume@ubuntu:~/$ cat 6-model_state.sql | mysql -uroot -p
# Enter password: 
# ERROR 1146 (42S02) at line 4: Table 'hbtn_0e_6_usa.states' doesn't exist
# guillaume@ubuntu:~/$ cat 6-model_state.py
# #!/usr/bin/python3
# """Start link class to table in database 
# """
# import sys
# from model_state import Base, State

# from sqlalchemy import (create_engine)

# if __name__ == "__main__":
#     engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
#     Base.metadata.create_all(engine)

# guillaume@ubuntu:~/$ ./6-model_state.py root root hbtn_0e_6_usa
# guillaume@ubuntu:~/$ cat 6-model_state.sql | mysql -uroot -p
# Enter password: 
# Table   Create Table
# states  CREATE TABLE `states` (\n  `id` int(11) NOT NULL AUTO_INCREMENT,\n  `name` varchar(128) NOT NULL,\n  PRIMARY KEY (`id`)\n) ENGINE=InnoDB DEFAULT CHARSET=latin1
# guillaume@ubuntu:~/$ 

# No test cases needed

# ///////////////////////////////////////////////

#!/usr/bin/python3
"""Definition of the State class"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """Class State"""

    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True,
                primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
