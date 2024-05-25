import requests
from bs4 import BeautifulSoup

class WikipediaParser:
    def __init__(self, url):
        self.url = url

    def get_page_content(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup.get_text()

    def count_word_occurrences(self, word):
        content = self.get_page_content()
        return content.lower().count(word.lower())

if __name__ == "__main__":
    wikipedia_url = "https://uk.wikipedia.org/wiki/%D0%91%D0%B5%D1%80%D1%81%D0%B5%D1%80%D0%BA_(%D0%BC%D0%B0%D0%BD%D2%91%D0%B0)"
    word_to_search = "берсерк"

    parser = WikipediaParser(wikipedia_url)
    occurrences = parser.count_word_occurrences(word_to_search)
    print(f"слово {word_to_search} вживалось {occurrences} раз на вікі")
