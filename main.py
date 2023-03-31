import request
import selectorlib
import smtplib, ssl
import os

url = "https://programmer100.pythonanywhere.com/tours/"

def scrape(url):
    '''scrape the page sorce from url'''

    response = request.get(url)
    source_text = response.text
    return source_text

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file('extract.yaml')
    value = extractor.extract(source)['tours']


def send_email(message):
    host = 'smtp.gmail.com'
    port = 465
    username = 'your_email'
    password = os.getenv("Password")
    receiver = "your_email"
    my_context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

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
            send_email(message="New Event was found")

