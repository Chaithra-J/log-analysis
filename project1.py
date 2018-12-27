#!/usr/bin/env python

import psycopg2

DBNAME = "news"


# Top three popular articles
def popular_articles():
    query = """SELECT articles.title, COUNT(*) AS num
            FROM articles
            JOIN log ON log.path
            LIKE concat('/article/%', articles.slug)
            GROUP BY articles.title ORDER BY num DESC LIMIT 3;"""
    db = psycopg2.connect('dbname=' + DBNAME)
    c = db.cursor()
    c.execute(query)
    rows = c.fetchall()
    db.close()
    print('\nPopular Articles are:')
    for i in rows:
        print(i[0] + ' : ' + str(i[1]) + " views ")


popular_articles()


# Top three authors of popular articles
def popular_authors():
    query = """SELECT authors.name, COUNT(*) AS num
            FROM authors
            JOIN articles ON authors.id = articles.author
            JOIN log ON log.path
            like concat('/article/%', articles.slug)
            GROUP BY authors.name ORDER BY num DESC LIMIT 3;"""
    db = psycopg2.connect('dbname=' + DBNAME)
    c = db.cursor()
    c.execute(query)
    rows = c.fetchall()
    db.close()
    print('\nPopular Authors are:')
    for i in rows:
        print(i[0] + ' : ' + str(i[1]) + " views")


popular_authors()


# Percentage errors
def percentage_errors():
    query = """SELECT total.day,
            ROUND(((errors.error_requests*1.0) / total.requests), 3)
            AS percent
            FROM (SELECT date_trunc('day', time) "day", count(*)
            AS error_requests
            FROM log WHERE status LIKE '404%' GROUP BY day)
            AS errors
            JOIN (SELECT date_trunc('day', time) "day",
            count(*) AS requests
            FROM log GROUP BY day)
            AS total ON total.day = errors.day
            WHERE (ROUND(((errors.error_requests*1.0)
             / total.requests), 3) > 0.01)
            ORDER BY percent DESC;"""
    db = psycopg2.connect('dbname=' + DBNAME)
    c = db.cursor()
    c.execute(query)
    rows = c.fetchall()
    db.close()
    print('\nDAYS WITH MORE THAN 1% ERRORS:')
    for i in rows:
        date = i[0].strftime('%B %d, %Y')
        errors = str(round(i[1]*100, 1)) + "%" + " errors"
        print(date + " on " + errors)


percentage_errors()
