import scrapy
import re

class ImdbWikiSpider(scrapy.Spider):
    name = "imdb_wiki"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/List_of_American_films_of_2023"]

    def parse(self, response):
        # Every table on the page
        tables = response.xpath('//table[contains(@class,"wikitable")]')

        for table in tables:
            rows = table.xpath(".//tr")[1:]  # Exclude the header
            for row in rows:
                cells = row.xpath(".//td")
                
                if len(cells) >= 4:
                    title = cells[0].xpath(".//a/text()").get(default="").strip()
                    director = cells[1].xpath(".//a/text()").get(default="").strip()
                    cast_list = cells[2].xpath(".//a/text()").getall()
                    cast = ", ".join([c.strip() for c in cast_list if c.strip() != ""])
                    genre = cells[3].xpath("string(.)").get(default="").strip()
                    
                    notes = ""
                    if len(cells) > 4:
                        notes_raw = cells[4].xpath("string(.)").get(default="").strip()
                        # Remove numbers in parentheses
                        notes = re.sub(r'\[\d+\]', '', notes_raw).strip()

                    # Ignore rows that don’t have a title or director
                    if title and director:
                        yield {
                            "title": title,
                            "director": director,
                            "cast": cast,
                            "genre": genre,
                            "notes": notes
                        }
