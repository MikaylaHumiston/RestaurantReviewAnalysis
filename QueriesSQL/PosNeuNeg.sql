SELECT YEAR(Review_Date) AS Review_Year,
       MONTH(Review_Date) AS Review_Month,
       SUM(CASE
               WHEN Rating >= 4 THEN 1
               ELSE 0
           END) AS Positive_Reviews,
       SUM(CASE
               WHEN Rating = 3 THEN 1
               ELSE 0
           END) AS Neutral_Reviews,
       SUM(CASE
               WHEN Rating < 3 THEN 1
               ELSE 0
           END) AS Negative_Reviews,
       COUNT(*) AS Total_Reviews,
       CONVERT(DECIMAL(5, 2), 100.0 * SUM(CASE
                                            WHEN Rating >= 4 THEN 1
                                            ELSE 0
                                        END) / COUNT(*)) AS Positive_Proportion,
       CONVERT(DECIMAL(5, 2), 100.0 * SUM(CASE
                                            WHEN Rating = 3 THEN 1
                                            ELSE 0
                                        END) / COUNT(*)) AS Neutral_Proportion,
       CONVERT(DECIMAL(5, 2), 100.0 * SUM(CASE
                                            WHEN Rating < 3 THEN 1
                                            ELSE 0
                                        END) / COUNT(*)) AS Negative_Proportion
FROM review_table
GROUP BY YEAR(Review_Date), MONTH(Review_Date)
ORDER BY Positive_Proportion DESC, Review_Year DESC, Review_Month DESC;
