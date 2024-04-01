SELECT Reviewer_Name, COUNT(*) AS ReviewCount
FROM review_table
GROUP BY Reviewer_Name
ORDER BY ReviewCount DESC;