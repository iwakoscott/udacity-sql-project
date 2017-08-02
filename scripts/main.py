#!/usr/bin/python3

# Author: Satoshi Scott Iwako
# Udacity SQL Project

import psycopg2

query_one = '''
        SELECT title FROM articles JOIN
        (SELECT path, count(*) AS n FROM log
        WHERE path like '/article/%'
        GROUP BY path
        ORDER BY n DESC
        LIMIT 3) as n_views
        ON n_views.path ILIKE '%' || articles.slug || '%'
        ORDER BY n_views.n DESC;'''

query_two = '''
        SELECT articlesauthors.name, COUNT(*) AS n FROM (SELECT * FROM articles
        JOIN authors
        ON articles.author=authors.id) AS articlesauthors
        JOIN log ON log.path ILIKE '%' || articlesauthors.slug || '%'
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

    SELECT grandquery.thedate
    FROM
      (
        SELECT failed.thedate,
        CAST(failed.n AS DECIMAL)/total.intotal AS percentage
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
    WHERE grandquery.percentage > 0.01;
'''

def part_one():
    """
    1. What are the most popular three articles of all time? Which
    #articles have been accessed the most? Present this information as a sorted
    #list with the most popular article at the top.
    """
    with psycopg2.connect('dbname=news') as conn:
        cur = conn.cursor()
        cur.execute(query_one)
        data = [x[0] for x in cur.fetchall()]
        return data

def part_two():
    """
    TODO: 2. Who are the most popular article authors of all time? That is,
    when you sum up all of the articles each author has written, which authors
    get the most page views? Present this as a sorted list with the most
    popular author at the top.
    """
    with psycopg2.connect('dbname=news') as conn:
        cur = conn.cursor()
        cur.execute(query_two)
        data = [x[0] for x in cur.fetchall()]
        return data

def main():
    print(part_one())
    print(part_two())

    #TODO: 3. On which days did more than 1% of requests lead to errors?
    #The log table includes a column status that indicates the HTTP status code
    #that the news site sent to the user's browser.



if __name__ == '__main__':
    main()
