import csv
import requests
from bs4 import BeautifulSoup
import unicodedata
import time
from datetime import datetime, timedelta


def scrape_reviews(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}

    reviews = []
    page_num = 1
    while True:
        page_url = f"{url}&page={page_num}"
        response = requests.get(page_url, headers=headers)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')

        review_containers = soup.find_all(class_='afkKaa-4T28-')
        if not review_containers:
            break

        for review in review_containers:
            reviewer_name = review.find(class_='_1p30XHjz2rI- C7Tp-bANpE4-').get_text(strip=True)
            rating = review.find(class_='tSiVMQB9es0-').get_text(strip=True)
            review_text = review.find(class_='l9bbXUdC9v0- ZatlKKd1hyc- ukvN6yaH1Ds-').get_text(strip=True)
            review_date = extract_review_date(review)

            #Normalize review text to handle special characters
            review_text = normalize_text(review_text)

            reviews.append({'Review_Date': review_date, 'Reviewer_Name': reviewer_name, 'Rating': rating, 'Review_Text': review_text})

        page_num += 1
        time.sleep(2)  #Add a delay between requests

    return reviews


def extract_review_date(review):
    #Find the date element
    date_element = review.find(class_='iLkEeQbexGs-')

    if date_element:
        date_str = date_element.get_text(strip=True)
        print("Date string:", date_str)  #Add this line to print the date string

        try:
            #Try to parse the date in the "Dined on" format
            review_date = datetime.strptime(date_str, 'Dined on %B %d, %Y').date()
            print("Parsed as 'Dined on' format. Review date:", review_date)
        except ValueError:
            #If not "Dined on" format, assume it's in "days ago" format
            if 'days ago' in date_str:
                print("Parsing as 'days ago' format...")
                try:
                    days_ago = int(date_str.split()[1])  # Extract the number of days
                    print("Days ago:", days_ago)
                    review_date = datetime.now().date() - timedelta(days=days_ago)
                    print("Review date:", review_date)
                except ValueError as e:
                    #Handle the case where the format is invalid
                    print("Error:", e)
                    review_date = None
                    print("Invalid format for 'days ago'")
            else:
                print("Error: Invalid date format")
                review_date = None
    else:
        print("Error: Date element not found")
        review_date = None

    return review_date




def save_csv(reviews, filename):
    with open(filename, 'w', newline='', encoding='utf-8-sig') as csvfile:
        fieldnames = ['Review_Date', 'Reviewer_Name', 'Rating', 'Review_Text']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(reviews)


def normalize_text(text):
    #Normalize text to NFKD form to handle special characters
    normalized_text = unicodedata.normalize('NFKD', text)
    return normalized_text


if __name__ == "__main__":
    url = 'https://www.opentable.com/r/legal-sea-foods-framingham?corrid=c50ba8c0-0109-4925-8946-2321a6448f49&p=2&sd=2024-03-21T21%3A00%3A00&sortBy=newestReview'
    reviews = scrape_reviews(url)
    save_csv(reviews, 'reviews.csv')
