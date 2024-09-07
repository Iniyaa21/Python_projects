from demo import get_weather
from plyer import notification

tup = get_weather()
notification.notify(title="Weather update",
                    message=f"{tup[1]}\nCurrent temperature {tup[0]} in Chennai, India\n{tup[2]}")
