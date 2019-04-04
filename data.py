# importing requests package 
import requests

# url to get top headlines of business news in India 
url = " https://newsapi.org/v2/top-headlines?country=in&sort_by=top&category=business&apiKey=f6e1c6b98075456692613b67879c33f5"

# fetching data in json format 
data = requests.get(url).json() 

# getting all articles in a string article 
article = data["articles"]

