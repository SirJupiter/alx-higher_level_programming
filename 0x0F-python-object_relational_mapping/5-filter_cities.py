#!/usr/bin/python3
"""script that takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa"""

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
        state_name = sys.argv[4]

        query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC;
        """

        try:
            cursor.execute(query, (state_name,))
        except MySQLdb.OperationalError as e:
            print(f"An error occurred: {e}")
        except Exception:
            pass
        else:
            result = cursor.fetchall()

            for row in result:
                print(*row, end='')
                if result[len(result) - 1] != row:
                    print(", ", end='')

    except MySQLdb.Error as e:
        print(f"Error: Could not connect to database ({e})")


if __name__ == "__main__":
    main()
