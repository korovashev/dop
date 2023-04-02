from functools import reduce

def filter_news(positive_news, news_item):
    if not positive_news:
        return [news_item]

    last_news = positive_news[-1][0]
    now_news = news_item[0]

    if now_news > last_news:
        positive_news.append(news_item)

    return positive_news


with open('news.txt', 'r') as file:
    news = [(int(line.split()[0]), line.strip()) for line in file.readlines()]

positive_news = reduce(filter_news, news, [])

for i in positive_news:
    print(i[1])