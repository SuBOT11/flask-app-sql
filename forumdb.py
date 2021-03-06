# "Database code" for the DB Forum.
# 
import datetime
import psycopg2
import bleach
from os import environ
s = environ.get('S')
u = environ.get('U')
p = environ.get('P')


DBNAME = "forum"


def get_posts():
    """Return all posts from the 'database', most recent first."""
    
    db = psycopg2.connect(host=s, user=u, password=p, database=DBNAME)

    c = db.cursor()
    c.execute("select content, time from posts order by time desc")
    posts = c.fetchall()
    db.close()
    return posts


def add_post(content):
    """Add a post to the 'database' with the current timestamp."""

    db = psycopg2.connect(host=s, user=u, password=p, database=DBNAME)
    c = db.cursor()
  
    c.execute("insert into posts values (%s)", (bleach.clean(content),))
    db.commit()
    db.close()
