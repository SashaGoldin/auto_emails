import yagmail
import os
import pandas
from news import NewsFeed
import datetime

today = datetime.datetime.today()
yesterday = today - datetime.timedelta(days=1)

df = pandas.read_excel('visitors.xlsx')
for index, row in df.iterrows():
    news_feed = NewsFeed(interest=row['interest'],
                         from_date=yesterday.strftime('%Y-%m-%d'),
                         to_date=today.strftime("%Y-%m-%d"))

    email = yagmail.SMTP(user="alex.it.goldin@gmail.com", password=os.getenv("GMAIL_PASS"))
    email.send(to=row['email'],
               subject=f"Your {row['interest']} news for today!",
               contents=f"Hi {row['name']}\n See what's on about {row['interest']} today.\n\n "
                        f"{news_feed.get()}\n\nAlex G")

