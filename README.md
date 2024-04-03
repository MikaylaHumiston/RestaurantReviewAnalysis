# RestaurantReviewAnalysis
Author: Mikayla Humiston

This is a data analysis project with the aim of collecting and analyzing reviews for a specific Legal Sea Foods restaurant location. As an employee of this Legal Sea Foods, I have been interested in using the guest reviews to gain insight into the overall perception of the restaurant and ways that we can facilitate a superb dining experience. My personal goals of this project are expanding my knowledge and skills with Python and MATLAB in applications pertaining to data analysis.

## [Web Scraping](ScrapingCleaningPython)
Python BeautifulSoup is used to scrape guest reviews from OpenTable in scrape.py. This program targets html class attributes associated with the date, reviewer name, rating, and review text for each review. The program clean_and_store.py then prepares the data by cleaning it, removing special characters, converting text to lower case, then connecting and storing it in a Microsoft SQL Server database.

## [Collected Data](Data)
Review data is stored in csv files, making them easy to work with in Python and store in a table in SQL Server. Notice: These csv files are very large and not suitable for viewing in Github.

## [SQL Queries](QueriesSQL)
SQL Queries written in SQL Server Management Studio to gain insight into the review data, generate stats, find trends, and investigate the data.

## [Visualization with MATLAB](VisualModelsMATLAB)
Used MATLAB Database Explorer toolbox to connect to SQL Server data source, retrieve information, write SQL queries, generate data visualizations. The file is a MATAB live script.
