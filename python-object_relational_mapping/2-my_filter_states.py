
# 2. Filter states by user input
# mandatory

# Write a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.

#     Your script should take 4 arguments: mysql username, mysql password, database name and state name searched (no argument validation needed)
#     You must use the module MySQLdb (import MySQLdb)
#     Your script should connect to a MySQL server running on localhost at port 3306
#     You must use format to create the SQL query with the user input
#     Results must be sorted in ascending order by states.id
#     Results must be displayed as they are in the example below
#     Your code should not be executed when imported

# guillaume@ubuntu:~/$ cat 0-select_states.sql
# -- Create states table in hbtn_0e_0_usa with some data
# CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
# USE hbtn_0e_0_usa;
# CREATE TABLE IF NOT EXISTS states ( 
#     id INT NOT NULL AUTO_INCREMENT, 
#     name VARCHAR(256) NOT NULL,
#     PRIMARY KEY (id)
# );
# INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

# guillaume@ubuntu:~/$ cat 0-select_states.sql | mysql -uroot -p
# Enter password: 
# guillaume@ubuntu:~/$ ./2-my_filter_states.py root root hbtn_0e_0_usa 'Arizona'
# (2, 'Arizona')
# guillaume@ubuntu:~/$ 

# No test cases needed

# ///////////////////////////////////////////////

#!/usr/bin/python3
"""takes in an argument and displays all values
in the states table of hbtn_0e_0_usa
where name matches the argument"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'\
                ORDER BY states.id ASC".format(sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
