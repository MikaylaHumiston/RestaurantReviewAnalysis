SELECT TOP 1 Review_Text AS HighestRatedReview
FROM review_table
WHERE Rating = (SELECT MAX(Rating) FROM review_table);

SELECT TOP 1 Review_Text AS LowestRatedReview
FROM review_table
WHERE Rating = (SELECT MIN(Rating) FROM review_table);