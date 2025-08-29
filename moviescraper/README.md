🎬 Movies Scraper
📌 Overview

This project is a web scraping tool built with Scrapy.It extracts data about movies, directors, cast, genres, and notes from the Wikipedia page:
List of American films of 2023.


The scraped data is stored in a clean CSV file for analysis, visualization, or portfolio use.

⚙️ Technologies Used

* Python 3.x

* Scrapy Framework

* XPath Selectors

* CSV Output




🚀 How it Works

The Scrapy spider:

1. Sends a request to the Wikipedia page.

2. Parses all wikitable tables on the page.

3. Extracts:
🎬 Movie Title

🎥 Director

👥 Cast

🎭 Genre

📝 Notes (if available)

4. Saves the extracted data to a CSV file.


📂 Project Structure
movies-scraper/
│
├── moviescraper/              # Scrapy project folder
│   ├── spiders/                # Contains the spider file
│   │   └── imdb_wiki.py
│   ├── items.py
│   ├── pipelines.py
│   └── settings.py
│
├── movies.csv                  # Final scraped data
└── README.md                   # Project documentation



| Title       | Director     | Cast                                       | Genre | Notes |
| ----------- | ------------ | ------------------------------------------ | ----- | ----- |
| The Old Way | Saban Films  | Nicolas Cage                               | —     | \[4]  |
| House Party | Warner Bros. | Calmatic, Stephen Glover, Tosin Cole       | —     | \[7]  |
| Sick        | Peacock      | John Hyams, Kevin Williamson, Gideon Adlon | —     | \[8]  |



📎 How to Run

Clone the repository:

git clone https://github.com/your-username/movies-scraper.git


Navigate into the project folder:

cd movies-scraper


Run the spider:

scrapy crawl imdb_wiki -o movies.csv

⭐ Future Improvements

* Include release year and movie ratings.

* Add more years or expand to international movies.

* Visualize data using Matplotlib / Seaborn.

* Store data in a database (SQLite / MongoDB) for larger datasets.

👤 Author:
     Tendo

📧 Email:
     tendooza123@gmail.com

🔗 GitHub:
     TendoOZA