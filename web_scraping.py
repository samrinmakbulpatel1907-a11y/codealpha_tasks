
import requests
from bs4 import BeautifulSoup
import csv
import os

# Public practice website
url = "https://books.toscrape.com/"

try:
    print("Connecting to website...")

    response = requests.get(
        url,
        timeout=30,
        headers={"User-Agent": "Mozilla/5.0"}
    )
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    data = []

    for book in books:
        title = book.h3.a.get("title", "Unknown")
        price = book.find(
            "p", class_="price_color"
        ).get_text(strip=True)
        availability = book.find(
            "p", class_="instock availability"
        ).get_text(strip=True)

        data.append([title, price, availability])

    # Save CSV in the same folder as this Python file
    folder = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(folder, "scraped_books.csv")

    with open(
        file_path, "w", newline="", encoding="utf-8-sig"
    ) as file:
        writer = csv.writer(file)
        writer.writerow(["Book Title", "Price", "Availability"])
        writer.writerows(data)

    print("\nWEB SCRAPING COMPLETED!")
    print("Total books scraped:", len(data))
    print("CSV file saved at:")
    print(file_path)

    print("\nFirst 5 books:")
    for row in data[:5]:
        print("Title:", row[0])
        print("Price:", row[1])
        print("Availability:", row[2])
        print("-" * 30)

except requests.RequestException as error:
    print("Website request failed:", error)

except (OSError, csv.Error) as error:
    print("File saving failed: