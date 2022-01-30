"""
Database connection and insertion logic.
"""
import os
import json

import psycopg2

from src.archtypes.path import Archive
from src.consts import SQL_INSERT, DB_TABLE_MAP

# Get secret config
with open(os.path.join(os.path.dirname(__file__), 'secrets.secret'), 'r') as secretfile:
    SECRETS = json.load(secretfile)

class DBConnection():
    """
    Object to simplify handling connections to the db.
    """
    conn = None
    cursor = None
    def __init__(self):
        self._connect()

    def _connect(self):
        """
        Connect to the Postgress db.
        """
        self.conn = psycopg2.connect(
            database=SECRETS["database"],
            user=SECRETS["user"]
        )
        self.cursor = self.conn.cursor()

    def insert(self, table, fields, values):
        """
        Insert the requested field/value combos as a new table entry.

        :param str table: the table on which to insert
        :param list[str] fields: the fields being inserted
        :param list[str] values: the value with corresponding indexes to the fields
        """
        fieldstr = ", ".join(fields)
        query = SQL_INSERT.format(table=table, fieldstr=fieldstr)
        query = query % (", ".join(["%s" for x in range(0, len(values))]))
        self.cursor.execute(query, values)
        self.conn.commit()

    def close(self):
        """
        ABSOLUTELY call this when you're done with the DBConnection object.
        """
        self.cursor.close()
        self.conn.close()


def getarchiveinsertkeys(archive):
    """
    Decontruct the archive python type into base types for easy sqledge.

    :param Archive archive: the archive to parse

    :returns: the DB table, fields to insert, and field values of this archive, as a 3-pair
    :rtype: str | list[str] | list[str]
    """
    table = DB_TABLE_MAP[archive.archtype]
    fields = []
    values = []
    for field, value in archive.parse():
        fields.append(field)
        values.append(value)
    return table, fields, values


def insertarchive(archive):
    """
    Insert the archive into the DB.
    If this goes wrong, there's gonna be a problem.

    :param Archive archives: the python archive object to enter into the DB
    """
    dbconn = DBConnection()
    table, fields, values = getarchiveinsertkeys(archive)
    dbconn.insert(table, fields, values)
    dbconn.close()
