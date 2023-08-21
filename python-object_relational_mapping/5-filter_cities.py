
# 5. All cities by state
# mandatory

# Write a script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa

#     Your script should take 4 arguments: mysql username, mysql password, database name and state name (SQL injection free!)
#     You must use the module MySQLdb (import MySQLdb)
#     Your script should connect to a MySQL server running on localhost at port 3306
#     Results must be sorted in ascending order by cities.id
#     You can use only execute() once
#     The results must be displayed as they are in the example below
#     Your code should not be executed when imported

# guillaume@ubuntu:~/$ cat 4-cities_by_state.sql
# -- Create states table in hbtn_0e_4_usa with some data
# CREATE DATABASE IF NOT EXISTS hbtn_0e_4_usa;
# USE hbtn_0e_4_usa;
# CREATE TABLE IF NOT EXISTS states ( 
#     id INT NOT NULL AUTO_INCREMENT, 
#     name VARCHAR(256) NOT NULL,
#     PRIMARY KEY (id)
# );
# INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

# CREATE TABLE IF NOT EXISTS cities ( 
#     id INT NOT NULL AUTO_INCREMENT, 
#     state_id INT NOT NULL,
#     name VARCHAR(256) NOT NULL,
#     PRIMARY KEY (id),
#     FOREIGN KEY(state_id) REFERENCES states(id)
# );
# INSERT INTO cities (state_id, name) VALUES (1, "San Francisco"), (1, "San Jose"), (1, "Los Angeles"), (1, "Fremont"), (1, "Livermore");
# INSERT INTO cities (state_id, name) VALUES (2, "Page"), (2, "Phoenix");
# INSERT INTO cities (state_id, name) VALUES (3, "Dallas"), (3, "Houston"), (3, "Austin");
# INSERT INTO cities (state_id, name) VALUES (4, "New York");
# INSERT INTO cities (state_id, name) VALUES (5, "Las Vegas"), (5, "Reno"), (5, "Henderson"), (5, "Carson City");

# guillaume@ubuntu:~/$ ./5-filter_cities.py root root hbtn_0e_4_usa Texas

# guillaume@ubuntu:~/$ cat 4-cities_by_state.sql | mysql -uroot -p
# Enter password: 
# guillaume@ubuntu:~/$ ./5-filter_cities.py root root hbtn_0e_4_usa Texas
# Dallas, Houston, Austin
# guillaume@ubuntu:~/$ ./5-filter_cities.py root root hbtn_0e_4_usa Hawaii

# guillaume@ubuntu:~/$  

# No test cases needed

# ///////////////////////////////////////////////

#!/usr/bin/python3
"""takes in the name of a state as an argument and
lists all cities of that state,
using the database hbtn_0e_4_usa"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT cities.name\
                FROM cities LEFT JOIN states\
                ON states.id = cities.state_id\
                WHERE states.name = %s\
                ORDER BY cities.id ASC", (sys.argv[4],))
    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))
    cur.close()
    db.close()
