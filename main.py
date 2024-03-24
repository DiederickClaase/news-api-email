import requests
from send_email import send_email

topic = "tesla"

api_key = "152f7e7e6a4047bdbcbd14f6734f2349"

url = "https://newsapi.org/v2/everything?"f"q={topic}&""from=2024-02-24&sortBy=publishedAt&\
apiKey=152f7e7e6a4047bdbcbd14f6734f2349&language=en"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article title and description
body = ""
for article in content["articles"][0:21]:
    if article["description"] is not None:
        body = "Subject: Today's Top 20 News Articles" + "\n" + body + article["title"]\
               + "\n" + article["description"]\
               + "\n" + article["url"]\
               + 2*"\n"

print(body)

body.encode("UTF-8")
body = body.encode('ascii', 'ignore').decode('ascii')
send_email(message=body)

