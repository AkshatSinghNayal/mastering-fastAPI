import requests
from fastapi import FastAPI
from bs4 import BeautifulSoup


# url = "example.com"

# response = requests.get(url)

# soup = BeautifulStoneSoup(requests.txt , "html.parse")
# print(soup.title.text)




app = FastAPI()

@app.get("/news")
def get_news(page : int , limit : int =  5):
    url = "https://indianexpress.com/"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    title =[]

    for item in soup.find_all("a", class_="article-click topblockNews__sidebarLink"):
        title.append(item.text)

    start = (page-1)*limit
    end = start+limit

    return{
        "page" : page,
        "limit" : limit,
        "total" : len(title),
        "data" : title[start:end]
    } 