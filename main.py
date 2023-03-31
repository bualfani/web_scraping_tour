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

def send_email():


def store(extrated):
    with open('data.txt', 'a') as file:
        file.write(extrated + '\n')

def read(extracted):
    with open('data.txt', 'r') as file:
        return file.read()


if __name__ == "__main__":
    scraped = scrape(url)
    extracted = extract(scraped)

    content = read(extracted)
    if extracted != 'No upcoming tour':
        if extracted not in content:
            store(extracted)
            send_email()

