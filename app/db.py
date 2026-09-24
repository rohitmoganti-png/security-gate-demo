import sqlite3

from flask import g


def get_db() -> sqlite3.Connection:
    if "db" not in g:
        g.db = sqlite3.connect("billing.db")
        g.db.row_factory = sqlite3.Row
    return g.db
