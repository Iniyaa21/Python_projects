import requests
from bs4 import BeautifulSoup


def get_weather():

    html_src_code = requests.get(
        "https://weather.com/en-IN/weather/today/l/c22247914cbb82cd681cd51c2e04e8e9e7ef952fb32c47ce4842d04f312def3b").text
    soup = BeautifulSoup(html_src_code, "lxml")
    # print(soup.prettify().encode("utf-8"))

    temp = soup.find(
        "div", class_="CurrentConditions--primary--2DOqs").text.encode("utf-8")
    string = temp.decode("ascii", "ignore")
    string = (string.split("Day"))[0]
    temperature = string[:2]
    weather = string[2:]

    prec = soup.find(
        "div", class_="InsightNotification--root--3R2Jo PrecipIntensityCard--InsightNotification--24_-s InsightNotification--background--2JOmA").p.text.encode("utf-8")
    precipitation = prec.decode("ascii", "ignore")

    return temperature, weather, precipitation
