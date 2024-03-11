import requests

with open("api_key.txt", "r") as file:
    api_key = file.read()

url = f"https://newsapi.org/v2/everything?q=tesla&from=2024-02-11&sortBy=publishedAt&apiKey={api_key}"

request = requests.get(url)
content = request.json()

for article in content["articles"]:
    print("author: ", article["author"])
    print("title: ", article["title"])
    print("content: ", article["content"])
    print("url: ", article["url"], "\n")
