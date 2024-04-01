SELECT YEAR(Review_Date) AS Review_Year,
       MONTH(Review_Date) AS Review_Month,
       COUNT(*) AS Num_Reviews,
	   AVG(Rating) AS Average_Rating
FROM review_table
GROUP BY YEAR(Review_Date), MONTH(Review_Date)
ORDER BY Review_Year, Review_Month;