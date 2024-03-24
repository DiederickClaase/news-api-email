import requests
from send_email import send_email

api_key = "152f7e7e6a4047bdbcbd14f6734f2349"

url = ("https://newsapi.org/v2/everything?q=tesla&from=2024-02-24&sortBy=publishedAt&apiKey\
=152f7e7e6a4047bdbcbd14f6734f2349")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article title and description
body = ""
for article in content["articles"]:
    if article["description"] is not None:

        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

print(body)
body.encode("utf-8")
send_email(message=body)



