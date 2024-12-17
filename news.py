# Api key: 33e58909a4a94bb2a61579caf9735b9b
import requests
import os


class NewsFeed:
    base_url='https://newsapi.org/v2/everything?'
    api_key = os.getenv('NEWS_API_KEY')

    def __init__(self, interest, from_date, to_date):
        self.to_date = to_date
        self.from_date = from_date
        self.interest = interest

    def get(self):
        url = f"{self.base_url}" \
              f"qInTitle={self.interest}&" \
              f"from={self.from_date}&" \
              f"to={self.to_date}&" \
              "language=en&" \
              f"apiKey={self.api_key}"

        res = requests.get(url)
        content = res.json()
        articles = content['articles']

        email_body = ''
        for article in articles:
            email_body += article['title'] + '\n' + article['url'] + '\n\n'

        return email_body


if __name__ == "__main__":
    news_feed = NewsFeed(interest="psychology", from_date="2024-12-10", to_date="2024-12-15")
    print(news_feed.get())

