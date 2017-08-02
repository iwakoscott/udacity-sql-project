# udacity-sql-project

## How to Download code:

Click "Fork" at the top of this webpage and click "Download ZIP" or copy the link provided and clone the repository through the command line.

## Requirements?
psql and Python3.
 
## How to run?
In your terminal navigate to the directory 'scripts' containing 'main.py' and run 'python main.py'. 

## 'main.py' Design
'main.py' is structured very logically. First we import psycopg2 to connect to the 'news' database using psql. The first chunk of the code consists of the complex queries necessary to answer the questions provided for this assignment labeled: query_one, query_two, and query_three. I then have a helper function 'get_results' that returns the results of a query into a nice list. I call this function three times with each of the aforementioned queries and print out the results in 'main'.  

## Copy of Output?
Open 'output.txt' in your favorite text editor or simply run 'cat output.txt' to view the output of 'main'.
