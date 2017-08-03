# udacity-sql-project

## How to Download code:

Click "Fork" at the top of this webpage and click "Download ZIP" or copy the link provided and clone the repository through the command line.

## Requirements?
psql, Python3.

## How to run?
Before running the program in the terminal you must first download and unzip the following file to get the newsdata.sql file (https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). After doing so run, 'psql -d news -f newsdata.sql' to create the 'news' database. Then navigate to the directory 'scripts' containing 'main.py' and run 'python main.py'. 

## 'main.py' Design
'main.py' is structured very logically. First we import psycopg2 to connect to the 'news' database using psql. The first chunk of the code consists of the complex queries necessary to answer the questions provided for this assignment labeled: query_one, query_two, and query_three. I then have a helper function 'get_results' that returns the results of a query into a nice list. I call this function three times with each of the aforementioned queries and print out the results in 'main'.  

## Copy of Output?
Open 'output.txt' in your favorite text editor or simply run 'cat output.txt' to view the output of 'main'.

## What is the directory 'misc'?
You don't actually have to go in there at all. I just put a .txt file that helped me visualize the three tables provided for this assignment.
