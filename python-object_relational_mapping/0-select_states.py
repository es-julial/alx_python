#!/usr/bin/python3

# 0. Get all states
# mandatory

# Write a script that lists all states from the database hbtn_0e_0_usa:

# Your script should take 3 arguments: mysql username, mysql password
# and database name (no argument validation needed)
# You must use the module MySQLdb (import MySQLdb)
# Your script should connect to a MySQL server running on localhost at
# port 3306
# Results must be sorted in ascending order by states.id
# Results must be displayed as they are in the example below
# Your code should not be executed when imported

# guillaume@ubuntu:~/$ cat 0-select_states.sql
# -- Create states table in hbtn_0e_0_usa with some data
# CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
# USE hbtn_0e_0_usa;
# CREATE TABLE IF NOT EXISTS states (
#  id INT NOT NULL AUTO_INCREMENT,
#  name VARCHAR(256) NOT NULL,
# PRIMARY KEY (id)
# );
# INSERT INTO states (name) VALUES ("California"), ("Arizona"),
# ("Texas"), ("New York"), ("Nevada");

# guillaume@ubuntu:~/$ cat 0-select_states.sql | mysql -uroot -p
# Enter password:
# guillaume@ubuntu:~/$ ./0-select_states.py root root hbtn_0e_0_usa
# (1, 'California')
# (2, 'Arizona')
# (3, 'Texas')
# (4, 'New York')
# (5, 'Nevada')
# guillaume@ubuntu:~/$

# No test cases needed

# ////////////////////////////////////////////////////////////////

"""lists all states from the database hbtn_0e_0_usa"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
