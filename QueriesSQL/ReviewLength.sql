SELECT Review_Date, Reviewer_Name, Rating, Review_Text,
       LEN(Review_Text) AS Text_Length
FROM review_table
ORDER BY Text_Length DESC; -- Longest first
