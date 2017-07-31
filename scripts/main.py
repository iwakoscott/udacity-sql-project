#!/usr/bin/python3

# Author: Satoshi Scott Iwako
# Udacity SQL Project

import psycopg2

query_one = '''SELECT title FROM articles JOIN
        (SELECT path, count(*) AS n FROM log
        WHERE path like '/article/%'
        GROUP BY path
        ORDER BY n DESC
        LIMIT 3) as n_views
        ON n_views.path ILIKE '%' || articles.slug || '%'
        ORDER BY n_views.n DESC;'''

def part_one():
    with psycopg2.connect('dbname=news') as conn:
        cur = conn.cursor()
        cur.execute(query_one)
        data = [x[0] for x in cur.fetchall()]
        return data


def main():
    #TODO: 1. What are the most popular three articles of all time? Which
    #articles have been accessed the most? Present this information as a sorted
    #list with the most popular article at the top.
    print(part_one())

    #TODO: 2. Who are the most popular article authors of all time? That is,
    #when you sum up all of the articles each author has written, which authors
    #get the most page views? Present this as a sorted list with the most
    #popular author at the top.

    #TODO: 3. On which days did more than 1% of requests lead to errors?
    #The log table includes a column status that indicates the HTTP status code
    #that the news site sent to the user's browser.



if __name__ == '__main__':
    main()
