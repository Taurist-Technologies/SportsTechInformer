from bs4 import BeautifulSoup
import requests
import constants as c
import blog_post
import datetime_checker as dt
from time import sleep
import logging

# Configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s")
file_handler = logging.FileHandler("logs.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def fetch_articles_from_sportstech_blog():
    url = c.SPORTS_TECHNOLOGY_URL
    soup = BeautifulSoup(requests.get(url).text, "html.parser")

    # Get all the articles
    articles = soup.find_all("article")

    for article in articles:
        time_published = article.find("time", class_="entry-date published")["datetime"]
        if dt.is_today_from_string(time_published):
            title = article.find("h2").text
            link = article.find("a")["href"]
            blog = blog_post.BlogPost(title, link)
            blog.send_to_slack()
        else:
            continue
    logger.info("Ran sports technology blog!")
    return


def fetch_articles_from_techcrunch():
    url = c.TECH_CRUNCH_URL
    soup = BeautifulSoup(requests.get(url).text, "html.parser")

    # Get all the articles
    articles = soup.find_all(
        "div", class_="post-block post-block--image post-block--unread"
    )

    for article in articles:
        time_published = article.find("time")["datetime"]
        if dt.is_today_from_string(time_published):
            title = article.find("h2", class_="post-block__title").text
            link = article.find("a", class_="post-block__title__link")["href"]
            blog = blog_post.BlogPost(title, link)
            blog.send_to_slack()
        else:
            continue
    logger.info("Ran tech crunch!")
    return


def fetch_articles_from_cnbc():
    url = c.CNBC_URL
    soup = BeautifulSoup(requests.get(url).text, "html.parser")

    # Get all the articles
    articles = soup.find_all("div", class_="Card-standardBreakerCard")

    for article in articles:
        time_published = (
            article.find("span", class_="Card-time").text.split(",")[1].strip()
        )
        if dt.is_today_from_string(time_published):
            title = article.find("a", class_="Card-title").text
            link = article.find("a")["href"]
            blog = blog_post.BlogPost(title, link)
            blog.send_to_slack()
        else:
            continue
    logger.info("Ran cnbc!")
    return


if __name__ == "__main__":
    fetch_articles_from_sportstech_blog()
    sleep(5)
    fetch_articles_from_techcrunch()
    sleep(5)
    fetch_articles_from_cnbc()
