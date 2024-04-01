SELECT r.Reviewer_Name,
       AVGRating.AvgRating,
       r.ReviewCount
FROM (
    SELECT Reviewer_Name, 
           COUNT(*) AS ReviewCount
    FROM review_table
    GROUP BY Reviewer_Name
) r
JOIN (
    SELECT Reviewer_Name,
           CAST(AVG(CAST(Rating AS FLOAT)) AS FLOAT) AS AvgRating
    FROM review_table
    GROUP BY Reviewer_Name
) AvgRating ON r.Reviewer_Name = AvgRating.Reviewer_Name
ORDER BY r.ReviewCount DESC, AvgRating ASC;
