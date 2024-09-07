import requests
from bs4 import BeautifulSoup


def news():
    # getting the headline
    html_src_code = requests.get(
        "https://timesofindia.indiatimes.com/india/tamil-nadu").text

    soup = BeautifulSoup(html_src_code, "lxml")

    headline = soup.find("span", class_="w_tle").a.text
    # print(headline)

    # getting the contents
    url = (soup.find("span", class_="w_tle").a)["href"]
    formatted_url = f"https://timesofindia.indiatimes.com{url}"

    content_src_code = requests.get(formatted_url).text

    soup = BeautifulSoup(content_src_code, "lxml")
    # print(soup.prettify().encode("utf-8"))

    content = soup.find("div", class_="_s30J clearfix").text.encode("utf-8")
    content = content.decode("ascii", "ignore")
    return headline, content
