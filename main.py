import request
import selectorlib

url = "https://programmer100.pythonanywhere.com/tours/"

def scrape(url):
    '''scrape the page sorce from url'''

    response = request.get(url)
    source_text = response.text
    return source_text

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file('extract.yaml')
    value = extractor.extract(source)['tours']

if __name__ == "__main__":
    scraped = scrape(url)
    extracted = extract(scraped)

    if extracted != 'No Upcoming Tour'

