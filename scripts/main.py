#!/usr/bin/python3

# Author: Satoshi Scott Iwako
# Udacity SQL Project

import psycopg2

def query_one():
    sql = '''SELECT path, count(*) AS n FROM log
            WHERE path like '/article/%'
            GROUP BY path
            ORDER BY n DESC
            LIMIT 3;'''
            
def main():
    #TODO: 1. What are the most popular three articles of all time? Which
    #articles have been accessed the most? Present this information as a sorted
    #list with the most popular article at the top.

    #TODO: 2. Who are the most popular article authors of all time? That is,
    #when you sum up all of the articles each author has written, which authors
    #get the most page views? Present this as a sorted list with the most
    #popular author at the top.

    #TODO: 3. On which days did more than 1% of requests lead to errors?
    #The log table includes a column status that indicates the HTTP status code
    #that the news site sent to the user's browser.



if __name__ == '__main__':
    main()
