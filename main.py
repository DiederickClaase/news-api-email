import requests

api_key = "152f7e7e6a4047bdbcbd14f6734f2349"

url = ("https://newsapi.org/v2/everything?q=tesla&from=2024-02-24&sortBy=publishedAt&apiKey=152f7e7e6a4047bdbcbd14f6734f2349")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article title and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])

