import pandas as pd
import pyodbc
from sqlalchemy import create_engine

df = pd.read_csv('reviews.csv')

#print(df.head)

#print(df.describe())

#print(df.info())

#remove duplicates
df.drop_duplicates(inplace=True)

#handle missing values. replacing them with an empty string
df['Review_Text'] = df['Review_Text'].fillna('')

#remove special characters
df['Review_Text'] = df['Review_Text'].str.replace(r'[^a-zA-Z0-9\s]', '')

#convert text to lowercase
df['Review_Text'] = df['Review_Text'].str.lower()

#display cleaned dataset
#print("\nCleaned Dataset:")
#print(df.head())
#print(df.describe())
#print(df.info())

df.to_csv("cleaned_reviews.csv", index=False, encoding='utf-8-sig')

conn_str = 'mssql+pyodbc://DESKTOP-F156GB8\SQLEXPRESS/LegalReviewsDB?driver=ODBC+Driver+17+for+SQL+Server'

engine = create_engine(conn_str)

df = pd.read_csv('cleaned_reviews.csv')

df.to_sql(name='review_table', con=engine, if_exists='replace', index=False)

engine.dispose()