"""script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys


def main():
    """Main function"""

    db_config = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db_config.cursor()
    query = "SELECT * FROM states ORDER BY id ASC;"

    cursor.execute(query)

    result = cursor.fetchall()
    for row in result:
        print(row)

    # Closing connection and cursor
    cursor.close()
    db_config.close()


if __name__ == "__main__":
    main()
