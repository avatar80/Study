from database import init_db
from database import (db_session, init_db)
from models import USERS

def show_tables():
    queries = db_session.query(USERS)
    entries = [dict(id=q.id, datetime=q.datetime, string=q.string) for q in queries]
    print(entries)


def add_entry(datetime, string):
    t = USERS(datetime, string)
    db_session.add(t)
    db_session.commit()


def delete_entry(datetime, string):
    db_session.query(USERS).filter(USERS.datetime == datetime, USERS.string == string).delete()
    db_session.commit()

def main():
    init_db()
    add_entry("2015-02-06 09:00:05", "test1")
    show_tables()
    #delete_entry("2015-02-06 09:00:05", "test1")
    db_session.close()


if __name__ == "__main__":
    main()