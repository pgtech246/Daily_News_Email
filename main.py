import requests
from send_email import send_email
from datetime import date, timedelta

current_date = date.today()
ten_days_ago = current_date - timedelta(days=10)

with open("api_key.txt", "r") as file:
    api_key = file.read()

url = f"https://newsapi.org/v2/everything?q=AI&from={ten_days_ago}&sortBy=publishedAt&apiKey={api_key}&language=en"

request = requests.get(url)
content = request.json()

body = ""
for article in content['articles'][:11]:
    body = body + str(article['title']) + '\n' + str(article['description']) + '\n' + str(article['url']) + 2*'\n'

body = body.encode('utf-8')
send_email(body)
