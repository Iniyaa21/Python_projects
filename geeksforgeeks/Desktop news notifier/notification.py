from demo import news
from plyer import notification

news_ = news()
lst = news_[1].split()
msg, start, end, n = [], 0, 20, len(lst)//20 + 1

for i in range(n):
    string = " ".join(lst[start: end])
    msg.append(string)
    start += 20
    end += 20

for ele in msg:
    notification.notify(
        title="Top news",
        message=ele)
