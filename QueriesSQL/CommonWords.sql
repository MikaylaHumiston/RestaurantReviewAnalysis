SELECT TOP 10 value AS CommonWords, COUNT(*) AS WordCount
FROM review_table
CROSS APPLY STRING_SPLIT(Review_Text, ' ') AS Words
LEFT JOIN StopWords ON Words.value = StopWords.StopWords
WHERE Words.value <> '' -- Exclude empty strings
  AND StopWords.StopWords IS NULL -- Exclude stopwords
GROUP BY value
ORDER BY WordCount DESC;