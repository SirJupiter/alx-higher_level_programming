#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
import sys


def main():
    """Main entry function"""

    try:
        db_config = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        )

        cursor = db_config.cursor()

        query = "SELECT cities.id, cities.name, states.name FROM cities \
            INNER JOIN states ON cities.state_id = states.id \
                ORDER BY cities.id ASC;"

        try:
            cursor.execute(query)
        except MySQLdb.Error as e:
            print("An error occured: {}".format(e))
        else:
            result = cursor.fetchall()
            for row in result:
                print(row)

    except MySQLdb.Error as e:
        print("Error: Could not connect to Database ({})".format(e))

    finally:
        if cursor:
            cursor.close()
        if db_config:
            db_config.close()


if __name__ == "__main__":
    main()
