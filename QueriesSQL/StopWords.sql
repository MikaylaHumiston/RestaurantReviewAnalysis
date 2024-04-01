BULK INSERT StopWords
FROM 'C:\Users\mikay\Documents\SQL Server Management Studio\LegalReviews\StopWords.txt'
WITH
(
    FIELDTERMINATOR = ',',  -- Specify the field terminator in your text file
    ROWTERMINATOR = '\n',   -- Specify the row terminator in your text file
    FIRSTROW = 2            -- Specify if the first row contains column headers
);