#!/usr/bin/python3

# Author: Satoshi Scott Iwako
# Udacity SQL Project

import psycopg2
import datetime as dt

query_one = '''
    SELECT titles.title,
    COUNT(*) AS n FROM log JOIN
    (SELECT slug, title FROM articles) AS titles
    ON log.path LIKE '/article/' || titles.slug
    GROUP BY titles.title
    ORDER BY n DESC
    LIMIT 3;
'''

query_two = '''
        SELECT articlesauthors.name, COUNT(*) AS n FROM (SELECT * FROM articles
        JOIN authors
        ON articles.author=authors.id) AS articlesauthors
        JOIN log ON log.path ILIKE '%' || articlesauthors.slug
        GROUP BY articlesauthors.name
        ORDER BY n DESC;'''

query_three = '''
    WITH subquery AS
    (
      SELECT
      log.status,
      substring(CAST(log.time AS TEXT), 1, 10) AS thedate,
      count(*) AS n
      FROM log
      GROUP BY thedate, status
    )

    SELECT grandquery.thedate, round(grandquery.proportion*100, 2) as percent
    FROM
      (
        SELECT failed.thedate,
        CAST(failed.n AS DECIMAL)/total.intotal AS proportion
        FROM
        (
          (
            SELECT subquery.thedate, subquery.n
            FROM subquery
            WHERE subquery.status LIKE '404%') AS failed
            JOIN
              (
                SELECT subquery.thedate,
                sum(subquery.n) AS intotal
                FROM subquery
                GROUP BY subquery.thedate
              ) AS total
            on failed.thedate=total.thedate
          )
      ) AS grandquery
    WHERE grandquery.proportion > 0.01;
'''


def get_results(query):
    """Querys the 'news' database with the 'query' and returns the results based
    on the query provided as a list.
    """
    with psycopg2.connect('dbname=news') as conn:
        cur = conn.cursor()
        cur.execute(query)
        return cur.fetchall()


def main():
    # 1. What are the most popular three articles of all time? Which
    # articles have been accessed the most? Present this information as a
    # sorted list with the most popular article at the top.

    print('\nTop Three Popular Articles of All Time')
    for n, row in enumerate(get_results(query_one)):
        article, views = row
        print('{}. "{}"--{} views'.format(n + 1, article, views))

    # 2. Who are the most popular article authors of all time? That is,
    # when you sum up all of the articles each author has written, which
    # authors get the most page views? Present this as a sorted list with
    # the most popular author at the top.
    print('\nMost Popular Article Authors of All Time')
    for n, row in enumerate(get_results(query_two)):
        author, views = row
        print('{}. {}--{} views'.format(n + 1, author, views))

    print('''\nDays Where More Than 1% of Requests Lead to Errors''')
    # 3. On which days did more than 1% of requests lead to errors?
    # The log table includes a column status that indicates the HTTP
    # status code that the news site sent to the user's browser.
    for n, row in enumerate(get_results(query_three)):
        date, error = row
        date = dt.datetime.strptime(date, '%Y-%m-%d')
        dateasstr = dt.datetime.strftime(date, '%B %d, %Y')
        print('{}. {}--{}% errors'.format(n + 1, dateasstr, error))

if __name__ == '__main__':
    main()
