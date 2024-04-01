SELECT COUNT(*) AS Total_Reviews,
       AVG(Rating) AS Average_Rating,
       MAX(Rating) AS Highest_Rating,
       MIN(Rating) AS Lowest_Rating,
	   AVG(LEN(Review_Text)) AS Avg_Review_Length

FROM review_table;
