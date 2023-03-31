import request
import selectorlib

url = "https://programmer100.pythonanywhere.com/tours/"

def scrape(url):
    '''scrape the page sorce from url'''

    response = request.get(url)
    source_text = response.text
    return source_text

if __name__ == "__main__":
    scrape(url)

