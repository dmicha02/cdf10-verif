import requests
from bs4 import BeautifulSoup

url = "https://www.athle.fr/asp.net/main.html/html.aspx?htmlid=129"

# Fetch the HTML content of the website
response = requests.get(url)
html_content = response.content

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find the <div> with class="titlefr"
div_titlefr = soup.findAll('div', class_='titlefr')

# Check if the <div> exists and contains an <a> tag
if div_titlefr:
    for div in div_titlefr:
        a_tag = div.find('a')
        if a_tag:
            if "Championnats de France de 10 km" == a_tag.text:
                print("Available!")
                print(a_tag['href'])
            else:
                print("Not yet!")